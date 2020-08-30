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
#  CHARATER IDENTIFIERS
# CHARACTER     DESCRIPTION     EXAMPLE         EXAMPLE_MATCH
# \d            A digit         file_\d\d       file_25
# \w            Alpha numeric   \w-\w\w\w       A-b_1
# \s            Whitespace      a\sb\sc         a b c
# \D            Non Digit       \D\D\D          ABC
# \W         Non alpha numberic \W\W\W\W        +-*=
# \S         Non whitespace     \S\S\S          yyOy

# %%
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
# %%
phone
# %%
phone.group()
# %%
# USING QUANTIFIERS TO WRITE SMARTER CODE
# CHARACTER         DESCRIPTION          EXAMPLE        EG. MATCH
#   +          occurs 1 or more times    VER \w-\w+     VER A-b1_1
#  {3}      occurs 3 times only         \D{3}           ABD
#  {2, 4}   occurs 2 to 4 times         \d{2, 4}        123
# {3, }     occurs 3 times or more      \w{3}           anycharfjkr
#  *        occurs 0 or more times      ABC*            AACCC
#  ?        Once or none                plurals?        plural
# %%
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)

# %%
# compiles a regular expression into a normal expression
phone_patterns = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# %%
results = re.search(phone_patterns, text)

# %%
results.group()
# %%
for i in results.group(1):
    print(type(i))

# %%
