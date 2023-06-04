import unittest

def is_palindrome( word : str):
    try:
        assert isinstance(word, str)
        word = word.lower()
        word = word.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        
        if word == word[::-1]:
            return True
        return False
    
    except AssertionError:
        return 'Must provide a string.'


class TestIsPalindrome(unittest.TestCase):
    
    def test_not_palindrome_word(self):
        self.assertEqual(is_palindrome('home'), False)
        self.assertEqual(is_palindrome('casa'), False)
        self.assertEqual(is_palindrome('avión'), False)
    
    def test_palindrome_word(self):
        self.assertEqual(is_palindrome('ana'), True)
        self.assertEqual(is_palindrome('ama'), True)   
        
    def test_palindrome_word_with_uppercase(self):
        self.assertEqual(is_palindrome('Narran'), True)
        self.assertEqual(is_palindrome('Ala'), True)

    def test_palindrome_word_with_accent_mark(self):
        self.assertEqual(is_palindrome('aérea'), True)
        self.assertEqual(is_palindrome('Alá'), True)
        
        
    def test_list(self):
        self.assertEqual(is_palindrome([1,1,1]), 'Must provide a string.')


if __name__ == '__main__':
    unittest.main()
# Run like: python3 -m unittest