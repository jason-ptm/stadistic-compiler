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