# generators use the yield keyword
# %%

def create_cubes(n):
    result = list()
    for x in range(n):
        result.append(x**3)
    return result


# %%


def create_cubes(n):
    for x in range(n):
        yield(x**3)


# %%
for x in create_cubes(10):
    print(x)
# %%
create_cubes(10)
# %%

list(create_cubes(10))

# %%

# %%

# %%


def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


# %%
for number in gen_fibon(10):
    print(number)
# %%


def simple_func():
    for i in range(3):
        yield i


# %%
for x in simple_func():
    print(x)
# %%
g = simple_func()
# %%
g

# %%
next(g)
# %%
# iter function - allows us to iterate through objects
# %%
s = 'hello'
# %%
for i in s:
    print(i)
# %%
# to turn some datatype into a generator
# the iter func. is used
# %%
s_iter = iter(s)

# %%
# wont work
next(s)
# %%
# but this will
next(s_iter)
# %%
