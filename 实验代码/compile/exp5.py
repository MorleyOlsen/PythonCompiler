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

# 示例用法
eh = ErrorHandling()
print(eh.divide(10, 0))
print(eh.divide(10, "a"))
