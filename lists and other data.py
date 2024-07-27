from collections import Counter

#a counter shows how many times an item occurs
a = "aaaaaaabbbbbcccc"
my_counter = Counter(a)
print(my_counter) #shows dictionary
print(my_counter.keys()) #shows all the keys
print(my_counter.values()) #shows all values
print(my_counter.most_common(1)) #shows the most common elemnt