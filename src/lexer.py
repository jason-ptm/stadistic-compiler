""" 
This module implements a lexical analyzer (lexer) that processes input text and breaks it down
into meaningful tokens. The lexer uses regular expressions to identify keywords, numbers, dates,
and other patterns, while ignoring whitespace and comments. It is a crucial component in the
compilation process, providing the foundation for syntactic and semantic analysis.

Authors: Jason Stevens Solarte Herrera, Andrés Felipe Vanegas Bogotá
"""

import re

TOKEN_PATTERNS = [
    #Matches the keyword 'define'
    ('INTEREST', r'\binterest\b'),
    ('RATE', r'\brate\b'),
    ('AMOUNT', r'\bamount\b'),
    ('DATE', r'\bdate\b'),
    ('MATURITY', r'\bmaturity\b'),
    ('SAVINGS', r'\bsavings\b'),
    ('INVESTMENT', r'\binvestment\b'),
    ('PAYMENT', r'\bpayment\b'),
    ('ANNUITY', r'\bannuity\b'),
    ('BALANCE', r'\bbalance\b'),
    ('DATE_VALUE', r'\b\d{2}/\d{2}/\d{4}\b'),   # Matches dates in DD/MM/YYYY format
    ('NUMBER', r'\b\d+(\.\d+)?\b'),             # Matches integers and decimal numbers
    ('CALCULATE', r'\bCALCULATE\b'),  
    ('DEFINE', r'\bDEFINE\b'),
    ('TIME', r'\bTIME\b'),
    ('YEARS', r'\bYEARS\b'),
    ('PERIOD', r'\bPERIOD\b'),
    ('DAYS', r'\bDAYS\b'),
    ('WHITESPACE', r'\s+'),                  # Matches whitespace (spaces, tabs, newlines)
    ('SINGLE_LINE_COMMENT', r'#.*'),         # Matches single-line comments starting with #
    ('MULTI_LINE_COMMENT', r'/\*.*?\*/'),    # Matches multi-line comments between /* and */
]

class Lexer:
    def __init__(self, text):
        """
        Initializes the Lexer with the input text.
        - text: The input string to tokenize.
        - pos: The current position in the input text.
        - tokens: The list of tokens generated by the lexer.
        """
        self.text = text
        self.pos = 0 
        self.tokens = []

    def tokenize(self):
        """
        Tokenizes the input text by matching patterns defined in TOKEN_PATTERNS.
        Returns a list of tokens, ignoring whitespace and comments.
        Raises a RuntimeError if an illegal character is encountered.
        """
        while self.pos < len(self.text):
            match = None
            for token_type, pattern in TOKEN_PATTERNS:
                # Compile the regex pattern with appropriate flags:
                # - re.IGNORECASE: Case-insensitive matching for keywords.
                # - re.DOTALL: Allows '.' to match newlines (used for multi-line comments).
                flags = re.IGNORECASE
                if token_type == 'MULTI_LINE_COMMENT':
                    flags |= re.DOTALL
                regex = re.compile(pattern, flags)
                match = regex.match(self.text, self.pos)
                if match:
                    value = match.group(0)
                    # Ignore whitespace and comments (they are not added to the tokens list)
                    if token_type not in ['WHITESPACE', 'SINGLE_LINE_COMMENT', 'MULTI_LINE_COMMENT']:
                        self.tokens.append((token_type, value))  
                    self.pos = match.end()  
                    break
            # If no pattern matches, raise an error for illegal characters
            if not match:
                raise RuntimeError(f'Illegal character: {self.text[self.pos]}')
        return self.tokens