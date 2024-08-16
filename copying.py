import copy

org = [0, 1, 2, 3, 4]
cpy = copy.copy(org) #don't change the other vairable
cpy[0] = -10
print(cpy)
print(org)

"""This is useless (kinda)"""