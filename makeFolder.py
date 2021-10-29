import os
  
folderName = input("Enter the name of the folder: ")
print(" ")
  
location = input("Enter the path where you want to create the folder: ")
print(" ")
  
path = os.path.join(location, folderName)
  

os.mkdir(path)
print("Wo hooo !!! Your Directory", "''", folderName, "''", "is created.")