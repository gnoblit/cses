"""
Going to look at current element and previous element.
Going to count how many times I have to add 1 to the current element to make it equal to the previous
"""
n = int(input())
array = [int(x) for x in input().split(' ')]

tracker = 0

for iter_ in range(1, len(array)):
    while array[iter_] < array[iter_ - 1]:
        difference = array[iter_ - 1] - array[iter_]
        array[iter_] = array[iter_ - 1]

        tracker += difference

print(tracker)