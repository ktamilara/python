class Node:
  def __init__(self1,data):
    self1.value=data
    self1.right=None
    self1.left=None

def insert(root,data):
  if root is None:
    root=Node(data)
  elif root.value > data:
    if root.left is None:
      root.left=Node(data)
    else:
      insert(root.left,data)
  elif root.value < data:
    if root.right is None:
      root.right=Node(data)
    else:
      insert(root.right,data)

def LCA(root,L_val,R_val):
  if root is None:
    return None
  elif L_val > root.value and R_val > root.value:
    return(LCA(root.right,L_val,R_val))
  elif L_val < root.value and R_val < root.value:
    return (LCA(root.left,L_val,R_val))
  else:
    return root.value

n11=int(input())
val1=list(map(eval1,input().split()))
u1,v1=map(eval,input().split())
R1=Node(val1[0])
for i1 in range(1,n11):
  insert(R1,val[i1])
print(LCA(R1,u1,v1))
