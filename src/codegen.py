"""
This module represents the behavior of an intermediate code generator.
It processes a list of tokens and translates them into an intermediate representation,
which serves as a bridge between the high-level source code and the final machine code or execution.

Authors: Jason Stevens Solarte Herrera, Andrés Felipe Vanegas Bogotá
"""

class IntermediateCodeGenerator:
    def __init__(self, tokens):
        """
        Initializes the generator with tokens and an empty intermediate representation.
        """
        self.tokens = tokens  
        self.pos = 0 
        self.intermediate_representation = [] 

    def generate(self):
        """
        Generates intermediate code by processing all tokens.
        """
        while self.pos < len(self.tokens):
            self.instruction()

    def instruction(self):
        """
        Processes the current instruction based on the token type.
        """
        if self.pos < len(self.tokens):
            if self.tokens[self.pos][0] == 'CALCULATE':
                self.calculate_instruction()
            elif self.tokens[self.pos][0] == 'DEFINE':
                self.define_rate()
            elif self.tokens[self.pos][0] == 'PAYMENT':
                self.payment()
            elif self.tokens[self.pos][0] == 'BALANCE':
                self.balance()
            elif self.tokens[self.pos][0] == 'SAVINGS':
                self.savings()
            elif self.tokens[self.pos][0] == 'INVESTMENT':
                self.investment()
            elif self.tokens[self.pos][0] == 'ANNUITY':
                self.annuity()
            else:
                self.error(f"Unexpected instruction {self.tokens[self.pos]}")

    def calculate_instruction(self):
        """
        Handles the 'CALCULATE' instruction and delegates to interest or maturity calculation.
        """
        self.match('CALCULATE')
        if self.tokens[self.pos][0] == 'INTEREST':
            self.calculate_interest()
        elif self.tokens[self.pos][0] == 'MATURITY':
            self.calculate_maturity()
        else:
            self.error("Expected INTEREST or MATURITY after CALCULATE")

    def calculate_interest(self):
        """
        Generates intermediate code for interest calculation.
        """
        self.match('INTEREST')
        amount_value = self.consume_value('AMOUNT')
        rate_value = self.consume_value('RATE')
        time_value = self.consume_value('TIME')
        self.match('YEARS')
        
        interest_code = [
            'INTEREST_CALCULATION',
            f'AMOUNT {amount_value}',
            f'RATE {rate_value}',
            f'TIME {time_value}',
            'YEARS'
        ]
        self.intermediate_representation.append(interest_code)

    def calculate_maturity(self):
        """
        Generates intermediate code for maturity calculation.
        """
        self.match('MATURITY')
        self.match('DATE')
        date_value = self.consume('DATE_VALUE')
        self.match('PERIOD')
        period_value = self.consume('NUMBER')
        self.match('DAYS')

        maturity_code = [
            f'DATE_VALUE {date_value}',
            f'PERIOD {period_value}',
            'MATURITY_CALCULATION'
        ]
        self.intermediate_representation.append(maturity_code)

    def define_rate(self):
        """
        Generates intermediate code for defining a rate.
        """
        self.match('DEFINE')
        rate_value = self.consume_value('RATE')
        define_code = [f'DEFINE_RATE {rate_value}']
        self.intermediate_representation.append(define_code)

    def payment(self):
        """
        Generates intermediate code for a payment operation.
        """
        self.match('PAYMENT')
        payment_value = self.consume('NUMBER')
        payment_code = [f'PAYMENT {payment_value}']
        self.intermediate_representation.append(payment_code)

    def balance(self):
        """
        Generates intermediate code for a balance operation.
        """
        self.match('BALANCE')
        balance_code = ['BALANCE']
        self.intermediate_representation.append(balance_code)

    def savings(self):
        """
        Generates intermediate code for a savings operation.
        """
        self.match('SAVINGS')
        savings_code = ['SAVINGS_OPERATION']
        self.intermediate_representation.append(savings_code)

    def investment(self):
        """
        Generates intermediate code for an investment operation.
        """
        self.match('INVESTMENT')
        investment_code = ['INVESTMENT_OPERATION']
        self.intermediate_representation.append(investment_code)

    def annuity(self):
        """
        Generates intermediate code for an annuity operation.
        """
        self.match('ANNUITY')
        annuity_code = ['ANNUITY_OPERATION']
        self.intermediate_representation.append(annuity_code)

    def consume_value(self, expected_type):
        """
        Matches the expected token type and consumes the associated value.
        """
        self.match(expected_type)
        return self.consume('NUMBER')

    def match(self, expected_type):
        """
        Ensures the current token matches the expected type and advances the position.
        """
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            self.pos += 1
        else:
            self.error(f"Expected {expected_type}")

    def consume(self, expected_type):
        """
        Consumes the current token if it matches the expected type and returns its value.
        """
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            value = self.tokens[self.pos][1]
            self.pos += 1
            return value
        else:
            self.error(f"Expected {expected_type}")

    def error(self, message):
        """
        Raises an error with a descriptive message and the current token position.
        """
        raise RuntimeError(f"Code generation error at token {self.pos}: {message}")

    def get_intermediate_representation(self):
        """
        Returns the generated intermediate representation.
        """
        return self.intermediate_representation