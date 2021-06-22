#第５章　チャレンジ問題
#No.1_好きなミュージシャンのリストを作ろう。

musicans = ["ガーネットクロウ","倉木麻衣","ポルノグラフィティ","T.M.Revolution","水樹奈々","B'z"]
print(musicans)



#No.2_タプルのリストを作ろう。
#     各タプルにはあなたがいったことのある場所の緯度と経度を持たせよう。

place = []

tokyo = ("35.4122","139.4130")
hokkaido = ("43.0351","141.2049")
kyoto = ("35.0117","135.4520")

place.append(tokyo)
place.append(hokkaido)
place.append(kyoto)

print(place)



#No.3_辞書を作ろう。
#     辞書にはあなたの特徴を表すキーバリューのペアを持たせよう。
#     たとえば、身長、好きな色、好きな作家、など。

profile = {
    "身長": "158.8cm",
    "好きな色": "水色",
    "好きな動物": "ウサギ"
    }

print(profile)



#No.4_任意のキーを入力させるプログラムを書こう。
#     入力されたキーを使って、1つ前のチャレンジで用意した辞書から、バリューを取得して表示しよう。

n = input("身長・好きな色・好きな動物のいずれかを入力してください: ")

if  n in profile:
    prf = profile[n]
    print(prf)
else:
    print("入力エラー")



#No.5_あなたが好きなミュージシャンを辞書のキーに入れ、
#     そのバリューとしてそのミュージシャンの曲をリストで持たせよう。

favorite = {
    "ガーネットクロウ" : ["夏の幻", "夢花火"],
    "倉木麻衣" : ["secret of my heart","time after time"],
    "ポルノグラフィティ" : ["アゲハ蝶","サウダージ"],
    "T.M.Revolution" : ["Flags","SWORD SUMMIT"],
    "水樹奈々" : ["Exterminate","ETERNAL BLAZE"],
    "B'z" : ["ultra soul","今宵月の見える丘に"]
    }

print(favorite)


#No.6_リスト、タプル、辞書はPyhtonの組み込みコンテナの一部です。
#     Pythonのset（コンテナ型の1つ）について調べよう。
#     setは何に使えるだろう？

#set は集合を表すデータ型。
#リストとは異なり要素は順番を持たず、また重複した要素は取り除かれる。
#setは「和集合、積集合、差集合」などの集合演算（論理演算）に使用できる。
