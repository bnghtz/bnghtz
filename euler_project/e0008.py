# PYTHON 3.6+ !!

"""
Largest product in a series

Problem 8
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
      0        1         2         3         4         5
      12345678901234567890123456789012345678901234567890
      ::::::::::::::::::::::::::::::::::::::::::::::::::
01:   73167176531330624919225119674426574742355349194934
02:   96983520312774506326239578318016984801869478851843
03:   85861560789112949495459501737958331952853208805511
04:   12540698747158523863050715693290963295227443043557
05:   66896648950445244523161731856403098711121722383113
06:   62229893423380308135336276614282806444486645238749
07:   30358907296290491560440772390713810515859307960866
08:   70172427121883998797908792274921901699720888093776
09:   65727333001053367881220235421809751254540594752243
10:   52584907711670556013604839586446706324415722155397
11:   53697817977846174064955149290862569321978468622482
12:   83972241375657056057490261407972968652414535100474
13:   82166370484403199890008895243450658541227588666881
14:   16427171479924442928230863465674813919123162824586
15:   17866458359124566529476545682848912883142607690042
16:   24219022671055626321111109370544217506941658960408
17:   07198403850962455444362981230987879927244284909188
18:   84580156166097919133875499200524063689912560717606
19:   05886116467109405077541002256983155200055935729725
20:   71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

"""
import sys

# read the matrix from text file
fn = "e0008_1000-digit number.txt"
mx = []
for line in open(fn, "r"):
    mx.append(line.rstrip())

max_v = len(mx)
max_h = len(mx[0])

# get lenght of adjacent from argument. Default: 13
adj = int(sys.argv[1]) if len(sys.argv) >= 2 else 13

##############################################################################
## adjecent searching:
## top left corner     (i,j) = (1,1)
## bottom right corner (i,j) = (max_v, max_h) = (20,50)
## NOTE here: the address should generated with (index - 1) !!


def right_diag(i, j):
    """ search matrix for RIGHT DIAGONAL adjacents on the position: (i,j)
        [1]2 3
        4[5]6
        7 8[9]
    Returns:
        if the address points over the matrix => returns with False
        tuple of the RIGHT DIAGONAL numbers
    """
    if (i < 1) or (j < 1) or (i > max_v - adj + 1) or (j > max_h - adj + 1):
        return False
    out = []
    for x in range(0, adj):
        out.append(int(mx[i - 1 + x][j - 1 + x]))
    return tuple(out)


def left_diag(i, j):
    """ search matrix for LEFT DIAGONAL adjacents on the position: (i,j)
        1 2[3]
        4[5]6
        [7]8 9
    Returns:
        if the address points over the matrix => returns with False
        tuple of the LEFT DIAGONAL numbers
    """
    if (i < 1) or (j < adj) or (i > max_v - adj + 1) or (j > max_h):
        return False
    out = []
    for x in range(0, adj):
        out.append(int(mx[i - 1 + x][j - 1 - x]))
    return tuple(out)


def vert(i, j):
    """ search matrix for VERTICAL adjacents on the position: (i,j)
        [1]2 3
        [4]5 6
        [7]8 9
    Returns:
        if the address points over the matrix => returns with False
        tuple of the VERTICAL numbers
    """
    if (i < 1) or (j < 1) or (i > max_v - adj + 1) or (j > max_h):
        return False
    out = []
    for x in range(0, adj):
        out.append(int(mx[i - 1 + x][j - 1]))
    return tuple(out)


def hori(i, j):
    """ search matrix for HORIZONTAL adjacents on the position: (i,j)
        [1][2][3]
        4 5 6
        7 8 9
    Returns:
        if the address points over the matrix => returns with False
        tuple of the HORIZONTAL numbers
    """
    if (i < 1) or (j < 1) or (i > max_v) or (j > max_h - adj + 1):
        return False
    out = []
    for x in range(0, adj):
        out.append(int(mx[i - 1][j - 1 + x]))
    return tuple(out)


