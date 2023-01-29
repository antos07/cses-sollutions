t = int(input())
for n in range(1, t + 1):
    ans = (n - 1) * (n + 4) * (n ** 2 - 3 * n + 4) // 2
    print(ans)
