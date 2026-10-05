n=int(input())
for row in range(0,n):
    for col in range(0,n):
        if  row==col and row<=n//2:
            print("* ",end=" ")
        elif row +col==n-1 and row<=n//2:
            print(" ",end=" ")
        else:
            print
    print()