#!/bin/python3
import os
import time


DAYS = 1
FOLDERS = [
    "/home/pi/Pictures/",
    # "/home/pi"
]

TOTAL_DELETED_SIZE = 0
TOTAL_DELETED_FILES = 0
TOTAL_DELETED_DIRS = 0

nowTime = time.time()  # time in seconds
ageTime = nowTime - 60*60*24*DAYS


def delete_old_files(folders):
    global TOTAL_DELETED_FILES
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folders):
        for file in files:
            fileName = os.path.join(path, file)     # get full path for file
            fileTime = os.path.getmtime(fileName)
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile
                TOTAL_DELETED_FILES += 1            # count sum size of files
                os.remove(fileName)                 # delete file


def delete_empty_dirs(folders):
    global TOTAL_DELETED_DIRS
    empty_folders_in_this_run = 0
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files) and (path not in FOLDERS):
            TOTAL_DELETED_DIRS += 1
            empty_folders_in_this_run += 1
            os.rmdir(path)
    if empty_folders_in_this_run > 0:
        delete_empty_dirs(folder)


# ===================== MAIN =====================
starttime = time.asctime()
for folder in FOLDERS:
    delete_old_files(folder)
    delete_empty_dirs(folder)
finishtime = time.asctime()
# ===================== MAIN =====================


print("===================== STATISTIC =====================")

print("START TIME:               " +
      str(starttime))
print("TOTAL SAVED SIZE:         " +
      str(int(TOTAL_DELETED_SIZE/1024/1024/1024)) + "MB")
print("TOTAL DELETED FILES:      " +
      str(TOTAL_DELETED_FILES))
print("TOTAL DELETED EMPTY DIRS: " +
      str(TOTAL_DELETED_DIRS))
print("FINISH TIME:              " +
      str(finishtime))

# import glob

# pattern = "/home/pi/*.log"
# files = glob.glob(pattern)
# for file in files:
#    os.remove(file)
