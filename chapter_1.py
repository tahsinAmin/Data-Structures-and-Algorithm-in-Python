# 1.1) Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.
"""
def is_multiple(n, m):
    for i in range(n):
        # print("Value of i is %d" %i)
        if (i*m) == n:
            return True
        if (i*m) > n:
            return False

n, m = list(map(int, input().split()))
flag = is_multiple(n, m)
print(flag)
"""

# 1.2) Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. <em>However, your function
# cannot use the multiplication, modulo, or division operators.</em>
"""
def is_even(n):
    return True if (-1)**n == 1 else False

n = int(input())
print(is_even(n))
"""

# 1.3) Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. <em>Do not use the built-in functions min or
# max in implementing your solution.</em>
"""
def minmax(arr):
	smallest = largest = arr[0]
	
	for i in arr:
		smallest = i if i < smallest else smallest
		largest = i if i > largest else largest
	
	return smallest, largest

arr = [7,-4,-9,10,200]
print(minmax(arr))
"""

# 1.4) Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.
"""
def square_sum_all_pos_int_smaller_than_(n):
	sum = 0
	
	for i in range(n):
		sum += i**2
	
	return sum
	
n = int(input(''))
result = square_sum_all_pos_int_smaller_than_(n)
print(result)
"""

# 1.5) Give a single command that computes the sum from Exercise R-1.4, relying
# on Python’s comprehension syntax and the built-in sum function.
"""
n = int(input(''))
result = sum([k**2 for k in range(n)])
print(result)
"""

#  1.6) Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.
# &
# 1.7) Give a single command that computes the sum from Exercise R-1.6, relying
#  on Python’s comprehension syntax and the built-in sum function.
"""
n = int(input(''))
result = sum([k**2 for k in range(n) if k%2 == 1])
print(result)
"""

# 1.8) Python allows negative integers to be used as indices into a sequence, such as a
#  string. If string s has length n, and expression s[k] is used for index
#  −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the same element?
"""
index j is n-k in order to display the same item for index k
s[k] == s[n-k]
"""
# 1.9) What parameters should be sent to the range constructor, to produce a range with
# values 50, 60, 70, 80?
"""
l = [n for n in range(50,81,10)]
print(l)
"""

#  For 1.9 to 1.11 => https://gist.github.com/vgratian/7508c636171de86e8857c4dc578ef757
# https://github.com/RichardAfolabi/Data-Structures-Algorithms-in-Python/blob/master/chp_one_python_primer.py
