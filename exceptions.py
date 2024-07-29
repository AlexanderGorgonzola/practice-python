#CREATE EXCEPTIONS#
print("Creating exceptions:")
x = 5
#One way
if x < 0:
    raise Exception("Vairable should be positive")
#Second way
assert (x>=0), "Vairable should be positive"
print("\n")

#TRY, EXCEPT#
print("Try, except methods:")
try:
    a = 5 / 0
    b = a + 2
except ZeroDivisionError: #you can also do except Exxception as e to know specific error
    print("Cannot divide by zero you monkey")
except TypeError as e:
    print(e)
else:
    print("All good")
finally:
    print("Its morbin time")
#you can try multiple statemnts, and specify the error
print("\n")

#ERROR CLASSES#
print("Defining error classes:")
class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high ;(")
    elif x < 10:
        raise ValueTooSmallError("Value is too small *_*")
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)