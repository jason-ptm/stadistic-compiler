class IntermediateCodeGenerator:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.intermediate_representation = []

    def generate(self):
        while self.pos < len(self.tokens):
            self.instruction()

    def instruction(self):
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
        self.match('CALCULATE')
        if self.tokens[self.pos][0] == 'INTEREST':
            self.calculate_interest()
        elif self.tokens[self.pos][0] == 'MATURITY':
            self.calculate_maturity()
        else:
            self.error("Expected INTEREST or MATURITY after CALCULATE")

    def calculate_interest(self):
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
        self.match('DEFINE')
        rate_value = self.consume_value('RATE')
        
        define_code = [f'DEFINE_RATE {rate_value}']
        self.intermediate_representation.append(define_code)

    def payment(self):
        self.match('PAYMENT')
        payment_value = self.consume('NUMBER')
        payment_code = [f'PAYMENT {payment_value}']
        self.intermediate_representation.append(payment_code)

    def balance(self):
        self.match('BALANCE')
        balance_code = ['BALANCE']
        self.intermediate_representation.append(balance_code)

    def savings(self):
        self.match('SAVINGS')
        savings_code = ['SAVINGS_OPERATION']
        self.intermediate_representation.append(savings_code)

    def investment(self):
        self.match('INVESTMENT')
        investment_code = ['INVESTMENT_OPERATION']
        self.intermediate_representation.append(investment_code)

    def annuity(self):
        self.match('ANNUITY')
        annuity_code = ['ANNUITY_OPERATION']
        self.intermediate_representation.append(annuity_code)

    def consume_value(self, expected_type):
        self.match(expected_type)
        return self.consume('NUMBER')

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
        raise RuntimeError(f"Code generation error at token {self.pos}: {message}")

    def get_intermediate_representation(self):
        return self.intermediate_representation