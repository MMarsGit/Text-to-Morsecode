# Morse binary tree
This project contains a binary tree that functions as a morse tree.
There are two main functions in morse.py that is at the center of the project.
Using encode('string') you can enter a letter, word or phrase and it will be turned into its equivalent morese code.
Using decode('String') you can enter any morese encoding and it will be turned into the original phrase.

The other files concern testing. Assert_tests will run a couple of tests on the code.
moreseunit will perform an entire unit test of the code.

## What has been completed
The binary tree is fully functional. A search function allows any character to be located and for its binary code to be retrieved. My binary tree saves two pieces of data, one for its morese and one for its character. Saving the morse helps to simplify the program as while it is possible to trace the trees path, I have found it in the past to be less reliable. Saving two data points in each node allows the entire program to function more smoothly at the cost of size, which is not as important for a small implementation like this.
Add_child acts as the insert function for this tree. It takes the morse and character as arguments where it will follow the morse code to find the right location on the tree.
The tree can be printed to the console using print_tree().
The tree is intialised using initialise_tree.

## Running the code
The code can be run in any file by importing it. From there you only need to call morse.encode() or morse.decode() and it will work right out of the box.

