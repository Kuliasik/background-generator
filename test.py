import unittest
import PIL
import main

class TestGame(unittest.TestCase):
    def test_input(self):
        answer=5
        guess=5
        result= main.run_guess(guess, answer)
        self.assertTrue(result)
    def test_incorrect(self):
        answer=6
        guess=10
        result= main.run_guess(guess, answer)   
        self.assertFalse(result)
    
    def test_not_in_range(self):
        result= main.run_guess(12, 3)   
        self.assertFalse(result)
        
if __name__ == '__main__':
    unittest.main()