from collections import Counter, namedtuple, OrderedDict
from collections import defaultdict, deque
#COUNTERS#
#a counter shows how many times an item occurs
print("Counters:")
a = "aaaaaaabbbbbcccc"
my_counter = Counter(a)
print(my_counter) #shows dictionary
print(my_counter.keys()) #shows all the keys
print(my_counter.values()) #shows all values
print(my_counter.most_common(1)) #shows the most common elemnt
print(list(my_counter.elements())) #seperates the counter into a list
print("\n")

#NAMED TUPLES#
#I could use this for game tests later :)
print("Named Tuples")
Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt)
print("\n")

#ORDEREDDICTS#
#this has become obsolete
print("Ordered Dictionaries")
ordered_dict = OrderedDict()
#append things in here
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
print(ordered_dict)
print("\n")

#DEFAULTDICTS#
print("Defualt Dictionaries")
d = defaultdict(int) #int is default value
d["a"] = 1
d["b"] = 2
#this will print the value
print(d["a"])
#this will return default value
print(d["c"])
print("\n")

#DEQUES#
print("Deques:")
d = deque()
d.append(1)
d.append(2)
d.appendleft(3) #appends at the left
print(d)
d.pop() #manually removes last element unless specified
print(d)

#other functions
#d.extend([4, 5, 6])
#d.clear()
#d.popleft()
