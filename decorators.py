"""
how to make custom decorators 
how to use them 
"""


def func():
    return 1


func


def hello():
    return "Hello!"


greet = hello
greet()
del hello
# hello()
greet()


def hello(name="Jose"):
    print(f"The Hello func has been executed")

    def greet():
        return '\t This is the greet function inside hello function'

    def welcome():
        return '\t This is the welcome function inside hello function'

    print("I am going to return a function")
    if name.lower() == "jose":
        return greet
    else:
        return welcome


hello()

hello()
my_new_func = hello("JOse")
print(my_new_func())


def cool():
    def supercool():
        return "I am very cool"
    return supercool()


func = cool

func()

# building a decorator

# %%


def hello():
    return "Hi JOSE"


def other(some_def_func):
    print("Some  other code rubns here")
    print(some_def_func())


other(hello)

# %%
