import re
import ast
import autopep8
import textwrap
import numpy as np
import math
import sys
import inspect
from datetime import datetime, timedelta

# 模块一：词法分析器
class Lexer:
    # 初始化
    def __init__(self):
        # 关键字
        self.keywords = [
            # 条件判断
            'if', 'else',
            # 循环
            'for', 'while', 
            # 函数和类
            'return', 'def', 'class', 
            # 引入依赖
            'import', 'from', 'as', 
            # 其他关键字
            'try', 'except', 'finally'
        ]
        
        # 数据类型
        self.datatypes = [
            # 单变量
            'int', 'float', 'str', 'bool', 
            # 多变量集合
            'list', 'dict', 'tuple', 'set', 
            # 空
            'None'
        ]
        
        # 操作符号
        self.operators = [
            # 四则运算
            '+', '-', '*', '/', '=', 
            # 大小判断
            '==', '!=', '<', '>', '<=', '>=', 
            # 四则运算简写
            '+=', '-=', '*=', '/=', 
            # 与或非
            'and', 'or', 'not'
        ]
        
        # 括号
        self.brackets = [
            # 小括号
            '(', ')', 
            # 中括号
            '[', ']', 
            # 大括号
            '{', '}'
        ]
        
        # 高亮设置
        self.highlights = {
            # 关键字高亮
            'keyword': '\033[95m',
            # 数据类型高亮
            'datatype': '\033[94m',
            # 操作符号高亮
            'operator': '\033[93m',
            # 括号高亮
            'bracket': '\033[92m',
            # 结束高亮
            'end': '\033[0m'
        }

    # 高亮设置
    def highlight(self, code):
        # 获取记号流序列
        tokens = re.split(r'(\W)', code)
        
        # 高亮字符串初始化
        highlighted_code = ''
        
        # 遍历记号流
        for token in tokens:
            # 关键字定位
            if token in self.keywords:
                highlighted_code += self.highlights['keyword'] + token + self.highlights['end']
            # 数据类型定位
            elif token in self.datatypes:
                highlighted_code += self.highlights['datatype'] + token + self.highlights['end']
            # 操作符号定位
            elif token in self.operators:
                highlighted_code += self.highlights['operator'] + token + self.highlights['end']
            # 括号定位
            elif token in self.brackets:
                highlighted_code += self.highlights['bracket'] + token + self.highlights['end']
            # 其他非必要高亮的字符
            else:
                highlighted_code += token
        
        return highlighted_code

# 模块二：语法分析器
class SyntaxAnalyzer:
    # 初始化，接收记号流code
    def __init__(self, code):
        # 去除代码的公共前导空格并去除首尾空格
        self.code = textwrap.dedent(code).strip()
        # 解析代码生成抽象语法树
        self.tree = ast.parse(self.code)

    # 获取函数签名
    def get_function_signatures(self):
        # 遍历语法树中的所有节点，筛选出函数定义节点
        functions = [node for node in ast.walk(self.tree) if isinstance(node, ast.FunctionDef)]
        
        # 初始化函数签名
        signatures = []
        
        # 提取每个函数的名称和参数列表，形成函数签名字符串
        for func in functions:
            params = [arg.arg for arg in func.args.args]
            signatures.append(f"Function '{func.name}({', '.join(params)})'")
        
        # 返回函数签名
        return signatures

    # 格式化代码
    def format_code(self):
        # autopep8 格式化代码
        formatted_code = autopep8.fix_code(self.code)
        return formatted_code

    # 获取抽象语法树
    def get_ast(self):
        # 以缩进格式返回抽象语法树的字符串表示
        return ast.dump(self.tree, indent=4)

# 模块三：I/O 扩展模块
class IOExtension:
    # 静态方法下的格式化输入
    @staticmethod
    def formatted_input(prompt, dtype=str):
        # 显示提示信息，并获取用户输入
        value = input(prompt)
        # 尝试将输入转换为指定的数据类型
        try:
            return dtype(value)
        # 转换失败
        except ValueError:
            # 提示用户
            print(f"Invalid {dtype.__name__}, try again.")
            # 递归调用自身重新获取输入
            return IOExtension.formatted_input(prompt, dtype)

    # 静态方法下的格式化输出
    @staticmethod
    def formatted_output(data):
        # 数据是浮点数，按两位小数格式输出
        if isinstance(data, float):
            print(f"Formatted Output: {data:.2f}")
        # 数据是列表，按列表格式输出
        elif isinstance(data, list):
            print("List Output: ", data)
        # 数据是字典，按字典格式输出
        elif isinstance(data, dict):
            print("Dict Output: ", data)
        # 其他类型的数据，按默认格式输出
        else:
            print(f"Output: {data}")

