def inverse(s):
    res = ''
    for i in s:
        if i == '1':
            res += '0'
        else:
            res += '1'
    return s


for n in range(128, 256):
    x = bin(n)[2:]
    a = n - int(inverse(x), 2)
    print(n)
    if a == 105:
        print(n)
        break
