#第13章　チャレンジ問題
#No.1_RectangleとSquareクラスを作ろう。
#     両方のクラスに、その図形の外周の長さを計算して返すcalculate_perimeterメソッドを定義しよう。
#     そして、RectangleとSquareオブジェクトをつくって、それぞれのcalculate_perimeterメソッドを呼ぼう。

class Rectangle:
    def __init__(self, width, len):
        self.width = width
        self.len = len

    def calculate_perimeter(self):
        return (self.width + self.len) * 2
    

class Square:
    def __init__(self, len):
        self.len = len
        
    def calculate_perimeter(self):
        return self.len * 4


rectangle = Rectangle(20, 30)
print(rectangle.calculate_perimeter())

square = Square(50)
print(square.calculate_perimeter())
