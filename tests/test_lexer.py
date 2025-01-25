import unittest
from src.lexer import Lexer

class LexerTest(unittest.TestCase):
    def test_tokenize(self):
        code = "CALCULATE INTEREST AMOUNT 1000 RATE 5 TIME 2 YEARS"
        lexer = Lexer(code)
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
        self.assertEqual(tokens, expected_tokens)

if __name__ == '__main__':
    unittest.main()