import unittest
import morse

class TestMorse(unittest.TestCase):
    #encode tests
    def test_encode_us(self):
        self.assertEqual(morse.encode('us'), '..- ...')

    def test_encode_lowestVals(self):
        self.assertEqual(morse.encode('xyz'), '-..- -.-- --..')

    def test_encode_spaces(self):
        self.assertEqual(morse.encode('hello space'), '.... . .-.. --- / ... .--. .- -.-. .')
    
    def test_encode_upper(self):
        self.assertEqual(morse.encode('HELLO'), '.... . .-.. .-.. ---' )

    def test_encode_extraSpace(self):
        self.assertEqual(morse.encode(' hello  '), '.... . .-.. .-.. ---')
    #decode tests
    def test_decode_us(self):
        self.assertEqual(morse.decode('..- ...'), 'us')

    def test_decode_lowestVals(self):
        self.assertEqual(morse.decode('-..- -.-- --..', 'xyz'))

    def test_decode_spaces(self):
        self.assertEqual(morse.decode('.... . .-.. .-.. --- / .-- --- .-. .-.. -..'), 'hello world')

    def test_decode_rightTreeFirst(self):
        self.assertEqual(morse.decode('- --- -..'), 'tod')

    def test_decode_middleChars(self):
        self.assertEqual(morse.decode('.- -.- ..-'), 'aku')

    #Tree tests
    #def test_tree_insert(self):
        #morseTree.addChild()

if __name__ == '__main__':
    morse.print_tree()
    unittest.main()