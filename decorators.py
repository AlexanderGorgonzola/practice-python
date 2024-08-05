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