res = set()
for i in range(10, 1001):
    x = bin(i)[3:]
    x = int(x, 2)
    res.add(i - x)
print(len(res))