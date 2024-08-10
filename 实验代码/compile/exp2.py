import ast
import autopep8
import textwrap

# yacc

class SyntaxAnalyzer:
    def __init__(self, code):
        self.code = textwrap.dedent(code).strip()
        self.tree = ast.parse(self.code)

    def get_function_signatures(self):
        functions = [node for node in ast.walk(self.tree) if isinstance(node, ast.FunctionDef)]
        signatures = []
        for func in functions:
            params = [arg.arg for arg in func.args.args]
            signatures.append(f"Function '{func.name}({', '.join(params)})'")
        return signatures

    def format_code(self):
        formatted_code = autopep8.fix_code(self.code)
        return formatted_code

# 示例用法
code = """
def my_function(a, b):
    return a + b
"""

analyzer = SyntaxAnalyzer(code)
signatures = analyzer.get_function_signatures()
formatted_code = analyzer.format_code()
print("Function Signatures:", signatures)
print("Formatted Code:\n", formatted_code)
