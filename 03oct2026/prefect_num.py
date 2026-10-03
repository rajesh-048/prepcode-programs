l = 1
a = int(input("Enter a number: "))
sum = 0
while l < a:
    if a % l == 0:
        sum = sum + l
    l = l + 1
if a == sum:
    print("Perfect number")
else:
    print("Not a perfect number")