from test2 import Lexer, SyntaxAnalyzer, IOExtension, DataStructureExtension, ErrorHandling, AdvancedFeatures, FunctionSignature, CodeFormatter, FileOperations, MathOperations, DateTimeOperations, Encryption, Logging

# 主程序
def main():
    # 初始化数据结构扩展模块
    ds = DataStructureExtension()
    
    # 初始化错误处理模块
    eh = ErrorHandling()
    
    # 添加任务
    while True:
        task = input("请输入任务（或输入exit退出）: ")
        if task.lower() == 'exit':
            break
        ds.add_dict(task, False)  # False 表示任务未完成
    
    # 标记任务为完成
    while True:
        task = input("请输入要标记为完成的任务（或输入exit退出）: ")
        if task.lower() == 'exit':
            break
        
        try:
            if task in ds.get_dict():
                ds.add_dict(task, True)  # True 表示任务已完成
            else:
                print("任务不存在，请重新输入。")
        except KeyError:
            eh.handle_error("KeyError", "任务不存在")
    
    # 显示所有任务及其状态
    for task, completed in ds.get_dict().items():
        status = "完成" if completed else "未完成"
        IOExtension.formatted_output(f"任务: {task} 状态: {status}")
    
    # 处理可能的输入错误
    try:
        test_task = IOExtension.formatted_input("请输入测试任务: ", str)
        IOExtension.formatted_output(test_task)
    except ValueError:
        eh.handle_error("ValueError", "输入的任务无效")

# 主函数
if __name__ == "__main__":
    main()