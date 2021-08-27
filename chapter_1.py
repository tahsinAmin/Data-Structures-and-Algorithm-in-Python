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

# C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.
"""
print([chr(a) for a in range(ord('a'), ord('z') + 1)])
"""

# C-1.20 Python’s random module includes a function shuffle(data) that accepts a
# list of elements and randomly reorders the elements so that each possible order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuffle function.
"""
def my_shuffle(data):
	from random import randint
	for i in range(len(data)):
		m = randint(0, len(data) - 1)
		n = randint(0, len(data) - 1)
		data[m], data[n] = data[n], data[m]

if __name__ == '__main__':
	a = [i for i in range(10)]
	print('initial list:',a)
	
	for i in range(10):
		my_shuffle(a)
		print('shuffled:',a)
"""

# C-1.21 Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D)
"""
a=[]
while True:
	try:
		n = input()
		a.append(n)
	except(EOFError):
		break
	
a.reverse()
[print(i) for i in a]
"""

# C-1.22 Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.
"""
def dots(a,b):
	assert len(a) == len(b)
	return [a[i] * b[i] for i in range(len(a))]
	
a = [1,2,3]
b = [1,2,3]
c = dots(a,b)
print(c)
"""

# C-1.23 Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# “Don’t try buffer overflow attacks in Python!"
"""
a = [1,2,3]
try:
	a[len(a)] = 5
except IndexError as error:
	print("Don’t try buffer overflow attacks in Python!")
print(a)
"""

# C-1.24 Write a short Python function that counts the number of vowels in a given
# character string.
"""
s='Encyclopedia'
c=0

for i in s:
	c+= 1 if i in 'AEIOUaeiou' else 0

print(c)
"""

# C-1.25 Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For example, if given the string "Let s try, Mike.", this function would return
# "Lets try Mike"
"""
def removePunct(s):
	return ''.join(x for x in s if x.isspace() or x.isalnum())

s= "I'd have done it by now!!"
print(removePunct(s))
"""

# C-1.26 Write a short program that takes as input three integers, a, b, and c, from
# the console and determines if they can be used in a correct arithmetic
# formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”
"""
if __name__ == '__main__':
	s = input().split()
	a, b, c = (int(i) for i in s)
	print('Is {} + {} = {}?'.format(a, b, c), a + b == c)
	print('Is {} = {} - {}?'.format(a, b, c), a == b - c)
	print('Is {} = {} * {}?'.format(a, b, c), a == b * c)
"""

# C-1.28 The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is defined as
# v = # p # v# p# 1 +v# p# 2 +···+v# p# n .
# For the special case of p = 2, this results in the traditional Euclidean
# norm, which represents the length of the vector. For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a
# Euclidean norm of √
# 42 +32 = √16+9 = √
# 25 = 5. Give an implementation of a function named norm such that norm(v, p) returns the p-norm
# value of v and norm(v) returns the Euclidean norm of v. You may assume
# that v is a list of numbers.

"""
def norm(v,p):
	s = 0
	for i in v:
		s+= i**p
		
	print(s**(1/p))
		
		
norm([3,4],2)
"""

# P-1.29 Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.
#  Example: https://www.youtube.com/watch?v=QI9EczPQzPQ
"""if __name__ == '__main__':
    from itertools import permutations
    s = 'catdog'
    for i in range(len(s)):
        for x in permutations(s, i + 1):
            print(''.join(x))"""

# P-1.30 Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.
"""
from math import floor, log2

if __name__ == '__main__':
	n = int(input("input an integer: \n"))
	assert n > 2
	print("Need {} times to divide".format(int(floor(log2(n)))))
"""

# P-1.31 Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible.
"""
charge, given = map(float, input().split())
# print(charge, given)
dif = (given - charge)
if dif == int(dif):
	print("yes")
	print("Change:", dif)
else: 
	print("no")
	refined = int((dif - int(dif))*100)
	print("Change: %s Taka & %s Paisha" %(int(dif),refined))

"""


"""
from random import randrange
list_of_typos = [
	"Ai will never spam my friends again.",
	"I well never spam my friends again.",
	"I will nver spam my friends again.",
	"I will never spem my friends again.",
	"I will never spam mi friends again.",
	"I will never spam my frends again.",
	"I will never spam my friends agen.",
	"I will never spam my friends again.",
	]
	
[print(list_of_typos[randrange(0,8)]) for i in range(100)]
"""


# file:///C:/Users/User/Downloads/Documents/Data%20Structures%20and%20Algorithms%20in%20Python%20(%20PDFDrive%20).pdf
# https://github.com/findmyway/Data-Structures-and-Algorithms-in-Python/tree/master/ch1
