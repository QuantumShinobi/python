string = "      Hello world       "
sub_str = string[::-1]
string = string.strip()
print(string.lower().find('h'))
print(string.count('a'))
string.replace("world", "universe")
print(string)

my_str = "hi how are you ?"
lst = my_str.split()
new_str = " ".join(lst)
print(lst)
print(new_str)
