#第13章　チャレンジ問題
#No.4_HorseクラスとRiderクラスを定義しよう。
#     コンポジションを使って、馬（Hose）に騎手（Rider）を持たせよう。
#     

class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name


a_rider = Rider("Michael")
a_hose = Horse("Nick", a_rider)

print("The Horse is {}".format(a_hose.name))
print("The Rider is {}".format(a_hose.rider.name))
