import sys

#入力
word_list = sys.stdin.readlines()

alpha_count = [0 for i in range(26)]
alpha_list = [chr(i) for i in range(97,123)]
for word in word_list:
    for i in range(26):
        alpha_count[i] += word.count(alpha_list[i])+word.count(alpha_list[i].upper())

#出力
for i in range(26):
    print(f"{alpha_list[i]} : {alpha_count[i]}") 