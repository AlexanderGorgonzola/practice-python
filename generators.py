
import sys
"""generate things one at a time when you want them"""

def mygenerator():
    yield 3
    yield 2
    yield 1

g = mygenerator()
"""Will print its a generator object"""
print(g)

"""Will print the first thing"""
value = next(g)
print(value)
"""Will print the next thing until you hit the end"""
value = next(g)
print(value)
"""If it hits the end and you try again, you get error"""

"""Basically the sum of all of these"""
print(sum(g))

"""sorrted version"""
print(sorted(g))


"""Other stuff"""
def countdown(num):
    print("Starting...")
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

value  = next(cd)
print(next(cd))

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

"""how is this a generator"""
print(sum(firstn(10)))
print(sum(firstn_generator(10)))

print(sys.getsizeof(firstn(100000)))
print(sys.getsizeof(firstn_generator(100000)))

"""What the sigma is this word"""
def fibonacci(limit):
    """0 1 1 2 3 5 8 13 ... huh"""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
        """Oh my skib this is a sequence"""
fib = fibonacci(20)
for i in fib:
    print(i)

"""I never want to see this"""
"""The generator will save money"""
mygenerator_thing = (i for i in range(10) if i % 2 == 0)
print(mygenerator_thing)
mylist_thing = [i for i in range(10) if i % 2 == 0]
print(mylist_thing)