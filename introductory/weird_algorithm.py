"""
Function takes in an integer, n.
If n is even, function divides it by 2.
If n is odd, function multiplies by 3 and adds 1
Function does this to own integer until it produces 1
"""

n = int(input())
seq = [n]
while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n = 3*n + 1
    seq.append(int(n))
print(*seq)

