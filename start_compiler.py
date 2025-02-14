"""
This script reads the content of an example file and tokenizes it using the Lexer class, 
generating a list of tokens that will be printed to the console.

"""
from src.lexer import Lexer

def main():
    with open('examples/example_1.txt', 'r') as file:
        text = file.read()

    lexer = Lexer(text)
    tokens = lexer.tokenize()

    for token in tokens:
        print(token)

if __name__ == "__main__":
    main()