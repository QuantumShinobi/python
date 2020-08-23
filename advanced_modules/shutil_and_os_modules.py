# %%
import send2trash
import os
import shutil
f = open("practice.txt", "w+")
f.write("this is a text screen ")
f.close()

# %%
# current directory
os.getcwd()
# %%
# to list items in the current directory
os.listdir()
os.listdir(path="c:\\Users")
# %%
# to move files
# takes src and destination to move the files
shutil.move('practice.txt', "C:\\Users\\Shalini\\Desktop")
# %%
os.listdir(path="C:\\Users\\Shalini\\Desktop")

# %%
#  to delete files
#  there are 3 ways
#  1. os.unlink(path) => this deletes a file in a path
#  2. os.rmdir(path) => removes a folder
#  3. shutil.rmtree(path) => removes ALL THE FILES AND FOLDERS IN A PATH
# all of these methods are irreversible
# the files will be permanentaly deleted


# so to make it reverse
# a module called  "send2trash" is used
# with send2trash
# send2trash.send2trash
# %%
# %%
os.listdir()
# %%
shutil.move("C:\\Users\\Shalini\\Desktop\\practice.txt", os.getcwd())

# %%
send2trash.send2trash('practice.txt')
# %%
os.listdir()


# %%
# it will yield a tuple for all items in a diectory
# os.walk()
# %%
# for folder, sub_folders, files in os.walk()
# do this yourself
