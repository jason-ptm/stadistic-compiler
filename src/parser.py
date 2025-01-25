from src.lexer import Lexer

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        while self.pos < len(self.tokens):
            self.instruction()

    def instruction(self):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'CALCULATE':
            self.calculate_instruction()
        elif self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'DEFINE':
            self.define_rate()
        elif self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'PAYMENT':
            self.payment()
        elif self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'BALANCE':
            self.balance()
        elif self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'SAVINGS':
            self.savings()
        elif self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'INVESTMENT':
            self.investment()
        elif self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'ANNUITY':
            self.annuity()
        else:
            self.error("Expected CALCULATE, DEFINE, PAYMENT, BALANCE, SAVINGS, INVESTMENT, or ANNUITY")

    def calculate_instruction(self):
        self.match('CALCULATE')
        if self.tokens[self.pos][0] == 'INTEREST':
            self.calculate_interest()
        elif self.tokens[self.pos][0] == 'MATURITY':
            self.calculate_maturity()
        else:
            self.error("Expected INTEREST or MATURITY after CALCULATE")

    def calculate_interest(self):
        self.match('INTEREST')
        self.amount()
        self.rate()
        self.time()

    def calculate_maturity(self):
        self.match('MATURITY')
        self.match('DATE')
        self.match('DATE_VALUE')
        self.match('PERIOD')
        self.match('NUMBER')
        self.match('DAYS')

    def define_rate(self):
        self.match('DEFINE')
        self.rate()

    def payment(self):
        self.match('PAYMENT')
        self.match('NUMBER')

    def balance(self):
        self.match('BALANCE')

    def savings(self):
        self.match('SAVINGS')

    def investment(self):
        self.match('INVESTMENT')

    def annuity(self):
        self.match('ANNUITY')

    def amount(self):
        self.match('AMOUNT')
        self.match('NUMBER')

    def rate(self):
        self.match('RATE')
        self.match('NUMBER')

    def time(self):
        self.match('TIME')
        self.match('NUMBER')
        self.match('YEARS')

    def match(self, expected_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            self.pos += 1
        else:
            self.error(f"Expected {expected_type}")

    def error(self, message):
        raise ParserError(f"Syntax error at position {self.pos}: {message}")

# Definir cualquier excepción personalizadas que se necesiten
class ParserError(Exception):
    pass