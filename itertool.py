from itertools import product, permutations, combinations, combinations_with_replacement, accumulate
from itertools import groupby, count, cycle, repeat

#PRODUCTS#
#I dont really know what this does
print("Product:")
a = [1,2]
b = [3]
prod = product(a,b, repeat=2) #you can define repitions
print(list(prod))
print("\n")

#PERMUNATIONS#
print("Permunation:")
a = [1,2,3]
prem = permutations(a)
print(list(prem))
print("\n")

#COMBINATIONS#
print("Combination:")
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))
print("\n")

#ACCUMILATES#
print("Accumulate:")
a = [1, 2, 3, 4]
acc = accumulate(a) #you can make it add, subtract, multiply, etc.
print(a)
print(list(acc))
print("\n")

#GROUPBY#
print("Groupby:")
def smaller_than_3(x):
    return x < 3

a = [1,2,3,4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))
print("\n")

#COUNT, CYCLE, AND REPEAT#
for i in count(10):
    #loops inifitly
    print(i)
    if i == 15:
        break
a = [1, 2, 3, 4, 5]
for i in cycle(a):
    print(i)
    if i == 5:
        break
for i in repeat(1,4):
    print(i)