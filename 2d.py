W,H,x,y,r=map(int,input().split())

if W>=x+r and H>=y+r and x>=r and y>=r:
    print("Yes")
else:
    print("No")