

"""basic parameter practice"""
def foo(a, b, c, d=4): #d does not need to be specified
    print(a, b, c, d)

foo(1, 2, 3)


"""If marked with one stars, any number of positional aurguments"""
"""If marked with two stars, you can pass any number of keyword arguments"""
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, 6, seven=7, eight=8)


"""Use lists"""
def foo(a, b, c):
    print(a, b, c)
my_list = [0, 1, 2] #tuples and dictionaries can be used too
foo(*my_list)




"""*****<--- this stuff"""
#multiply
a = 4 * 2
print(a)

#square
a = 4 ** 2
print(a)

#lists
a = ["a"] * 10
print(a)

#strings
a = "a" * 10
print(a)