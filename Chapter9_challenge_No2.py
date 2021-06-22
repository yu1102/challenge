#第９章　チャレンジ問題
#No.2_何か質問するプログラムを書こう。
#　　 入力された回答をファイルに書き出そう。

import os
os.chdir("D:\\由有\\会社\\Python学習\\PY\\Challenge\\Chapter9")

# 標準入力取得
answer = input("好きな色は何ですか？：")

with open("No2_answer.txt", "w", encoding="utf-8") as f:
    f.write(answer)
