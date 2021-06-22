#第９章　チャレンジ問題
#No.4_チャレンジ3を日本語で同じようにやってみよう。
#　　 たとえば、"Top Gun"を"トップガン"のように日本語に置き換えて、CSVファイルに書き出そう。

import os, csv
os.chdir("D:\\由有\\会社\\Python学習\\PY\\Challenge\\Chapter9")


# 映画リスト
movies_list = [["トップガン", "卒業白書", "マイノリティ・リポート"],
          ["タイタニック", "レヴェナント", "インセプション"],
          [ "トレーニングデイ", "マイ・ボディガード", "フライト"]]


# リストから１行読み込む
# カンマ区切りで要素をファイルに書き出す
with open("No4_movies.csv", "w",newline='', encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for movies in movies_list:
        w.writerow(movies)