# 模块四：数据结构扩展模块
class DataStructureExtension:
    # 初始化
    def __init__(self):
        # 整数数组
        self.int_array = []
        # 浮点数数组
        self.float_array = []
        # 字符串列表
        self.str_list = []
        # 字典
        self.dict_structure = {}

    # 添加整数
    def add_int(self, value):
        # 检查是否为整数类型
        if isinstance(value, int):
            self.int_array.append(value)
        else:
            raise TypeError("Only integers are allowed in int_array")

    # 添加浮点数
    def add_float(self, value):
        # 检查是否为浮点数类型
        if isinstance(value, float):
            self.float_array.append(value)
        else:
            raise TypeError("Only floats are allowed in float_array")

    # 添加字符串
    def add_str(self, value):
        # 检查是否为字符串类型
        if isinstance(value, str):
            self.str_list.append(value)
        else:
            raise TypeError("Only strings are allowed in str_list")

    # 添加键值对到字典
    def add_dict(self, key, value):
        self.dict_structure[key] = value

    # 获取整数数组
    def get_int_array(self):
        return self.int_array

    # 获取浮点数数组
    def get_float_array(self):
        return self.float_array

    # 获取字符串列表
    def get_str_list(self):
        return self.str_list

    # 获取字典结构
    def get_dict(self):
        return self.dict_structure

# 模块五：错误处理模块
class ErrorHandling:
    # 静态方法下的处理错误并打印错误信息
    @staticmethod
    def handle_error(err_type, message):
        print(f"{err_type}: {message}")

    # 除法，带有错误处理
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            self.handle_error("ZeroDivisionError", "Cannot divide by zero")
        except TypeError:
            self.handle_error("TypeError", "Unsupported operand type(s)")
        except Exception as e:
            self.handle_error(type(e).__name__, str(e))

    # 索引错误处理
    def index_error(self, lst, index):
        # 尝试获取列表中的元素
        try:
            return lst[index]
        # 处理索引超出范围错误
        except IndexError:
            self.handle_error("IndexError", "List index out of range")
        # 处理其他异常
        except Exception as e:
            self.handle_error(type(e).__name__, str(e))

    # 键错误处理
    def key_error(self, dct, key):
        # 尝试获取字典中的值
        try:
            return dct[key]
        # 处理键不存在错误
        except KeyError:
            self.handle_error("KeyError", "Key not found in dictionary")
        # 处理其他异常
        except Exception as e:
            self.handle_error(type(e).__name__, str(e))

    # 类型错误处理
    def type_error(self, operation):
        # 尝试执行操作
        try:
            eval(operation)
        # 处理类型错误
        except TypeError:
            self.handle_error("TypeError", "Unsupported operand type(s)")
        # 处理其他异常
        except Exception as e:
            self.handle_error(type(e).__name__, str(e))

# 模块六：高级功能扩展模块
class AdvancedFeatures:
    # 初始化
    def __init__(self, array):
        # 接受一个数组并将其转换为numpy数组
        self.array = np.array(array)

    # 数组操作
    def array_operations(self, other_array, operation):
        # 其他数组强制转换为numpy数组
        other_array = np.array(other_array)
        
        # 数组加法
        if operation == 'add':
            return self.array + other_array
        # 数组减法
        elif operation == 'subtract':
            return self.array - other_array
        # 数组乘法
        elif operation == 'multiply':
            return self.array * other_array
        # 数组除法
        elif operation == 'divide':
            return self.array / other_array
        # 无效操作
        else:
            raise ValueError("Invalid operation")

    # 返回数组的统计信息
    def statistics(self):
        return {
            # 平均值
            'mean': np.mean(self.array),
            # 最大值
            'max': np.max(self.array),
            # 最小值
            'min': np.min(self.array),
            # 总和
            'sum': np.sum(self.array),
            # 标准差
            'std': np.std(self.array),
            # 方差
            'var': np.var(self.array)
        }

    # 幂运算
    def power(self, exponent):
        return np.power(self.array, exponent)

# 模块七：提示函数参数
class FunctionSignature:
    # 静态方法下的获取函数签名
    @staticmethod
    def get_signature(func):
        # 获取函数的签名
        signature = inspect.signature(func)
        # 返回函数名和签名字符串
        return f"{func.__name__}{signature}"

# 模块八：代码格式化
class CodeFormatter:
    # 静态方法下的格式化代码
    @staticmethod
    def format_code(code):
        # 使用 autopep8 对代码进行格式化
        return autopep8.fix_code(code)

