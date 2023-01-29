def test_case():
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a

    # a - 2x = b - x
    # a - b = x
    x = a - b
    a -= 2 * x
    b -= x
    if a >= 0 and a % 3 == 0:
        print('YES')
    else:
        print('NO')


t = int(input())
for _ in range(t):
    test_case()
