s11=0
q1=0
r1=int(input())
while(r1!=0):
    t1=r1%10
    s11=s11+t1
    r1=r1//10
a1=s11

if(s11<9):
    print("YES")
else:
    while(s11!=0):
        f1=s11%10
        q1=f1+(q1*10)
        
        s11=s11//10
    if(a1==q1):
        print("YES")
    else:
        print("NO")
