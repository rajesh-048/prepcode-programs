n=int(input())
for row in range(0,n):
    for col in range(2*n-1):
        if col == n-1-row or col == n-1+row or row ==n-1:
            print("* ",end="" )
        else:
            print("  ",end=" ")
print()