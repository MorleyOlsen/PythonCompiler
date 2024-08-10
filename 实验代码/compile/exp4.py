class DataStructureExtension:
    def __init__(self):
        self.int_array = []
        self.float_array = []

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

    def get_int_array(self):
        return self.int_array

    def get_float_array(self):
        return self.float_array

# 示例用法
ds = DataStructureExtension()
ds.add_int(5)
ds.add_float(3.14)
print("Int Array:", ds.get_int_array())
print("Float Array:", ds.get_float_array())
