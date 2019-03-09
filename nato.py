# coding: UTF-8
import sys

# 関数checkNato
# 引数に数値を入力し、Natoの何作目のレコード番号と一致するかを表示する。
def checkNato(target):
  n = 5       # 1作目のレコード番号は「5」
  diff = 2    # 階差の初期値

  for i in range(1000):    # range関数の引数1000は仮置き
    if n == target:
      print(i + 1)
      break

    n = n + diff
    diff = diff + 1

# コマンドライン引数を変数targetに代入する
args = sys.argv
target = int(args[1])

checkNato(target)
