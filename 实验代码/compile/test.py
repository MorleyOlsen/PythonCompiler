import re
import ast
import autopep8
import textwrap
import numpy as np
import math
import sys
import inspect
import threading
import time
from datetime import datetime, timedelta
from test2 import Lexer, SyntaxAnalyzer, IOExtension, DataStructureExtension, ErrorHandling, AdvancedFeatures, FunctionSignature, CodeFormatter, FileOperations, MathOperations, DateTimeOperations, Encryption, Logging

# 模块一：词法分析器
class Lexer:
    def __init__(self):
        self.keywords = [
            'if', 'else', 
            'for', 'while', 
            'return', 'def', 'class', 
            'import', 'from', 'as', 
            'try', 'except', 
            'finally'
        ]
        self.datatypes = [
            'int', 'float', 'str', 'bool', 
            'list', 'dict', 'tuple', 'set', 
            'None'
        ]
        self.operators = [
            '+', '-', '*', '/', 
            '=', '==', '!=', '<', '>', '<=', '>=', 
            '+=', '-=', '*=', '/=', 
            'and', 'or', 'not'
        ]
        self.brackets = [
            '(', ')', 
            '[', ']', 
            '{', '}'
        ]
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

# 模块二：语法分析器
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

    def get_ast(self):
        return ast.dump(self.tree, indent=4)

# 模块三：I/O 扩展模块
class IOExtension:
    @staticmethod
    def formatted_input(prompt, dtype=str):
        value = input(prompt)
        try:
            return dtype(value)
        except ValueError:
            print(f"Invalid {dtype.__name__}, try again.")
            return IOExtension.formatted_input(prompt, dtype)

    @staticmethod
    def formatted_output(data):
        if isinstance(data, float):
            print(f"Formatted Output: {data:.2f}")
        elif isinstance(data, list):
            print("List Output: ", data)
        elif isinstance(data, dict):
            print("Dict Output: ", data)
        else:
            print(f"Output: {data}")

# 模块四：数据结构扩展模块
class DataStructureExtension:
    def __init__(self):
        self.int_array = []
        self.float_array = []
        self.str_list = []
        self.dict_structure = {}

    def add_int(self, value):
        if isinstance(value, int):
            self.int_array.append(value)
        else:
            raise TypeError("Only integers are allowed in int_array")

    def add_float(self, value):
        if isinstance(value, float):
            self.float_array.append(value)
        else:
            raise TypeError("Only floats are allowed in float_array")

    def add_str(self, value):
        if isinstance(value, str):
            self.str_list.append(value)
        else:
            raise TypeError("Only strings are allowed in str_list")

    def add_dict(self, key, value):
        self.dict_structure[key] = value

    def get_int_array(self):
        return self.int_array

    def get_float_array(self):
        return self.float_array

    def get_str_list(self):
        return self.str_list

    def get_dict(self):
        return self.dict_structure

# 模块五：错误处理模块
class ErrorHandling:
    @staticmethod
    def handle_error(err_type, message):
        print(f"{err_type}: {message}")

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            self.handle_error("ZeroDivisionError", "Cannot divide by zero")
        except TypeError:
            self.handle_error("TypeError", "Unsupported operand type(s)")
        except Exception as e:
            self.handle_error(type(e).__name__, str(e))

    def index_error(self, lst, index):
        try:
            return lst[index]
        except IndexError:
            self.handle_error("IndexError", "List index out of range")
        except Exception as e:
            self.handle_error(type(e).__name__, str(e))

    def key_error(self, dct, key):
        try:
            return dct[key]
        except KeyError:
            self.handle_error("KeyError", "Key not found in dictionary")
        except Exception as e:
            self.handle_error(type(e).__name__, str(e))

    def type_error(self, operation):
        try:
            eval(operation)
        except TypeError:
            self.handle_error("TypeError", "Unsupported operand type(s)")
        except Exception as e:
            self.handle_error(type(e).__name__, str(e))

# 模块六：高级功能扩展模块
class AdvancedFeatures:
    def __init__(self, array):
        self.array = np.array(array)

    def array_operations(self, other_array, operation):
        other_array = np.array(other_array)
        if operation == 'add':
            return self.array + other_array
        elif operation == 'subtract':
            return self.array - other_array
        elif operation == 'multiply':
            return self.array * other_array
        elif operation == 'divide':
            return self.array / other_array
        else:
            raise ValueError("Invalid operation")

    def statistics(self):
        return {
            'mean': np.mean(self.array),
            'max': np.max(self.array),
            'min': np.min(self.array),
            'sum': np.sum(self.array),
            'std': np.std(self.array),
            'var': np.var(self.array)
        }

    def power(self, exponent):
        return np.power(self.array, exponent)

# 模块七：提示函数参数
class FunctionSignature:
    @staticmethod
    def get_signature(func):
        signature = inspect.signature(func)
        return f"{func.__name__}{signature}"

