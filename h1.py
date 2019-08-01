D=int(input())
V=list(map(int,input().split()))
Y=sorted(V)
N=Y[::-1]
P=[]
for j in range(0,len(V)):
  P.append(N[j])
  P.append(Y[j])
for k in P[:len(V)]:
  print(k,end=" ")
