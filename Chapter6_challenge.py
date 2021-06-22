#第６章　チャレンジ問題
#No.1_文字列"カミュ"に含まれるすべての文字を一文字ずつ出力しよう。

name = "カミュ"
print(name[0])
print(name[1])
print(name[2])



#No.2_2つの文字列を入力させるプログラムを書こう。
#     その文字列をそれぞれ、別の文字列の2つの箇所に穴埋めした新しい文字列を作ろう。
#     "私は昨日[入力1]を書いて、[入力2]に送った！"
#     そしてそれを出力しよう。

what = input("何を：")
who = input("誰に：")

print("私は昨日{}を書いて、{}に送った！".format(what,who))



#No.3_文法的には正しい文書を書いた文字列"aldous Huxley was born in 1894."の先頭をメソッドを使って大文字にしよう。

words = "aldous Huxley was born in 1894.".capitalize()
print(words)



#No.4_文字列"どこで？　だれが？　いつ？"をメソッドで分割して、
#     ["どこで？","だれが？","いつ？"]のようにリストにしよう。

words = "どこで？　だれが？　いつ？"
print(words.split("　"))
      


#No.5_リスト["The","fox","jumped","orver","the","fence","."]の文字列を正しい英文法になるように連結しよう。
#     単語と単語の間は空白が必要ですが、最後のピリオドの前には空白は不要です。
#     文字列を要素に持つリストを１つに連結するメソッドがあることを忘れずに！      

lst = ["The","fox","jumped","orver","the","fence","."]
line = " ".join(lst)
line= line.replace(" .",".")
print(line)


#No.6_文字列"A screaming comes across the sky."に含まれるすべての"s"をドル記号に置き換えた文字列を作ろう。

words = "A screaming comes across the sky."
words = words.replace("s","$")
print(words)



#No.7_メソッドを使って、"Hemingway"の中で最初に"n"が出現するインデックスを調べよう。

print("Hemingway".index("n"))


#No.8_好きな本の台詞を探して、Pythonの文字列にしよう。
#     ただし、クォート文字が含まれている台詞を選ぶこと。

print("リーダーとは\"希望を配る人\"のことだ。")


#No.9_文字列を"+"で結合して、"three three three"という文字列を作ろう。
#     また、"*"を使って同じ文字列を作ってみよう！

word = "three" + " three" + " three"
print(word)
words = word * 2
print(words)


#No.10_文字列"四月の晴れた寒い日で、時計がどれも十三時を打っていた。"をスライスして、
#     「、」の前までの部分文字列を作ろう。

words = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
print(words[0:10])

