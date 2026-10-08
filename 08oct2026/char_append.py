a = input()
li = []
vow = 'aeiouAEIOU'
for ch in a:
    if ch not in li and ch not in vow:
        li.append(ch)
print(li)
