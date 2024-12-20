from math_operations import MathOperations, calculate_percentage

class Calculator:
    def __init__(self):
        self.math_ops = MathOperations()
        self.history = []
    
    def perform_calculation(self, operation, value):
        """計算を実行し、履歴に保存する"""
        original_value = self.math_ops.get_value()
        
        if operation == 'add':
            result = self.math_ops.add(value)
        elif operation == 'subtract':
            result = self.math_ops.subtract(value)
        elif operation == 'multiply':
            result = self.math_ops.multiply(value)
        elif operation == 'divide':
            result = self.math_ops.divide(value)
        else:
            raise ValueError(f"不明な操作です: {operation}")
        
        self.history.append({
            'operation': operation,
            'value': value,
            'before': original_value,
            'after': result
        })
        
        return result
    
    def get_history(self):
        """計算履歴を取得する"""
        return self.history
    
    def calculate_growth(self, initial, final):
        """成長率を計算する"""
        if initial == 0:
            raise ValueError("初期値が0の場合、成長率を計算できません")
        growth = ((final - initial) / initial) * 100
        return f"{growth:.2f}%"
    
    def clear_history(self):
        """履歴をクリアし、計算機をリセットする"""
        self.history = []
        self.math_ops.reset()
