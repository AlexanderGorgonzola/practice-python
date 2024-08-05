import functools
#their are many types ofdecorators
#decorators can change your functions functionaloityerkjgbndjg
#tweak
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@start_end_decorator
def print_name():
    print("Nah, I'd Win")
#same thing
#print_name = start_end_decorator(print_name)
print_name()

@start_end_decorator
def add5(x):
    return x + 5
result = add5(10)
print(result)

print(help(add5))
print(add5.__name__)



def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hi fat {name}")

greet("wivchj") #erm what the sigma

#Ill find out more about this later
"""I'll be using these every once in a while""" 