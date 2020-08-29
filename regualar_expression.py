# %%
import re
text = "The agent's phone number is 408-555-1234. Call soon !"
'phone' in text
# %%
pattern = 'phone'
# %%
re.search(pattern, text)
# %%
pattern = "NOT IN TEXT"
# %%
print(re.search(pattern, text))
# %%
match = re.search(pattern, text)
# %%
match.span()
match.end()
# %%
txt = "phone one, phone 2"
matches = re.findall('phone', txt)
# %%
matches
# %%
for m in re.finditer('phone', txt):
    print(m)
# %%
# HOW TO BUILD PATTERNS