# 模块九：文件操作模块
class FileOperations:
    # 静态方法下的读取文件内容
    @staticmethod
    def read_file(filename):
        # 尝试以读取模式打开文件
        try:
            with open(filename, 'r') as file:
                # 读取文件内容
                content = file.read()
            return content
        # 处理文件未找到错误
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return None
        # 处理其他异常
        except Exception as e:
            print(f"Error reading file '{filename}': {str(e)}")
            return None

    # 静态方法下的将内容写入文件
    @staticmethod
    def write_to_file(filename, content):
        # 尝试以写入模式打开文件
        try:
            with open(filename, 'w') as file:
                # 将内容写入文件
                file.write(content)
            print(f"Content successfully written to '{filename}'.")
        # 处理写入文件时的异常
        except Exception as e:
            print(f"Error writing to file '{filename}': {str(e)}")

# 模块十：数学操作模块
class MathOperations:
    # 静态方法下的计算阶乘
    @staticmethod
    def factorial(n):
        # 尝试直接计算阶乘
        try:
            return math.factorial(n)
        # 处理值错误（例如传入负数）
        except ValueError as ve:
            print(f"ValueError: {str(ve)}")
            return None
        # 处理其他异常
        except Exception as e:
            print(f"Error calculating factorial: {str(e)}")
            return None

    # 静态方法下的计算最大公约数
    @staticmethod
    def gcd(a, b):
        # 尝试直接计算公约数
        try:
            return math.gcd(a, b)
        # 处理异常
        except Exception as e:
            print(f"Error calculating GCD: {str(e)}")
            return None

    # 静态方法下的计算最小公倍数
    @staticmethod
    def lcm(a, b):
        # 尝试使用最大公约数计算最小公倍数
        try:
            return abs(a * b) // math.gcd(a, b)
        # 处理异常
        except Exception as e:
            print(f"Error calculating LCM: {str(e)}")
            return None

# 模块十一：日期时间操作模块
class DateTimeOperations:
    # 静态方法下的获取当前日期和时间
    @staticmethod
    def current_datetime():
        # 时间格式化为字符串
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 静态方法下的格式化给定的日期时间对象
    @staticmethod
    def format_datetime(dt):
        # 时间格式化为字符串
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    # 静态方法下的计算两个日期之间的天数
    @staticmethod
    def days_between_dates(date1, date2):
        # 尝试直接计算日期之差
        try:
            # 将字符串格式的日期转换为日期对象
            date1 = datetime.strptime(date1, "%Y-%m-%d")
            date2 = datetime.strptime(date2, "%Y-%m-%d")
            # 计算日期差
            delta = date2 - date1
            return delta.days
        # 处理日期格式错误
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return None
        # 处理其他异常
        except Exception as e:
            print(f"Error calculating days between dates: {str(e)}")
        return None

    # 静态方法下的在给定日期上增加指定天数
    @staticmethod
    def add_days(date_str, days_to_add):
        # 尝试直接处理
        try:
            # 将字符串格式的日期转换为日期对象
            date = datetime.strptime(date_str, "%Y-%m-%d")
            # 增加指定天数
            new_date = date + timedelta(days=days_to_add)
            # 将新的日期格式化为字符串
            return new_date.strftime("%Y-%m-%d")
        # 处理日期格式错误
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return None
        # 处理其他异常
        except Exception as e:
            print(f"Error adding days to date: {str(e)}")
            return None

# 模块十二：加密解密模块
class Encryption:
    @staticmethod
    # 静态方法下的加密文本
    def encrypt(text, key):
        # 初始化存储加密后的字符
        encrypted_text = []
        
        # 对每个字符的 ASCII 码加上密钥值
        for char in text:
            encrypted_text.append(chr(ord(char) + key))
        
        # 将列表中的字符连接成字符串并返回
        return ''.join(encrypted_text)

    # 静态方法下的解密文本
    @staticmethod
    def decrypt(encrypted_text, key):
        # 初始化存储解密后的字符
        decrypted_text = []
        
        # 对每个字符的 ASCII 码减去密钥值
        for char in encrypted_text:
            decrypted_text.append(chr(ord(char) - key))
        
        # 将列表中的字符连接成字符串并返回
        return ''.join(decrypted_text)

# 模块十三：日志记录模块
class Logging:
    # 静态方法下的记录日志信息
    @staticmethod
    def log(message):
        # 获取当前时间戳，并格式化为字符串
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 打印带有时间戳的日志信息
        print(f"[{timestamp}] {message}")