# 模块八：代码格式化
class CodeFormatter:
    @staticmethod
    def format_code(code):
        return autopep8.fix_code(code)

# 模块九：文件操作模块
class FileOperations:
    @staticmethod
    def read_file(filename):
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error reading file '{filename}': {e}")

    @staticmethod
    def write_file(filename, content):
        try:
            with open(filename, 'w') as file:
                file.write(content)
            print(f"Content written to '{filename}' successfully.")
        except Exception as e:
            print(f"Error writing to file '{filename}': {e}")

# 模块十：数学计算模块
class MathOperations:
    @staticmethod
    def factorial(n):
        if n < 0:
            print("Factorial is not defined for negative numbers.")
            return None
        elif n == 0:
            return 1
        else:
            return n * MathOperations.factorial(n - 1)

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    @staticmethod
    def lcm(a, b):
        return abs(a * b) // MathOperations.gcd(a, b)

    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

# 模块十一：数列计算模块
class SequenceCalculator:
    @staticmethod
    def fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            fib_sequence = [0, 1]
            a, b = 0, 1
            for _ in range(2, n):
                a, b = b, a + b
                fib_sequence.append(b)
            return fib_sequence

    @staticmethod
    def arithmetic_series(a, d, n):
        return [a + i * d for i in range(n)]

# 模块十二：日期和时间操作模块
class DateTimeOperations:
    @staticmethod
    def current_datetime():
        return datetime.now()

    @staticmethod
    def format_datetime(dt, format="%Y-%m-%d %H:%M:%S"):
        return dt.strftime(format)

    @staticmethod
    def add_days_to_date(dt, days):
        return dt + timedelta(days=days)

