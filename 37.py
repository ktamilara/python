from itertools import combinations
s1=input()
t11=0
l1=list(combinations(s1,len(s1)-1))
for i1 in range(len(l1)):
    if l1[i1]==l1[i1][::-1]:
        print("YES")
        t11=1
        break
if t11==0:
    print("NO")