# 主程序
def main():
    # 循环读入代码
    while True:
        code = input("请输入代码进行处理（输入0退出）: ")

        # 退出循环
        if code == '0':
            break
        
        # 尝试识别源代码
        try:
            # Step 1: 高亮代码
            lexer = Lexer()
            highlighted_code = lexer.highlight(code)
            print("Highlighted Code:\n", highlighted_code)

            # Step 2: 语法分析及其格式化
            analyzer = SyntaxAnalyzer(code)
            signatures = analyzer.get_function_signatures()
            formatted_code = analyzer.format_code()
            print("Function Signatures:", signatures)
            print("Formatted Code:\n", formatted_code)
            print("Abstract Syntax Tree (AST):\n", analyzer.get_ast())

            # Step 3: 格式化输入输出
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

            # Step 4: 数据类型扩展
            ds = DataStructureExtension()
            sub_choice = input("请输入数据类型和值（如：int 5, float 3.14, str 'hello', dict key:value）或输入exit退出: ")
            while sub_choice != 'exit':
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
                sub_choice = input("请输入数据类型和值或输入exit退出: ")

            # Step 5: 出错处理
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

            # Step 6: 高级数学运算
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

            # Step 7: 函数名识别
            func_name = input("请输入函数名：")
            try:
                func = eval(func_name)
                signature = FunctionSignature.get_signature(func)
                print(f"Function Signature: {signature}")
            except NameError:
                print("函数不存在，请输入正确的函数名。")

            # Step 8: 代码格式化
            formatted_code = CodeFormatter.format_code(code)
            print("Formatted Code:\n", formatted_code)

            # Step 9: 文件操作
            filename = input("请输入文件名进行读取（或输入exit退出）: ")
            if filename == 'exit':
                break
            content = FileOperations.read_file(filename)
            if content:
                print(f"File Content:\n{content}")

            # Step 10: 数学操作
            num = input("请输入要计算阶乘的数字: ")
            try:
                num = int(num)
                factorial_result = MathOperations.factorial(num)
                if factorial_result is not None:
                    print(f"{num}的阶乘是: {factorial_result}")
            except ValueError:
                print("请输入一个整数。")

            a = input("请输入第一个整数用于计算最大公约数和最小公倍数: ")
            b = input("请输入第二个整数: ")
            
            try:
                a = int(a)
                b = int(b)
                gcd_result = MathOperations.gcd(a, b)
                lcm_result = MathOperations.lcm(a, b)
                if gcd_result is not None:
                    print(f"{a}和{b}的最大公约数是: {gcd_result}")
                if lcm_result is not None:
                    print(f"{a}和{b}的最小公倍数是: {lcm_result}")
            except ValueError:
                print("请输入两个整数。")

            # Step 11: 时间操作
            date_choice = input("请输入要执行的日期时间操作（current, format, days_between, add_days）: ")
            if date_choice == 'current':
                print("Current Datetime:", DateTimeOperations.current_datetime())
            elif date_choice == 'format':
                dt_str = input("请输入要格式化的日期时间（如 2024-01-01 12:00:00）: ")
                formatted_dt = DateTimeOperations.format_datetime(dt_str)
                print("Formatted Datetime:", formatted_dt)
            elif date_choice == 'days_between':
                date1 = input("请输入第一个日期（YYYY-MM-DD）: ")
                date2 = input("请输入第二个日期（YYYY-MM-DD）: ")
                days = DateTimeOperations.days_between_dates(date1, date2)
                if days is not None:
                    print(f"Days between {date1} and {date2}: {days}")
            elif date_choice == 'add_days':
                date_str = input("请输入日期（YYYY-MM-DD）: ")
                days_to_add = int(input("请输入要添加的天数: "))
                new_date = DateTimeOperations.add_days(date_str, days_to_add)
                if new_date is not None:
                    print(f"New Date after adding {days_to_add} days:", new_date)
            else:
                print("Invalid choice for date and time operations.")

            # Step 12: 文本加密与解密
            text = input("请输入要加密的文本: ")
            key = int(input("请输入加密密钥（整数）: "))
            
            # 加密文本
            encrypted_text = Encryption.encrypt(text, key)
            print("Encrypted Text:", encrypted_text)

            # 解密文本
            decrypted_text = Encryption.decrypt(encrypted_text, key)
            print("Decrypted Text:", decrypted_text)

            # Step 13: 日志
            message = input("请输入要记录的日志消息: ")
            Logging.log(message)

        # ctrl + C
        except KeyboardInterrupt:
          print("\n操作中断，程序退出。")
          break
        # 其他异常
        except Exception as e:
          print(f"发生异常: {str(e)}，请检查并重试。")

# 主函数
if __name__ == "__main__":
    main()