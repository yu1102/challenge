#第８章　チャレンジ問題
#No.1_statisticsモジュールの別の関数を呼んでみよう。

import statistics

nums = [3,7,11,16,23]
print(nums)

# データ数が奇数の場合は中央の値を返し、偶数の場合は中央の2値の小さい方を返す。
result = statistics.median_low(nums)
print(result)



#No.2_cubedという名前のモジュールを作って関数を1つ書こう。
#　　 関数は1つの数値を引数として受け取り、渡された数値を3乗して返そう。
#　　 このモジュールをほかのモジュールからインポートして関数を呼び出そう。

import cubed

result = cubed.f(3)
print(result)
