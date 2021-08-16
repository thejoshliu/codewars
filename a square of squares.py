# A square of squares
# Task
# Given an integral number, determine if it's a square number:
# # In mathematics, a square number or perfect square is an integer that is the square of an integer;
# in other words, it is the product of some integer with itself.

# The tests will always use some integral number, so don't worry about that in dynamic typed languages.

def is_square(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    elif isinstance(n, int) is False:
        return False
    else:
        psqlist = []
        for each in range(n):
            sq = each * each
            psqlist.append(sq)

        if n in psqlist:
            return True

        else:
            return False

## takes too long

import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;