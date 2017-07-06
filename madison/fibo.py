prev = 0
temp = 0
cur = 1

for n in range(10):
    print(cur)
    temp = cur
    cur = prev + cur
    prev = temp
