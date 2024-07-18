""" 
Instead of using pointers, just move along and count.
"""

s = input()

max_count = 0
count = 0
current = ""

for el_ in s:
    if el_ == current:
        count += 1
    else:
        max_count = max(count, max_count)
        count = 1
        current = el_

max_count = max(count, max_count)

print(max_count)