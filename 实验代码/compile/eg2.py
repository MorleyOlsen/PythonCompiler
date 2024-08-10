from test2 import Lexer, SyntaxAnalyzer, IOExtension, DataStructureExtension, ErrorHandling, AdvancedFeatures, FunctionSignature, CodeFormatter, FileOperations, MathOperations, DateTimeOperations, Encryption, Logging

# 主程序
def main():
    # 初始化错误处理模块
    eh = ErrorHandling()

    while True:
        try:
            # 输入总头数
            heads = IOExtension.formatted_input("请输入总头数（或输入-1退出）: ", int)
            if heads == -1:
                break
            
            # 输入总脚数
            legs = IOExtension.formatted_input("请输入总脚数: ", int)
            
            # 计算兔子的数量
            rabbits = (legs - 2 * heads) / 2
            # 计算鸡的数量
            chickens = heads - rabbits
            
            # 检查计算结果是否为非负整数
            if rabbits < 0 or chickens < 0 or not rabbits.is_integer() or not chickens.is_integer():
                eh.handle_error("ValueError", "输入的头数和脚数不可能对应实际的鸡和兔子数量")
            else:
                IOExtension.formatted_output(f"鸡的数量: {int(chickens)}")
                IOExtension.formatted_output(f"兔子的数量: {int(rabbits)}")

        except ValueError:
            eh.handle_error("ValueError", "输入的值无效，请输入整数")
        except KeyboardInterrupt:
            print("\n操作中断，程序退出。")
            break
        except Exception as e:
            eh.handle_error(type(e).__name__, str(e))

if __name__ == "__main__":
    main()