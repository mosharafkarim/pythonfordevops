import os

folders = input("Put the folder name to get files from this folder: ").split()

for folder in folders :

    try :
        files = os.listdir(folder)
    except FileNotFoundError :
        print("This folder doen't exist, Please put right folder name")
        break
    except PermissionError :
        print("You don't have permission to view files in the folder: ", folder)
        break

    print("---------list of files/folders in folder:", folder)

    for file in files :
        print(file)
