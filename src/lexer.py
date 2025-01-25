import re

TOKEN_PATTERNS = [
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
    ('DATE_VALUE', r'\b\d{2}/\d{2}/\d{4}\b'),  # Fecha en formato DD/MM/YYYY, esto debe ir antes de NUMBER
    ('NUMBER', r'\b\d+(\.\d+)?\b'),  # Modificado para aceptar enteros y decimales
    ('CALCULATE', r'\bCALCULATE\b'),
    ('DEFINE', r'\bDEFINE\b'),
    ('TIME', r'\bTIME\b'),
    ('YEARS', r'\bYEARS\b'),
    ('PERIOD', r'\bPERIOD\b'),
    ('DAYS', r'\bDAYS\b'),
    ('WHITESPACE', r'\s+'),
]

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.tokens = []

    def tokenize(self):
        while self.pos < len(self.text):
            match = None
            for token_type, pattern in TOKEN_PATTERNS:
                regex = re.compile(pattern, re.IGNORECASE)
                match = regex.match(self.text, self.pos)
                if match:
                    value = match.group(0)
                    if token_type != 'WHITESPACE':  # Ignore espacios en blanco
                        self.tokens.append((token_type, value))
                    self.pos = match.end()
                    break
            if not match:
                raise RuntimeError(f'Illegal character: {self.text[self.pos]}')
        return self.tokens