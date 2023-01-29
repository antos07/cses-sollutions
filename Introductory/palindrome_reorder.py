from collections import Counter

counter = Counter(input())
counter = counter.most_common()

odd_cnt = [key for key, cnt in counter if cnt % 2 == 1]
if len(odd_cnt) > 1:
    print('NO SOLUTION')
    exit(0)

left_part = ''.join(key * (cnt // 2) for key, cnt in counter)
right_part = ''.join(reversed(left_part))
ans = left_part + (odd_cnt[0] if odd_cnt else '') + right_part

print(ans)
