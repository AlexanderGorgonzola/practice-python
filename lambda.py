from functools import reduce

#BASICS#
print("Basics:")
add10 = lambda x: x + 10 #argument: expression
#basically a function
print(add10(5))

#multiple arguemnts could be used :)
mult = lambda x, y: x * y
print(mult(2,7))
print("\n")

#SORTED#
print("Sorts:")
points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])
#you can sort it different ways using lambdas, functions, etc.
print(points2D)
print(points2D_sorted)
print("\n")

#MAPS#
print("Maps:")
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x*2, a)
print(list(b))

#same thing as that ^
c = [x*2 for x in a]
print(c)
print("\n")

#FILTER#
print("Filters:")
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2==0, a)
print(list(b))

#same thing ^
c = [x for x in a if x%2==0]
print(c)
print("\n")

#REDUCE#
#basically multiplies
print("Reduce:")
a = [1, 2, 3, 4, 5, 6]
product_a = reduce(lambda x,y: x*y, a)
print(product_a)