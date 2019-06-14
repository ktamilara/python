r11=int(input())
s1=list(map(int,input().split()))
f1=[]
f1.append(sum(s1))
for i1 in range(0,r11-1):
  a1=s1[:i1+1]
  y1=s1[1i+1:]
  if sum(a1)>sum(y1):
    f1.append(sum(a1))
  else:
    f1.append(sum(y1))
print(max(f))
