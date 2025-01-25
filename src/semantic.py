class SemanticAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def analyze(self):
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
            self.error('Unexpected token or syntax error')

    def calculate_instruction(self):
        self.match('CALCULATE')
        if self.tokens[self.pos][0] == 'INTEREST':
            self.calculate_interest()
        elif self.tokens[self.pos][0] == 'MATURITY':
            self.calculate_maturity()
        else:
            self.error('Expected INTEREST or MATURITY after CALCULATE')

    def calculate_maturity(self):
        self.match('MATURITY')
        self.match('DATE')
        self.match('DATE_VALUE')
        self.match('PERIOD')
        self.match('NUMBER')
        self.match('DAYS')
        
    def calculate_interest(self):
        self.match('INTEREST')
        self.amount()
        self.rate()
        self.time()

    def amount(self):
        self.match('AMOUNT')
        if self.pos < len(self.tokens):
            number_value = float(self.consume('NUMBER'))
            if number_value <= 0:
                self.error("Amount must be a positive number")

    def define_rate(self):
        self.match('DEFINE')
        self.rate()

    def rate(self):
        self.match('RATE')
        if self.pos < len(self.tokens):
            number_value = float(self.consume('NUMBER'))
            if not (0 <= number_value <= 100):
                self.error("Rate must be between 0 and 100")
    
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

    def time(self):
        self.match('TIME')
        if self.pos < len(self.tokens):
            years_value = float(self.consume('NUMBER'))
            if years_value <= 0:
                self.error("Time must be a positive number")
            self.match('YEARS')

    def match(self, expected_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            self.pos += 1
        else:
            self.error(f"Expected {expected_type}")

    def consume(self, expected_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            value = self.tokens[self.pos][1]
            self.pos += 1
            return value
        else:
            self.error(f"Expected {expected_type}")

    def error(self, message):
        raise SemanticError(f"Semantic error at token {self.pos}: {message}")
    

# Define una excepción personalizada
class SemanticError(Exception):
    pass