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

# 1.10) What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
"""print([n for n in range(8,-9,-2)])"""

# 1.11) Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""
lst = [2**n for n in range(0, 9)]
print(lst)
"""

# 1.12 Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module in-
# cludes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.
"""
from random import choice, randrange

print(randrange(5,25,5))
# l = [5, 10, 15, 20, 25]
# print(choice(l))
"""

# C-1.13 Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.
"""
function(list1):
	list2 = []
	for each item, i in list1:
		list2.append(list1[i])
	
	return list2
	**Now I need to check witgh the real one

---

list1.reverse()
print(list1)
"""

# C-1.14 Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.
"""
def product_odd(l):
    n = len(l)
    for i in range(n):
    	for j in range(n):
    		if (i != j and i*j % 2 == 1):
    			yield(i,j)
    			# print("Pair for", i, j)
    		j+=1

l = [0, 1, 2, 3, 4,5,6,7,8,9,10]
gen = product_odd(l)
for item in gen:
	print(item)
"""

# C-1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).
"""
def all_unique(array):
    number_set = set()
    for number in array:
        if number in number_set: return False
        else: number_set.add(number)
    return True

data = [1,2,3,4,5,6]; print (all_unique(data))
data = [1,2,3,3,5,6]; print (all_unique(data))
data = []; print (all_unique(data))
"""

# C-1.16 In our implementation of the scale function (page 25), the body of the loop
# executes the command data[j] = factor. We have discussed that numeric
# types are immutable, and that use of the = operator in this context causes
# the creation of a new instance (not the mutation of an existing instance).
# How is it still possible, then, that our implementation of scale changes the
# actual parameter sent by the caller?
"""print('\nLists are mutable, so what changes in the list are the references to new, immutable objects.\n\nIn other words, scaling creates a new object, but its reference is stored in the original list structure\n')"""

# C-1.17 Had we implemented the scale function (page 25) as follows, does it work properly?
# def scale(data, factor):
# for val in data:
# val = factor
# Explain why or why not
"""
def scale(data, factor):
    for val in data:
        val *= factor
print('Bad scaling')

data = [1,2,3,4,5]; print (data)
scale(data, 5); print (data)

def realscale(data, factor):
    #data*=factor #This will concatenate the array with itself multiple times!  
    for i in range (len(data)):
        data[i]*=factor

print ('\nGood scaling')
data = [1,2,3,4,5]; print (data)
realscale(data, 5); print (data)
"""

# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
"""
print([a * (a + 1) for a in range(10)])
"""

# https://github.com/findmyway/Data-Structures-and-Algorithms-in-Python/tree/master/ch1
# https://github.com/wdlcameron/Solutions-to-Data-Structures-and-Algorithms-in-Python/blob/master/Chapter%201%20Exercises.ipynb
# https://github.com/RichardAfolabi/Data-Structures-Algorithms-in-Python/blob/master/chp_one_python_primer.py
