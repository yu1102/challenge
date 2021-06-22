#第14章　チャレンジ問題
#No.1_Squareクラスにsquare_listクラス変数を追加しよう。
#     そして、新しくSquareオブジェクトが作られるたびに、そのオブジェクトをこのリストに追加しよう。

class Square:
    square_list = []

    def __init__(self, len):
        self.len = len
        self.square_list.append(self.len)


sq1 = Square(5)
print(Square.square_list)

sq2 = Square(10)
print(Square.square_list)

sq3 = Square(100)
print(Square.square_list)
