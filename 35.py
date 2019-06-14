t1=input()
a11=0
for i1 in range(len(t1)):
    if t1[:i1]==t1[i1+1:]:
        a11=0
        break
    else:
        a11=1
if a11==0:
    print("YES")
else:
    print("NO")
