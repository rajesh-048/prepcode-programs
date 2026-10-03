name = input("Enter your name: ")
sum = 0
for i in name:
    key = ord(i)
    sum = sum + key
print("Hash key value:", sum)
if sum % 2 == 0:
    print("Even")
else:
    print("Odd")
