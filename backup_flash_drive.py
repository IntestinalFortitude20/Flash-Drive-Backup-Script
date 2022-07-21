import os
import shutil
import sys
import ctypes
import pathlib
from datetime import date


#Create string for backup folder path (used for managing oldest folders)
backup_path = "C:/Users/pruck/OneDrive/Desktop/Flash_Drive_Backups/"


#Assign source directory using os.chdir
try:
    src_dir = os.chdir("D:/")
except:
    print("Drive not found.  Trying again...")
    
    try:
        src_dir = os.chdir("E:/")
        print("Drive found!  SUCCESS!")
    except:
        print("Drive not found.  Cancelling operation.")
        attempt_2 = False
        exit(0)


#Create date format for naming backup folders
today = date.today()
date_format = today.strftime("_%m_%d_%Y")


#Create string for destination directory (not created yet)
dst_dir = backup_path + "Flash_Drive_Backup" + date_format + "/"


#List out files/directories on removeable drive
sub_dir_list = (os.listdir(src_dir))


#Loop through sub-directories in source folder
for sub_dir in sub_dir_list:
    if "My Files" in sub_dir:
        try:
            shutil.copytree(sub_dir, dst_dir) # <<< destination directory created here
        except:
            print("Backup already exists.  No action taken.")


#List out backups for comparing creation dates
list_of_backups = os.listdir(backup_path)
#print("List of backups: ", end="\t")
#print(list_of_backups)


#Get number of backups
num_backups = 0
for b in list_of_backups: num_backups += 1


#Delete oldest backup
if num_backups > 3:
    oldest_backup = ""

    for backup in list_of_backups:
        current_backup = backup_path + backup + "/"

        if oldest_backup == "":
            oldest_backup = current_backup
        elif os.path.getctime(oldest_backup) > os.path.getctime(current_backup):
            oldest_backup = current_backup

    print("Oldest backup: " + oldest_backup)
    print()
    shutil.rmtree(oldest_backup)
    print("Removed oldest backup.")


#Wrapping things up
print()
print("All operations completed successfully.")