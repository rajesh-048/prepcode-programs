n=int(input("enter a nub"))
for i in range(1,n-1):
    print("  "*(n-1),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(1,i):
        print(j,end=" ")
print()
