n = int(input("enter a num"))
sum = 0
for val in range(1,n+1,2):
    print(val, end=" ")
    sum = sum + val
print(sum)