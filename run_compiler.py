from src.lexer import Lexer
from src.parser import Parser, ParserError
from src.semantic import SemanticAnalyzer, SemanticError
from src.codegen import IntermediateCodeGenerator
from src.assembler import Assembler

def run_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

        # Fase de análisis léxico
        lexer = Lexer(text)
        tokens = lexer.tokenize()

        # Fase de análisis sintáctico
        parser = Parser(tokens)
        parser.parse()

        # Fase de análisis semántico
        analyzer = SemanticAnalyzer(tokens)
        analyzer.analyze()

        # Fase de generación de código intermedio
        code_generator = IntermediateCodeGenerator(tokens)
        code_generator.generate()
        intermediate_representation = code_generator.get_intermediate_representation()

        # Fase de ensamblaje
        assembler = Assembler(intermediate_representation)
        assembler.assemble()
        assembler.execute()

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except (ParserError, SemanticError, RuntimeError) as e:
        print(f"Compilation error: {e}")

if __name__ == '__main__':
    run_from_file('examples/example_3.txt')