#第９章　チャレンジ問題
#No.1_コンピューターにある何かのファイルをPythonで開いて、コンテンツを出力しよう。
"""
ファイルの存在確認をして、コンテンツを出力する
"""

import os
os.chdir("D:\\由有\\会社\\Python学習\\PY\\Challenge\\Chapter9")

# ファイルの存在確認
file = input("type a file name: ")
os.path.isfile(file)

# ファイルの読み込み
with open(file,"r", encoding="utf-8") as f:
    print(f.read())
