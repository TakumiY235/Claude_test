class MathOperations:
    def __init__(self, initial_value=0):
        self.value = initial_value
    
    def add(self, x):
        """数値を加算する"""
        self.value += x
        return self.value
    
    def subtract(self, x):
        """数値を減算する"""
        self.value -= x
        return self.value
    
    def multiply(self, x):
        """数値を乗算する"""
        self.value *= x
        return self.value
    
    def divide(self, x):
        """数値を除算する"""
        if x == 0:
            raise ValueError("0での除算はできません")
        self.value /= x
        return self.value
    
    def get_value(self):
        """現在の値を取得する"""
        return self.value
    
    def reset(self):
        """値を0にリセットする"""
        self.value = 0
        return self.value

def calculate_percentage(value, total):
    """パーセンテージを計算する"""
    if total == 0:
        raise ValueError("合計が0の場合、パーセンテージを計算できません")
    return (value / total) * 100