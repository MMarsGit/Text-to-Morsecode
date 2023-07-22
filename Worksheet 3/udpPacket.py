import asyncio
import base64
import time
import struct
import codecs
import websockets

# Function that calculates what the actual checksum should be
def compute_checksum(source, destination, payload):
    #binary values for each variable
    binSource = bin(source)
    binDestination = bin(destination)
    
    if isinstance(payload, str):
        byteArrayPayload = bytearray(payload, "utf8")
    else:
        byteArrayPayload = payload
    binLength = bin(len(str(payload)))
    # list for bytes array
    byteList = []

    # Put bytes into list
    for byte in byteArrayPayload:
        binaryPart = bin(byte)
        byteList.append(binaryPart)

    print(byteList)
    byteSum = bin(0)
    # Sum of all the bytes in byte array
    for byte in byteList:
        byteSum = bin(int(byteSum, 2) + int(byte, 2))

    # Sum of all the bytes
    addedBin = bin(int(binSource, 2) + int(binDestination, 2) + int(binLength, 2) + int(byteSum, 2))
    #not Opperation for checksum
    # is signed so prints negative
    notBin = ~(int(addedBin, 2))
    checksum = bin(notBin & 0b1111111111111111)
    print(checksum)
    return int(checksum, 2)

async def recieve_decode_packet(websocket):
    
    base64message = await websocket.recv()
    # base64 decoded packet
    decodedMessage = base64.b64decode(base64message)
    # The actual base 10 numbers for each variable
    source = int.from_bytes(decodedMessage[0:2],'little')
    destination = int.from_bytes(decodedMessage[2:4], 'little')
    length = int.from_bytes(decodedMessage[4:6], 'little')
    checksum = int.from_bytes(decodedMessage[6:8], 'little')
    # The message string sent by packet
    payload = decodedMessage[8:(length+8)].decode("utf-8")

    checksum = compute_checksum(source, destination, payload)

    # Formated & decoded packet printed to console
    print("Base64: " +str(base64message))
    print("Server Sent: " + str(decodedMessage))
    print("Decoded Packet: \{0}\{1}\{2}\{3}\ ".format(source, destination, length, checksum))
    print("source: " + str(source))
    print("destination: " + str(destination))
    print("Length: " + str(length))
    print("Checksum: " + str(checksum))
    print("message: " + payload)

    return destination, source

async def send_packet(websocket, destination, source, message):
    # build string
    # creates the byte from struct package
    # used this method so I can combine the bytes
    bytedest = struct.pack('i', destination)
    bytesource = struct.pack('i', source)
    length = 4
    bytelength = struct.pack('i', length)
    # getting checksum
    checksum = compute_checksum(source, destination, message)
    bytechecksum = struct.pack('i', checksum)
    #forms packet
    packet = bytesource+bytedest+message+bytelength+bytechecksum
    #sends packet to server
    await websocket.send(packet)
    return 0
    
async def main():
    uri = "ws://localhost:5612"
    async with websockets.connect(uri) as websocket:
        
        destination, source = await recieve_decode_packet(websocket)
        
        while True:

            await send_packet(websocket, destination, source, b'1111')

            destination, source = await recieve_decode_packet(websocket)

            time.sleep(1)
        
        return 0

if __name__ == "__main__":
    asyncio.run(main())