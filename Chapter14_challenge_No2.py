#第14章　チャレンジ問題
#No.2_Squareクラスのオブジェクトをprint関数に渡したら、4辺それぞれの長さを出力しよう。
#     たとえば、Square(29)のようにオブジェクトを作ったら、
#     print関数では29 by 29 by 29 by 29 と出力しよう。

class Square:
    def __init__(self, len):
        self.len = len

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.len, self.len, self.len, self.len)


sq1 = Square(29)
sq2 = Square(50)
sq3 = Square(100)

print(sq1)
print(sq2)
print(sq3)
