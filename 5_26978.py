for i in range(1, 100):
    n = 109 - i
    b = bin(n)[2:]
    if n % 2 == 0:
        b += '10'
    else:
        b += '01'
    r = int(b, 2)
print(r)