def on_pos(i, j):
    """ search the matrix in 4 direction for adjacents
        starting from the position (i,j):
        eg: on_pos(2,3):
            right diagonal     1  2  3  4  5  6  7  8
            left diagonal      1  2 :3:-4--5] 6  7  8
            vertical           1 /2/|3|\4\ 5  6  7  8
            horizontal        /1/ 2 |3| 4 \5\ 6  7  8

        This will provide all the possible adjacents in the matrix for a loop
        If address points outside the matrix it will skipped.
    Returns:
        list of tuples of numbers
        False: if there is no numbers can be defined
    """
    on = []
    d = right_diag(i, j)
    if d:
        on.append(d)
    d = left_diag(i, j)
    if d:
        on.append(d)
    d = vert(i, j)
    if d:
        on.append(d)
    d = hori(i, j)
    if d:
        on.append(d)
    if not on:
        return False
    return on


##############################################################################


def prod(t: tuple):
    # returns the product of an number tuple
    p = 1
    for x in t:
        if x == 0:
            return 0
        p *= x
    return p


DEBUG = 0
MAX = 0
# iterating the matrix
for i in range(1, max_v):
    for j in range(1, max_h):
        # get adjacents on position
        adj_on_pos = on_pos(i, j)
        if DEBUG:
            print(f"({i:>2},{j:<2})  {adj_on_pos}")
        if adj_on_pos:
            for l in adj_on_pos:
                p = prod(l)
                if DEBUG:
                    print(f"         P = {p}")
                if p > MAX:
                    MAX = p
                    max_items = l


def join_d(d):
    return "".join([str(i) for i in d])


print(f"adjecent_num = {adj}, product{max_items} = {MAX}")
print("answer: ", join_d(max_items))

# prod (9, 9, 8, 9) = 5832 # OK

# prod (9, 8, 4, 8, 9, 4, 6, 8, 5, 9, 5, 9, 8) = 64497254400 # BAD
# 9848946859598 # NOPE


DEBUG = 1
# TRY to find the max for each dimension:
MAX = MAX_v = MAX_h = MAX_r = MAX_l = 0
num = num_v = num_h = num_r = num_l = 0
for i in range(1, max_v):
    for j in range(1, max_h):
        d = right_diag(i, j)
        if d:
            p = prod(d)
            if p > MAX_r:
                MAX_r, num_r = p, d
                if MAX_r > MAX:
                    MAX, num = MAX_r, num_r
        d = left_diag(i, j)
        if d:
            p = prod(d)
            if p > MAX_l:
                MAX_l, num_l = p, d
                if MAX_l > MAX:
                    MAX, num = MAX_l, num_l
        d = hori(i, j)
        if d:
            p = prod(d)
            if p > MAX_h:
                MAX_h, num_h = p, d
                if MAX_h > MAX:
                    MAX, num = MAX_h, num_h
        d = vert(i, j)
        if d:
            p = prod(d)
            if p > MAX_v:
                MAX_v, num_v = p, d
                if MAX_v > MAX:
                    MAX, num = MAX_v, num_v

print("")
print(f"vertical      : product{num_v} = {MAX_v:<14} <-- {join_d(num_v)}")
print(f"horizontal    : product{num_h} = {MAX_h:<14} <-- {join_d(num_h)}")
print(f"left diagonal : product{num_l} = {MAX_l:<14} <-- {join_d(num_l)}")
print(f"right diagonal: product{num_r} = {MAX_r:<14} <-- {join_d(num_r)}")
print("")
print(f"total         : product{num} = {MAX:<14} <-- {join_d(num)}")

## vertical      : product(9, 8, 4, 8, 9, 4, 6, 8, 5, 9, 5, 9, 8) = 64497254400    <-- 9848946859598    # NOPE, NOPE
## horizontal    : product(3, 6, 9, 7, 8, 1, 7, 9, 7, 7, 8, 4, 6) = 5377010688     <-- 3697817977846    # NOPE, NOPE
## left diagonal : product(5, 6, 5, 8, 9, 9, 3, 7, 8, 5, 8, 4, 8) = 20901888000    <-- 5658993785848    # NOPE, NOPE
## right diagonal: product(9, 9, 6, 5, 9, 4, 4, 7, 4, 5, 6, 7, 9) = 18517766400    <-- 9965944745679    # NOPE, NOPE
##
## total         : product(9, 8, 4, 8, 9, 4, 6, 8, 5, 9, 5, 9, 8) = 64497254400    <-- 9848946859598    # NOPE, NOPE
## [Finished in 0.4s]

# total         : product(9, 8, 4, 8, 9, 4, 6, 8, 5, 9, 5, 9, 8) = 64497254400    <-- 9 × 8 × 4 × 8 × 9 × 4 × 6 × 8 × 5 × 9 × 5 × 9 × 8      # NOPE
