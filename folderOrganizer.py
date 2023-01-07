import datetime
import calendar
import os
import shutil

# Counters and accessories
position = 0
x = 0
# Path to organize
path_to_organize = "/home/joaquin/Documents/Downloading/"

# Files to organize
list_of_files = os.listdir(path_to_organize)
print(f"This are the files to be organized {list_of_files} ")
file_name = os.path.basename("/home/joaquin/Documents/Downloading/{}".format(list_of_files[position]))

# Path to file
path_to_file = "/home/joaquin/Documents/Downloading/{}".format(list_of_files[position])

# Extracting month of the file
create_time = os.path.getctime(path_to_file)
create_date = str(datetime.datetime.fromtimestamp(create_time).strftime("%Y%m%d%H%M%S"))
extract_month = str(create_date)
month_int = int(extract_month[4:6])
month_of_file = (calendar.month_name[month_int])
month_list = list(calendar.month_name)

# Moving paths
new_folder = "/home/joaquin/Documents/Downloading/{}".format(month_of_file)
source_file = "/home/joaquin/Documents/Downloading/{}".format(list_of_files[position])
destination_folder = new_folder

# Extracting file type
_, file_extension = os.path.splitext("/home/joaquin/Documents/Downloading/{}".format(list_of_files[position]))


# Actions to be made

def creatingAndFolderMoving():
    global new_folder, position, destination_folder, source_file
    global position
    os.makedirs(new_folder)
    shutil.move(source_file, destination_folder)
    print("folder moved correctly")


def onlyFolderMoving():
    global source_file, destination_folder
    shutil.move(source_file, destination_folder)


def folderType():
    if file_extension == "":
        return True
    else:
        return


def isItMonthFolder():
    global month_list, x
    month_list = list(calendar.month_name)
    del month_list[0]
    for f in range(0, len(list_of_files)):
        if file_name == month_list[x] and folderType():
            x += 1
            print("1")
            return True

        else:
            return


# for i in list_of_files:
#     if file_name == month_of_file and folderType() == "Folder":
#         onlyFolderMoving()
#     elif new_folder:
#         onlyFolderMoving()

# for file in list_of_files:
#     if os.path.exists("/home/joaquin/Documents/Downloading/{}".format(month_of_file)) and folderType():
#         onlyFolderMoving()
#         position += 1
#     else:
#         creatingAndFolderMoving()
#         position += 1
#
#
#

for month in range(0, len(month_list)):
    if not "December":
        print("It is not on the list")
        break
    else:
        print("It is on the list")
