# %%
import shutil
import zipfile
f = open('file1.txt', 'w+')
f.write('ONE FILe')
f.close()
# %%
f2 = open('file2.txt', 'w+')
f2.write('TWO FILe')
f2.close()

# %%
# %%
zip_file = zipfile.ZipFile('zip_file.zip', 'w')
# %%
zip_file.write("file1.txt", compress_type=zipfile.ZIP_DEFLATED)
zip_file.write("file2.txt", compress_type=zipfile.ZIP_DEFLATED)
# %%
zip_file.close()

# %%
zip_obj = zipfile.ZipFile('zip_file.zip', 'r')
# %%
# for 1 file -  zip_obj.extract()
zip_obj.extractall("extracted_content")
# %%
# pwd
# %%

# %%
# to compress folders
# %%
dir_to_zip = 'd:\\Coding\\github\\python\\advanced python modules\\extracted_content'


# %%
output_filename = 'example'

# %%
shutil.make_archive(output_filename, 'zip', dir_to_zip)
# %%
shutil.unpack_archive('example.zip', 'final unzip', 'zip')
# %%
