a1=int(input())
b1=list(map(int,input().split()))
t1=[]
for i1 in b1:
  t1.append(i1)
t1.reverse()
print(*t1,sep="->")
