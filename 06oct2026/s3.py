n=int(input())
for row in range(0,n):
    for col in range(0,n):
        if row==0 and col<=n//2:
            print("* ",end=" ")
        elif col==0 and row<=n//2:
            print("* ",end=" ")
        elif row==n//2 and col<=n//2:
            print("* ",end=" ")
        elif col==n//2:
            print("* ",end=" ")
        elif row==n-1 and col>=n//2:
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print()