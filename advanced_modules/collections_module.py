# %%
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
# %%