# 主程序
def main():
    def print_current_time():
        while True:
            now = DateTimeOperations.current_datetime()
            formatted_time = DateTimeOperations.format_datetime(now, "%Y-%m-%d %H:%M:%S")
            print(f"\r当前时间: {formatted_time}", end='', flush=True)
            time.sleep(1)

    time_thread = threading.Thread(target=print_current_time)
    time_thread.daemon = True  # 将线程设置为守护线程，使得主程序退出时线程也会退出
    time_thread.start()
    while True:
        print("\n选择功能：")
        print("1. 代码高亮")
        print("2. 语法分析和代码格式化")
        print("3. 格式化输入和输出")
        print("4. 数据结构扩展")
        print("5. 错误处理")
        print("6. 高级功能扩展")

        # 主程序（续）
        print("7. 提示函数参数")
        print("8. 代码格式化")
        print("9. 文件操作")
        print("10. 数学计算")
        print("11. 数列计算")
        print("0. 退出")
        choice = input("请输入选择的功能编号: ")

        if choice == '0':
            break
        elif choice == '1':
             code = input("请输入代码进行高亮显示: ")
             lexer = Lexer()
             highlighted_code = lexer.highlight(code)
             print(highlighted_code)
        elif choice == '2':
                code = input("请输入代码进行语法分析和格式化: ")
                analyzer = SyntaxAnalyzer(code)
                signatures = analyzer.get_function_signatures()
                formatted_code = analyzer.format_code()
                print("Function Signatures:", signatures)
                print("Formatted Code:\n", formatted_code)
                print("Abstract Syntax Tree (AST):\n", analyzer.get_ast())
        elif choice == '3':
            prompt = input("请输入提示信息: ")
            dtype = input("请输入数据类型（int, float, str, list, dict）: ")
            if dtype == 'int':
                value = IOExtension.formatted_input(prompt, int)
            elif dtype == 'float':
                value = IOExtension.formatted_input(prompt, float)
            elif dtype == 'list':
                value = IOExtension.formatted_input(prompt, eval)
            elif dtype == 'dict':
                value = IOExtension.formatted_input(prompt, eval)
            else:
                value = IOExtension.formatted_input(prompt, str)
            IOExtension.formatted_output(value)
        elif choice == '4':
            ds = DataStructureExtension()
            while True:
                sub_choice = input("请输入数据类型和值（如：int 5, float 3.14, str 'hello', dict key:value）或输入exit退出: ")
                if sub_choice == 'exit':
                    break
                dtype, value = sub_choice.split(maxsplit=1)
                if dtype == 'int':
                    ds.add_int(int(value))
                elif dtype == 'float':
                    ds.add_float(float(value))
                elif dtype == 'str':
                    ds.add_str(value.strip("'"))
                elif dtype == 'dict':
                    key, val = value.split(':')
                    ds.add_dict(key.strip(), val.strip())
                elif dtype == 'list':
                    items = eval(value)
                    for item in items:
                        if isinstance(item, int):
                            ds.add_int(item)
                        elif isinstance(item, float):
                            ds.add_float(item)
                        elif isinstance(item, str):
                            ds.add_str(item)
                        elif isinstance(item, dict):
                            for k, v in item.items():
                                ds.add_dict(k, v)
                        else:
                            print(f"Unsupported type in list: {type(item)}")
                print("Int Array:", ds.get_int_array())
                print("Float Array:", ds.get_float_array())
                print("Str List:", ds.get_str_list())
                print("Dict Structure:", ds.get_dict())
        elif choice == '5':
            eh = ErrorHandling()
            sub_choice = input("请输入要测试的错误类型（divide, index, key, type）: ")
            if sub_choice == 'divide':
                a = input("请输入被除数: ")
                b = input("请输入除数: ")
                result = eh.divide(float(a), float(b))
                if result is not None:
                    print("Division Result:", result)
            elif sub_choice == 'index':
                lst = input("请输入列表元素（用逗号分隔）: ").split(',')
                lst = list(map(str.strip, lst))
                index = input("请输入索引: ")
                result = eh.index_error(lst, int(index))
                if result is not None:
                    print("Element at index:", result)
            elif sub_choice == 'key':
                dct = eval(input("请输入字典（如 {'a': 1, 'b': 2}）: "))
                key = input("请输入键: ")
                result = eh.key_error(dct, key)
                if result is not None:
                    print("Value for key:", result)
            elif sub_choice == 'type':
                operation = input("请输入操作（如 '1 + 'hello''）：")
                eh.type_error(operation)
        elif choice == '6':
            array = input("请输入数组元素（用逗号分隔）: ").split(',')
            array = list(map(float, array))
            af = AdvancedFeatures(array)
            operation = input("请输入操作（add, subtract, multiply, divide, power, statistics）: ")
            if operation == 'statistics':
                print("Statistics:", af.statistics())
            elif operation == 'power':
                exponent = float(input("请输入幂: "))
                result = af.power(exponent)
                print("Power Result:", result)
            else:
                other_array = input("请输入另一个数组元素（用逗号分隔）: ").split(',')
                other_array = list(map(float, other_array))
                result = af.array_operations(other_array, operation)
                print("Array Operations Result:", result)
        elif choice == '7':
            func_name = input("请输入函数名：")
            try:
                func = eval(func_name)
                signature = FunctionSignature.get_signature(func)
                print(f"Function Signature: {signature}")
            except NameError:
                print("函数不存在，请输入正确的函数名。")
        elif choice == '8':
                code = input("请输入代码进行格式化: ")
                formatted_code = CodeFormatter.format_code(code)
                print("Formatted Code:\n", formatted_code)
        elif choice == '9':
            file_name = input("请输入文件名：")
            content = FileOperations.read_file(file_name)
            if content:
                print(f"文件内容：\n{content}")
                write_choice = input("是否写入新内容？（yes/no）")
                if write_choice.lower() == 'yes':
                    new_content = input("请输入新内容：")
                    FileOperations.write_file(file_name, new_content)
            else:
                print(f"文件 '{file_name}' 不存在或读取失败。")
        elif choice == '10':
            sub_choice = input("请输入要执行的数学操作（factorial, gcd, lcm, prime）: ")
            if sub_choice == 'factorial':
                n = int(input("请输入一个整数："))
                result = MathOperations.factorial(n)
                if result is not None:
                    print(f"Factorial of {n}: {result}")
            elif sub_choice in ['gcd', 'lcm']:
                a = int(input("请输入第一个整数："))
                b = int(input("请输入第二个整数："))
                if sub_choice == 'gcd':
                    result = MathOperations.gcd(a, b)
                    print(f"GCD of {a} and {b}: {result}")
                else:
                    result = MathOperations.lcm(a, b)
                    print(f"LCM of {a} and {b}: {result}")
            elif sub_choice == 'prime':
                n = int(input("请输入一个整数："))
                if MathOperations.is_prime(n):
                    print(f"{n} 是素数")
                else:
                    print(f"{n} 不是素数")
            else:
              print("无效的选择，请重新输入。")
        elif choice == '11':
            sub_choice = input("请选择要计算的数列（fibonacci, arithmetic）: ")
            if sub_choice == 'fibonacci':
                n = int(input("请输入要生成的斐波那契数列长度: "))
                result = SequenceCalculator.fibonacci(n)
                print(f"Fibonacci Sequence of length {n}: {result}")
            elif sub_choice == 'arithmetic':
                a = float(input("请输入等差数列的首项 a: "))
                d = float(input("请输入等差数列的公差 d: "))
                n = int(input("请输入等差数列的项数 n: "))
                result = SequenceCalculator.arithmetic_series(a, d, n)
                print(f"Arithmetic Series: {result}")
            else:
                print("无效的选择，请重新输入。")
        else:
            print("无效的选择，请重新输入。")

if __name__ == "__main__":
    main()





