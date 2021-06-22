#第13章　チャレンジ問題
#No.3_Shapeクラスを定義しよう。
#     呼ばれたら"I am a shape"を返すメソッドwhat_am_iを定義しよう。
#     前のチャレンジで定義したRectangleとSquareクラスを変更して、このShapeクラスを継承させよう。
#     そして、RectangleとSquareのオブジェクトを生成して、
#     このチャレンジで追加したメソッドwhat_am_iを呼んでみよう。

class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, width, len):
        self.width = width
        self.len = len

    def calculate_perimeter(self):
        return (self.width + self.len) * 2

class Square(Shape):
    def __init__(self, len):
        self.len = len

    def calculate_perimeter(self):
        return self.len * 4


rectangle = Rectangle(20,40)
rectangle.what_am_i()

square = Square(50)
square.what_am_i()
