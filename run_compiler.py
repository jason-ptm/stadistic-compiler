"""
Basic compiler that processes a source code file.

This script performs the following compilation phases:
    1. Lexical analysis: Divides the code into tokens.
    2. Syntactic analysis: Verifies the structure of the code.
    3. Semantic analysis: Verifies the meaning of the code.
    4. Intermediate code generation: Creates an intermediate representation of the code.
    5. Assembly: Converts the intermediate representation into executable code and runs it.

Handles common errors such as file not found, syntax errors, semantic errors, and runtime errors.
"""

from src.lexer import Lexer
from src.parser import Parser, ParserError
from src.semantic import SemanticAnalyzer, SemanticError
from src.codegen import IntermediateCodeGenerator
from src.assembler import Assembler

def run_from_file(file_path):
    """
    Processes a source code file and executes all compilation phases.compilación.

    Raises:
        FileNotFoundError: If the file is not found.
        ParserError: If there is a syntax error.
        SemanticError: If there is a semantic error.
        RuntimeError: If there is a runtime error.
    """
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            text = file.read()

        # Lexical analysis
        lexer = Lexer(text)
        tokens = lexer.tokenize()

        # Syntactic analysis
        parser = Parser(tokens)
        parser.parse()

        # Semantic analysis
        analyzer = SemanticAnalyzer(tokens)
        analyzer.analyze()

        # Intermediate code generation
        code_generator = IntermediateCodeGenerator(tokens)
        code_generator.generate()
        intermediate_representation = code_generator.get_intermediate_representation()

        # Assembly
        assembler = Assembler(intermediate_representation)
        assembler.assemble()
        assembler.execute()

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except (ParserError, SemanticError, RuntimeError) as e:
        print(f"Compilation error: {e}")

if __name__ == '__main__':
    # Execute the compiler with the example file
    run_from_file('examples/example_10.txt')