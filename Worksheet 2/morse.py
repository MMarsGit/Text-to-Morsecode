

#Class for each node on a binary tree


class BinaryNode:
    def __init__(self, morseData, char):
        self.char = char
        self.morseData = morseData
        self.result = None
        self.left = None
        self.right = None
        

    #Has a variable for number of morse characters
    def addChild(self,morseData, char):
        #morseCount sets the number of occured morse characters to 0
        morseCount = 0
        self._addChild(morseData, char, morseCount)

    #Add a child node to the Binary tree
    # Recurses down the tree based on conditions till a bottom node is reached 
    # where the node is then added    
    def _addChild(self, morseData, char, morseCount):
        if char == self.char:
            return
        
        if morseCount < len(morseData)-1:
            if morseData[morseCount] == '.':
                # add data in left tree
                if self.left:
                    morseCount += 1
                    self.left._addChild(morseData, char, morseCount)
                else:
                    self.left = BinaryNode("","")
                    morseCount += 1
                    self.left._addChild(morseData, char, morseCount)

            elif morseData[morseCount] == "-":
                # add data in right tree
                if self.right:
                    morseCount += 1
                    self.right._addChild(morseData, char, morseCount)
                else:
                    self.right = BinaryNode("", "")
                    morseCount += 1
                    self.right._addChild(morseData,char,morseCount)
        else:
            if morseData[morseCount] == ".":
                if self.left:
                    self.left.morseData = morseData
                    self.left.char = char
                else:
                    self.left = BinaryNode(morseData, char)
            else:
                if self.right:
                    self.right.morseData = morseData
                    self.right.char = char
                else:    
                    self.right = BinaryNode(morseData, char)         

    #Recurses down the tree and forms an array of all the nodes of the binary tree
    #Using an in order travesal algorithm
    def inOrderTraversal(self):
        elements = []

        # Travel left down the tree
        #elements array is returned to the next node and overwrites the element array of that node
        if self.left:
            elements += self.left.inOrderTraversal()

        # Added the current node to the array
        elements.append(self.char)
        # Travel right down the tree
        if self.right:
            elements += self.right.inOrderTraversal()

        return elements

    #Parent method of _printTree, prints the base node and sets the depth to 0
    def printTree(self):
        #Print root node first
        print(self.morseData)
        Depth = 0
        self._printTree(Depth)

    #Recurses down the tree and formats and prints it to the console
    def _printTree(self, Depth):

        if (self.left == False) or (self.right == False):
            Depth -= 1
        #Visit Left
        if self.left:
            Depth += 1
            print("  "*Depth + "l" +self.left.char + ":" + self.left.morseData)
            
            self.left._printTree(Depth)
        
        #Visit right
        if self.right:
            print("  "*Depth + "r" +self.right.char + ":" + self.right.morseData)
            #print(self.right.char + str(Depth))
            self.right._printTree(Depth)

    #Basic in order traversal to find a specific character
    def searchChar(self,val):
        char = "Null"
        result = []

        if self.left:
            result += self.left.searchChar(val)
        
        if self.char == val:
            result.append(self.morseData)

        if self.right:
            result += self.right.searchChar(val)

        return result

    def searchMorse(self, morseString):
        #Split the entire string (which can be multiple phrases) into one phrase
        morsePhraseArray = morseString.split(" /")
        #print("morsePhrase: " + str(morsePhraseArray))
        charArray = []
        decodedString = ""
        decodedWord = ""
        #Loop for every Word in the phrase
        for morseWord in range(0, len(morsePhraseArray)):
            #Split the word into letters
            morseWordArray = morsePhraseArray[morseWord].split(" ")
           # print("morseWordArray: " + str(morseWordArray))

            #Loop for every encoded letter
            
            for morseLetter in range(0, len(morseWordArray)):
                #Create a list of each coded component
                morseLetterArray = list(morseWordArray[morseLetter])

                #print("morse word: " + str(morseLetterArray))
                #Create an array of translated letters
                charArray += self._searchMorse(morseLetterArray, "")
                #print("morseChar: " + str(charArray))
            charArray.append(" ")
                
            #create a word out of the letters
        for char in range(0, len(charArray)):
            decodedWord += charArray[char]
            #print("Decoded word: " + str(decodedWord))

            
        decodedString += " " + decodedWord
        

        print(decodedString)

        
        return decodedString
            
    def _searchMorse(self, morseWord, currentChar):
        
        if (len(morseWord) != 0):
            morseLetter = morseWord.pop(0)
        else:
            morseLetter = ""
        
        #print("morseWord: " + str(morseWord))

        if(morseLetter == "."):
            currentChar = self.char
            #print("current char: " + currentChar)
            currentChar = self.left._searchMorse(morseWord, currentChar)
            
        elif morseLetter == "-":
            currentChar = self.char
            currentChar = self.right._searchMorse(morseWord, currentChar)
        else:
            if (self.char != "ROOT"):
                currentChar = self.char
                #print("Else Char: " + currentChar)

        return currentChar
            
#File Methods
#Creates a tree from the objects of the BinaryNode class
def buildTree(morse):
    rootNode = BinaryNode('ROOT','ROOT')

    for i in range(0, len(morse)):
        elements = morse[i].split(';') 
        rootNode.addChild(elements[1],elements[0])

    return rootNode

#Creates the Binary Tree
def initialiseTree():
    morse = ['a;.-','b;-...', 'c;-.-.', 'd;-..','e;.','f;..-.','g;--.','h;....','i;..','j;.---','k;-.-','l;.-..','m;--','n;-.','o;---','p;.--.','q;--.-','r;.-.','s;...','t;-','u;..-','v;...-','w;.--','x;-..-','y;-.--','z;--..']
    morseTree = buildTree(morse)
    return morseTree

#Creates a string from an array of morse encoded letters
def encode(normMessage):
    #Creates the tree
    #morse_tree = initialiseTree()

    morseArray = []
    normMessage = normMessage.lower()
    #For each letter Add a morse code to an array 
    for letter in range(0,len(normMessage)):
        #Add '/' for each space
        if (normMessage[letter] == " "):
            morseArray.append("/")
            
        else:
            morse = _encode(normMessage[letter]) #morse_tree
            morseArray.append(morse)

    morseString = ""
    for element in range(0, len(morseArray)):
        morseString += morseArray[element]
        morseString += " "

    morseString = morseString.strip()
    return morseString

#Uses the recursive method _searchChar() to recieve an array of morse encoded letters
def _encode(char): #morse_tree
    
    # Take a letter and find that letter in the binary tree
    # Send the morse of that letter back and repeat for the other letters
    morse = morseTree.searchChar(char)
    morse = morse[0]
    return morse

def decode(morseMessage):
    # Take a morse string and find the corresponding letter
    # Send the full translated string back
    normMessage = morseTree.searchMorse(morseMessage)
    normMessage = normMessage.strip()
    return normMessage


# array used to insert all morse characters into binary tree
# ';' seperates the character from the morse code
def print_tree():

    morseTree.printTree()

morseTree = initialiseTree()

if __name__ == "__main__":
    print_tree()
   # print(encode("us"))
    print(decode("..- ..."))
