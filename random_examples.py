import random
import secrets
import numpy as np

#random float
print("random.random")
a = random.random()
print(a)
print("\n")

#random anythin in range of these numbers
print("random.uniform")
a = random.uniform(1, 10)
print(a)
print("\n")

print("random.randint")
a = random.randint(1, 10)
print(a)
print("\n")

print("random.normalvariate")
a = random.normalvariate(0, 1)
print(a)
print("\n")

print("random.choice")
mylist = list("ABCDEFGHIJK")
a = random.choice(mylist)
print(a)
print("\n")

print("random.shuffle")
mylist = list("ABCDEFGHIJK")
random.shuffle(mylist)
print(mylist)
print("\n")

print("random.seed")
random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

print("\n")


#secrets shhhhh...
print("secrets.randbelow")
a = secrets.randbelow(10)
print(a)
print("\n")
print("secrets.randbits")
a = secrets.randbits(4) #no value would be needed
print(a)
print("\n")

print("secrets.choice")
mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)

#numpy

print("Numpy stuff")
#create arrays
a = np.random.rand(0, 10, 5) #<-- you can use multiple items for the array
print(a)