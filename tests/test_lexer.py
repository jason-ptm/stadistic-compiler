# This file contains the test cases for the lexer module.

import unittest
from src.lexer import Lexer

class LexerTest(unittest.TestCase):
    """This class contains the test cases for the lexer module."""

    def test_tokenize(self):
        # Test case 1
        code = "CALCULATE INTEREST AMOUNT 1000 RATE 5 TIME 2 YEARS"
        lexer = Lexer(code)
        # List of tokens
        tokens = lexer.tokenize()
        expected_tokens = [
            ('CALCULATE', 'CALCULATE'),
            ('INTEREST', 'INTEREST'),
            ('AMOUNT', 'AMOUNT'),
            ('NUMBER', '1000'),
            ('RATE', 'RATE'),
            ('NUMBER', '5'),
            ('TIME', 'TIME'),
            ('NUMBER', '2'),
            ('YEARS', 'YEARS'),
        ]
        # Check if the tokens are correct
        self.assertEqual(tokens, expected_tokens)

if __name__ == '__main__':
    # Run the test cases defined in the module above
    unittest.main()