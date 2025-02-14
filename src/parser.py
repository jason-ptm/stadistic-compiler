"""
This module implements a syntactic analyzer (parser) that validates the structure of a sequence
of tokens according to a predefined grammar. The parser ensures that the tokens follow the
correct syntax for financial calculations, such as interest, maturity, payments, and balances.
It raises custom errors if the syntax is invalid, providing detailed feedback for debugging.

Authors: Jason Stevens Solarte Herrera, Andrés Felipe Vanegas Bogotá
"""

from src.lexer import Lexer

# GRAMMAR DEFINITION:
# <PROGRAM>      -> <INSTRUCTION>*
# <INSTRUCTION>  -> <CALCULATE> | <DEFINE_RATE> | <PAYMENT> | <BALANCE> | <SAVINGS> | <INVESTMENT> | <ANNUITY>
# <CALCULATE>    -> "CALCULATE" (<INTEREST> | <MATURITY>)
# <INTEREST>     -> "INTEREST" "AMOUNT" <NUMBER> "RATE" <NUMBER> "TIME" <NUMBER> "YEARS"
# <MATURITY>     -> "MATURITY" "DATE" "DATE_VALUE" "PERIOD" <NUMBER> "DAYS"
# <DEFINE_RATE>  -> "DEFINE" "RATE" <NUMBER>
# <PAYMENT>      -> "PAYMENT" <NUMBER>
# <BALANCE>      -> "BALANCE"
# <SAVINGS>      -> "SAVINGS"
# <INVESTMENT>   -> "INVESTMENT"
# <ANNUITY>      -> "ANNUITY"

class Parser:
    def __init__(self, tokens):
        """
        Initializes the Parser with a list of tokens and sets the current position to 0.
        Also initializes a dictionary mapping instruction types to their corresponding handler methods.
        """
        self.tokens = tokens
        self.pos = 0
        self.instruction_handlers = {
            'CALCULATE': self.calculate_instruction,
            'DEFINE': self.define_rate,
            'PAYMENT': self.payment,
            'BALANCE': self.balance,
            'SAVINGS': self.savings,
            'INVESTMENT': self.investment,
            'ANNUITY': self.annuity
        }  # Maps instruction types to their handler methods

    def parse(self):
        """
        Main parsing loop. Iterates through the tokens and processes each instruction
        until all tokens are consumed.
        """
        while self.pos < len(self.tokens):
            self.instruction()

    def instruction(self):
        """
        Determines the type of the current instruction and delegates to the appropriate handler.
        If the instruction type is invalid, raises an error.
        """
        if self.pos < len(self.tokens):
            current_token = self.tokens[self.pos][0]               
            handler = self.instruction_handlers.get(current_token)
            if handler:
                handler()  # Execute the handler for the current instruction
            else:
                self.error(f"Expected CALCULATE, DEFINE, PAYMENT, BALANCE, SAVINGS, INVESTMENT, or ANNUITY. Found: {current_token}")


    """
    The following functions validate and process tokens related to calculations.
    They ensure that the required tokens (e.g., AMOUNT, RATE, TIME) are present
    and in the correct order for the specific calculation being performed.
    """

    def calculate_instruction(self):
        # Validate the 'CALCULATE' instruction and delegate to the appropriate calculation method.
        self.match('CALCULATE')       
        if self.tokens[self.pos][0] == 'INTEREST':
            self.calculate_interest()  
        elif self.tokens[self.pos][0] == 'MATURITY':
            self.calculate_maturity()
        else:
            self.error("Expected INTEREST or MATURITY after CALCULATE")

    def calculate_interest(self):
        # Validate the 'INTEREST' calculation.
        self.match('INTEREST')
        self.amount()               
        self.rate()                 
        self.time()                 

    def calculate_maturity(self):
        # Validate the 'MATURITY' calculation.
        self.match('MATURITY')
        self.match('DATE')
        self.match('DATE_VALUE')
        self.match('PERIOD')
        self.match('NUMBER')
        self.match('DAYS')

    def define_rate(self):
        # Validate the 'DEFINE RATE' instruction.
        self.match('DEFINE')
        self.rate()

    def payment(self):
        # Validate the 'PAYMENT' instruction.
        self.match('PAYMENT')
        self.match('NUMBER')

    def balance(self):
        # Validate the 'BALANCE' instruction.
        self.match('BALANCE')

    def savings(self):
        # Validate the 'SAVINGS' instruction.
        self.match('SAVINGS')

    def investment(self):
        # Validate the 'INVESTMENT' instruction.
        self.match('INVESTMENT') 

    def annuity(self):
        # Validate the 'ANNUITY' instruction.
        self.match('ANNUITY')    

    def amount(self):
        # Validate the 'AMOUNT' token.
        self.match('AMOUNT')
        self.match('NUMBER')
    def rate(self):
        # Validate the 'RATE' token.
        self.match('RATE')
        self.match('NUMBER')

    def time(self):
        # Validate the 'TIME' token.
        self.match('TIME')  
        self.match('NUMBER')
        self.match('YEARS') 

    def match(self, expected_type):
        # Check if the current token matches the expected type and move to the next token.
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            self.pos += 1
        else:
            self.error(f"Expected {expected_type}")  # Raise an error if the token doesn't match

    def error(self, message):
        """
        Raises a ParserError with a descriptive message, including the current position and the unexpected token.
        """
        token = self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '')  # Get the current token or EOF
        raise ParserError(f"Syntax error at position {self.pos}: {message}. Found: {token}")

# Custom exception for parser errors
class ParserError(Exception):
    """
    Custom exception class for parser-related errors.
    """
    pass