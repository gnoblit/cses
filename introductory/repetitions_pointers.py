"""
Iterate through string. 
Interested in contiguous identical characters. So we care about switching chars.
Keep track of previous max
When you switch, set a pointer.
When you switch again, set second pointer.
Calculate difference.
Compare to max, keep if larger than previous max
"""

s = input()
if len(s) == 1:
    print(1)
    exit

else:
    max_len = -1
    l, r = 0, 0

    while r < len(s): # Move along entire string
        if s[r] != s[l]:
            potential_max = r-l # Calculate potential max
            max_len = max(max_len, potential_max) # Take maximum of both and keep larger
            # Reset pointers
            l = r # Move left to switched character
        elif r == len(s) - 1:
            potential_max = r - l + 1
            max_len = max(max_len, potential_max)
        r += 1

    print(max_len)



