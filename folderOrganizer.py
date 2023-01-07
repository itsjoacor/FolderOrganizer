import datetime
import calendar
import os
import shutil

# falta organizar y definierlo en clases para mas organizacion. Pero hasta que no ande no se hace jajaja XD.
# Counters and accessories- contadores y accesorios
position = 0
x = 0

# Path to organize - directorio a organizar
path_to_organize = "/home/joaquin/Documents/Downloading/"

# Files to organize- listando archivos en el directorio a organizar.
list_of_files = os.listdir(path_to_organize)
print(f"This are the files to be organized {list_of_files} ")
file_name = os.path.basename("/home/joaquin/Documents/Downloading/{}".format(list_of_files[position]))

# Path to file - accediendo al archivo segun posicion en el listado
path_to_file = "/home/joaquin/Documents/Downloading/{}".format(list_of_files[position])

# Extracting month of the file -extrayendo el mes del archivo para saber que carpeta crear
create_time = os.path.getctime(path_to_file)
create_date = str(datetime.datetime.fromtimestamp(create_time).strftime("%Y%m%d%H%M%S"))
extract_month = str(create_date)
month_int = int(extract_month[4:6])
month_of_file = (calendar.month_name[month_int])
month_list = list(calendar.month_name)

# Moving paths - carpeta a crear - archivo a mover - destino donde se mueve el "source_file"- respectivo orden
new_folder = "/home/joaquin/Documents/Downloading/{}".format(month_of_file)
source_file = "/home/joaquin/Documents/Downloading/{}".format(list_of_files[position])
destination_folder = new_folder

# Extracting file type- extrayendo el tipo del archivo
_, file_extension = os.path.splitext("/home/joaquin/Documents/Downloading/{}".format(list_of_files[position]))


# Actions to be made - que haceres

# creando carpeta y moviendo archivo del mismo mes a esa carpeta
def creatingAndFolderMoving():
    global new_folder, position, destination_folder, source_file
    global position
    os.makedirs(new_folder)
    shutil.move(source_file, destination_folder)
    print("folder moved correctly")

# solo mueve el archivo a la carpeta (la carpeta del mes fue creada ya por otro arvhico previamente)
def onlyFolderMoving():
    global source_file, destination_folder
    shutil.move(source_file, destination_folder)

    
#retorna si el tipo de archivo es una carpeta o no
def folderType():
    if file_extension == "":
        return True
    else:
        return

# pruebas a ignorar
# def isItMonthFolder():
#     global month_list, x
#     month_list = list(calendar.month_name)
#     del month_list[0]
#     for f in range(0, len(list_of_files)):
#         if file_name == month_list[x] and folderType():
#             x += 1
#             print("1")
#             return True

#         else:
#             return




for month in range(0, len(month_list)):
    if not "December":
        print("It is not on the list")
        break
    else:
        print("It is on the list")
        
        
        
        
        
        
# pruebas de como acceder a los archivos en la lista y crear y mover etc.
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
