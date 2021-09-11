
while True:
    num_str = input()

    #０なら終了
    if num_str == "0":
        break

    #str型なのでiterableとして合計を出す
    Sum = 0
    for i in num_str:
        Sum += int(i)
    
    #出力
    print(Sum)