from itertools import groupby
from operator import itemgetter

dna = input()

longest_group = {'len': 0, 'key': None}
for key, group in groupby(dna):
    current_group = {'len': len(list(group)), 'key': key}
    longest_group = max(longest_group, current_group, key=itemgetter('len'))

print(longest_group['len'])
