# %%
from collections import namedtuple
from collections import defaultdict
from collections import Counter

mylist = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]
#  to get the unique objects
#  in a list
Counter(mylist)
# %%
my_list_2 = ['a', 10, 'b', 12, 'a', 10, 'b', 12, 'a', 10, 'b', 12, ]
Counter(my_list_2)


# %%

Counter('aaabbbbjjjjjjhefuhfhiwruf bhri bgib ur bg')
# %%
letters = "aaaaaaaabbbbbbbbbbccccccccccccddddddddddeeeeeeee"
# %%
c = Counter(letters)
# %%
c
# %%
c.most_common(1)
# %%
d = list(c)
# %%
d

# %%
# the default dictionary
# %%

# %%
d = {'a': 10}
# %%
d
# %%
d['a']


# %%
d[10]
# %%
d['wrong']
# %%
#   a default dictionary will assign a default value to a key
#  even if it was not created
#  hence no error will be recieved
# %%
d = defaultdict(lambda: 0)

# %%
d['ok'] = 100
# %%
d['ok']

# %%
d['no key']
# %%

# %%
d
# %%
# %%
mytuple = (10, 20, 30)
# %%
mytuple[0]
# %%
Dog = namedtuple('DOG', ['age', 'breed', 'name'])
# %%
sam = Dog(age=5, breed="husk", name="sam")
# %%
sam
# %%
sam.age
# %%
sam.name
# %%
sam.name
# %%
sam[1]
# %%
sam[0]
# %%
