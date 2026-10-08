l = list()
n = int(input())
for _ in range(n):
    a = int(input())
    l.append(a)
for val in l:
    print(val, l.count(val))
