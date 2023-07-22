# Worksheet 3
## udpPacket.py
This file contains four methods.
One is the main() method.

### Main() method
It is an asynchronous method which allows it to wait for a response from the server.
The method calls two methods, recieve_decode_packet() and send_packet().
The main() method is looped to call these two methods every second.

### recieve_decode_packet() method
This method takes the parameter: websocket.
Websocket is the established connection with the server.

The method waits to recieve a packet from the server. From this it assigns each section of the packet to a variable.

compute_checksum() is then called and source, destination and payload are taken as parameters. The checksum is then retrieved.

all the variables are then printed out to the console.

### Send_packet() method
The send_packet() method takes the parameters: websocket, destination, source and the message to send.

The destination and source are packed into a byte. A bitelength is specified and along with the checksum is also packed into a byte.
All the bytes are then sent as a packet.

# Completed tasks
Task 1-3 have all been completed successfully. Task 4 has been attempted however the checksum does not seem to come out correctly. Never the less most of the compute_checksum function works correctly as it is the calculation of the checksum that does not come out correctly.

# Examples of code 