#第17章　チャレンジ問題
#No.1_grepを使って、The Zen of Pythonの文中にある"Dutch"という単語に一致する正規表現を書こう。

grep Ducth zen.txt


#No.2_grepを使って、文字列"Arizona 479, 501, 870. California 209, 213, 650."にある、
#     数字の部分すべてに一致する正規表現を書こう。

echo Arizona 479, 501, 870. California 209, 213, 650. | grep [[:digit:]]

#No.3_Pythonのreモジュールを使って、何かの文字の後ろにoが2回登場する単語に一致する正規表現を書こう。
#     そして、"The ghost that says boo haunts the loo"の文中にあるbooやlooに一致するか試そう。

import re

text = "The ghost that says boo haunts the loo"
m = re.findall(" .oo", text)
print(m)
