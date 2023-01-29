n = int(input())

if n % 4 in (1, 2):
    print('NO')
    exit(0)

set1 = []
set2 = []

start = 1
if n % 4 == 3:
    set1 += [1, 2]
    set2 += [3]
    start = 4

for i in range(start, n + 1, 4):
    set1 += [i, i + 3]
    set2 += [i + 1, i + 2]

print('YES')
print(len(set1))
print(*set1)
print(len(set2))
print(*set2)
