for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    odd=[]
    even=[]
    for i in range(n):
        if li[i]%2==0:
            even.append(li[i])
        else:
            odd.append(li[i])
    if len(odd)%2==1:
        print("NO")
    else:
        print("YES")
