# Morese Code Decoder and Encoder
This program can convert text to morse code and vice versa.
The Core of it is a binary search tree that emulates a typical morse tree.
![image](https://github.com/MMarsGit/Text-to-Morsecode/assets/70379279/390b524a-50fb-43db-8747-93334aa2c7b8)

## Binary Tree
Under Worksheet 2 you will find the binary tree used to decode and encode morse messages.
For my binary tree I opted to store two data values at each node, one for the morse code and one for the character.
I recognise that it may be possible to store just the characters alone and only record the path taken however the added
complexity of doing this just to save on some space on an already small data structure pushed me towards doing it this way.
Due to this the encoding and decoding processes are very similar but both still benefit from the speed of searching on a binary tree.

## Remote Server
The Binary Tree was designed to communicate with a remote server hosted by my University. The program will still run correctly though
the main.py was designed for the remote server itself.

## UDP Packets
Though it is not the primary focus of the project, the folder worksheet 3 contains a program to recieve, decode and send UDP packets.
The UDP packets function as expected with a: source port, destination port, length and checksum, as well as the data itself.
As with the morse decoder and encoder, the UDP packets program was designed to work with the remote server.

