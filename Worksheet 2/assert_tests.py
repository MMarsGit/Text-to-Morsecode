import morse

def test_encode_us():
    assert morse.encode('us') == '..- ...', "Should be ..- ..."

if __name__ == "__main__":
    test_encode_us()
    print("All Tests Passed!")