#第10章　チャレンジ問題
#No.1_プログラムを書き換えて、答えの単語をリストからランダムに選ぶようにしよう。

import random

def hangman():
    # リストから答えを選択する
    word_list = ["cat", "dog", "rabbit", "bird", "hamster"]
    num = random.randint(0,len(word_list))
    word = word_list[num]
    
    wrong = 0
    stages = ["",
              "______________             ",
              "|                          ",
              "|             |            ",
              "|             O            ",
              "|            //|           ",
              "|            //            ",
              "                           ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    
    # 正解するか、不正解を重ねてイラストが完成するまでループする
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね："
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1

        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
                
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
        
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))



hangman()
