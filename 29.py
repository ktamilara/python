n11=int(input())
l1=list(map(int,input().split()))
p1=[]
for i1 in range(n11-1):
	for j1 in range(i1,n11):
		c1=l1[i1:j1+1]
		p1.append(sum(c1))
print(max(p1))
