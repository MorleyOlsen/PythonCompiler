import re

# lex

class Lexer:
    def __init__(self):
        self.keywords = ['if', 'else', 'for', 'while', 'return', 'def']
        self.datatypes = ['int', 'float', 'str', 'bool']
        self.operators = ['+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>=']
        self.brackets = ['(', ')', '[', ']', '{', '}']
        self.highlights = {
            'keyword': '\033[95m',
            'datatype': '\033[94m',
            'operator': '\033[93m',
            'bracket': '\033[92m',
            'end': '\033[0m'
        }

    def highlight(self, code):
        tokens = re.split(r'(\W)', code)
        highlighted_code = ''
        for token in tokens:
            if token in self.keywords:
                highlighted_code += self.highlights['keyword'] + token + self.highlights['end']
            elif token in self.datatypes:
                highlighted_code += self.highlights['datatype'] + token + self.highlights['end']
            elif token in self.operators:
                highlighted_code += self.highlights['operator'] + token + self.highlights['end']
            elif token in self.brackets:
                highlighted_code += self.highlights['bracket'] + token + self.highlights['end']
            else:
                highlighted_code += token
        return highlighted_code

# 示例用法
lexer = Lexer()
code = "def func(x): if x > 0: return int(x)"
highlighted_code = lexer.highlight(code)
print(highlighted_code)
