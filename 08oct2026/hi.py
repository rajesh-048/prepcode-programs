l=[]
n=int(input())
for i in range(n):
    a=int(input())
    l.append(a)
ans=[]
for val in l:
    if l.count(val)==1 and val not in ans:
        ans.append(val)
print(ans)