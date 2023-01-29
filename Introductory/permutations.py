n = int(input())

if 1 < n <= 3:
    print('NO SOLUTION')
    exit(0)

all_odd = list(range(1, n + 1, 2))
all_even = list(range(2, n + 1, 2))
ans = all_even + all_odd

print(*ans)
