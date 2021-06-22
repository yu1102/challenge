#第９章　チャレンジ問題
#No.3_リストのリストに含まれている要素をCSVファイルに書き出そう。
#　　 データは次の通り：
#　　 [["Top Gun", "Risky Business", "Minority Report"],
#　　  ["Titanic", "The Revenant", "Inception"],
#　　  [ "Training Day", "Man on Fire", "Flight"]]
#　　 データの各要素はCSVの1行となり、その1行に含まれる各要素がカンマで区切られるように書き出そう。

import os, csv
os.chdir("D:\\由有\\会社\\Python学習\\PY\\Challenge\\Chapter9")


# 映画リスト
movies_list = [["Top Gun", "Risky Business", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"],
          [ "Training Day", "Man on Fire", "Flight"]]


# リストから１行読み込む
# カンマ区切りで要素をファイルに書き出す
with open("No3_movies.csv", "w",newline='', encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for movies in movies_list:
        w.writerow(movies)
