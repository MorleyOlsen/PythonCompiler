import numpy as np

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
            'sum': np.sum(self.array)
        }

# 示例用法
af = AdvancedFeatures([1, 2, 3, 4, 5])
print("Array Operations (Add):", af.array_operations([5, 4, 3, 2, 1], 'add'))
print("Statistics:", af.statistics())
