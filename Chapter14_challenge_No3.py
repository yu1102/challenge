#第14章　チャレンジ問題
#No.3_2つのパラメーターを受け取る関数を書こう。
#     この関数は同じオブジェクトを渡されたらTrueを返し、そうじゃなかったらFalseを返そう。

def compare(x, y):
    return x is y


print(compare(11,2))
print(compare(5,5))
        
    
