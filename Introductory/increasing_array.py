import itertools

n = int(input())
a = [{'v': int(number)} for number in input().split()]

ans = 0
for prev, cur in itertools.pairwise(a):
    if cur['v'] < prev['v']:
        ans += prev['v'] - cur['v']
        cur['v'] = prev['v']
print(ans)
