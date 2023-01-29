n = int(input())

p2, p5 = 0, 0
for i in range(1, 32):
    p2 += n // (2 ** i)
    p5 += n // (5 ** i)

print(min(p2, p5))
