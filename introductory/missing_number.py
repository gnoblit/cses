n = int(input())
possible_nums = set(range(1, n+1))
l = set([int(x) for x in input().split()])
print((possible_nums - l).pop())
