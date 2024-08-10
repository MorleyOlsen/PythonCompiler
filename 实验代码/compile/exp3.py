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
        else:
            print(f"Output: {data}")

# 示例用法
age = IOExtension.formatted_input("Enter your age: ", int)
IOExtension.formatted_output(age)

# generate codes