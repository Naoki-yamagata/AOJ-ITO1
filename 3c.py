
while True:
    a,b=map(int,input().split())
    if a==b==0:
        break
    if a>=b:
        print(b,a)
    elif a<b:
        print(a,b)