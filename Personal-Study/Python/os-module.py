import os
print(os.getcwd()) # shows us which folder are we working on
# os.chdir()  # to change directory
#print(os.listdir()) shows us what we have in folder
print(os.listdir()) # if you give a parameter inside it you can see the containers in that folder
#to read the folder's containers we can do like this
for folder in os.listdir():
    print(folder)

 #os.mkdir() we use it to create a folder   
 # to create nested folders we can use os.makedirs()
 #to delete a folder use os.rmdir()
 #if you want to delete more than one folder use os.removedirs()
 # to rename a folder use os.rename(folder old name,new name)
 # to see the folder info about last access etc. use os.stat()
 # os.walk() shows us like a tree tho folders subfolders till the last one in another
 # os.path.isfile() and os.path.isdir() if you give an argument it returns true or false 
 # os.path.splitext() returns a tuple first element shows us the path the second one shows us the extension(.exe,.doc,.py etc)


print(os.getcwd())
os.chdir(r"\Users\HP\Desktop\personal study\Personal-Study\Python\from-internet")
print(os.getcwd())
print(os.listdir())
