def test_case():
    r, c = map(int, input().split())

    full_square_side = max(c, r)
    if full_square_side % 2 == 0:
        to_add = r if r < full_square_side else 2 * full_square_side - c
    else:
        to_add = c if c < full_square_side else 2 * full_square_side - r
    ans = (full_square_side - 1) ** 2 + to_add
    print(ans)


n = int(input())
for _ in range(n):
    test_case()
