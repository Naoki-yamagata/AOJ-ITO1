
while True:
    h,w = map(int,input().split())
    if w==h==0:
        break
    print("#"*w)
    for i in range(h-2):
        print("#","."*(w-2),"#",sep="")
    print("#"*w)
    print("")