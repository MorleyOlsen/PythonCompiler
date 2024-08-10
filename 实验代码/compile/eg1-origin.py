# 任务管理系统
class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if task in self.tasks:
            print(f"任务 '{task}' 已经存在.")
        else:
            self.tasks[task] = False  # False 表示任务未完成

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks[task] = True  # True 表示任务已完成
        else:
            print(f"任务 '{task}' 不存在.")

    def show_tasks(self):
        for task, completed in self.tasks.items():
            status = "完成" if completed else "未完成"
            print(f"任务: {task} 状态: {status}")

    def handle_error(self, err_type, message):
        print(f"{err_type}: {message}")

# 主程序
def main():
    # 初始化任务管理系统
    task_manager = TaskManager()

    # 添加任务
    while True:
        task = input("请输入任务（或输入exit退出）: ")
        if task.lower() == 'exit':
            break
        try:
            task_manager.add_task(task)
        except Exception as e:
            task_manager.handle_error(type(e).__name__, str(e))

    # 标记任务为完成
    while True:
        task = input("请输入要标记为完成的任务（或输入exit退出）: ")
        if task.lower() == 'exit':
            break
        try:
            task_manager.complete_task(task)
        except Exception as e:
            task_manager.handle_error(type(e).__name__, str(e))

    # 显示所有任务及其状态
    task_manager.show_tasks()

if __name__ == "__main__":
    main()
