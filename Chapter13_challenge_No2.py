#第13章　チャレンジ問題
#No.2_Squareクラスにchange_sizeメソッドを定義して、
#     そこに渡した数値の分だけSquareオブジェクトの横幅を増やしたり、
#     減らしたり（マイナス値の場合）してみよう

class Square:
    def __init__(self, len):
        self.len = len

    def calculate_perimeter(self):
        return self.len * 4

    def change_size(self, len):
        self.len += len

squ1 = Square(20)
print(squ1.len)
squ1.change_size(5)
print(squ1.len)


squ2 = Square(30)
print(squ2.len)
squ2.change_size(-10)
print(squ2.len)
