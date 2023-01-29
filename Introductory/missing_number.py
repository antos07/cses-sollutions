n = int(input())
a = {int(number) for number in input().split()}
all_numbers = set(range(1, n + 1))
diff = all_numbers - a
diff = diff.pop()
print(diff)
