a = "#"
b = "*"
n = int(input())
for val in range(1, n + 1):
    print(a * (n - val), b * val)
