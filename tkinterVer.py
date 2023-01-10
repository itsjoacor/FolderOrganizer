# Importing the required libraries
from tkinter import *
import tkinter as tk
import datetime
import calendar
import os
import shutil


# Function creating folder named after month of the file
# Crea carpeta con nombre del mes del archivo
def createFolder(path, date):
    os.chdir(path)
    os.makedirs(date)


# Function moving the file to its designated folder
# mueve el archivo seleecionado a su carpeta mensual
def moveFile(file_to_organize, path, folder):
    destination_folder = path + folder
    shutil.move(file_to_organize, destination_folder)

# corre el programa
def runningProgram():
    path_to_organize = entry.get()
    list_of_files = os.listdir(path_to_organize)
    for file in list_of_files:
        path_to_file = path_to_organize + file
        create_time = os.path.getctime(path_to_file)
        create_month = int(datetime.datetime.fromtimestamp(create_time).strftime("%m"))
        year_created = int(datetime.datetime.fromtimestamp(create_time).strftime("%Y"))
        month_name = calendar.month_name[create_month]
        new_folder_name = f"{month_name}-{year_created}"
        if not os.path.exists(path_to_organize + new_folder_name):
            createFolder(path_to_organize, new_folder_name)
            moveFile(file, path_to_organize, new_folder_name)
        else:
            moveFile(file, path_to_organize, new_folder_name)
    successfulProgram()


# Function modifying the organizing regimen
# deberia modificar el tipo de organizacion que se quiere - fecha de creacion
def byCreationDate():
    create_time = os.path.getctime(path_to_file)

# deberia modificar el tipo de organizacion que se quiere - fecha de ultima modificacion
def byLastModifiedDate():
    create_time = os.path.getmtime(path_to_file)
    
 """
 La idea es que el usuario tambien pueda decidir el tipo de organizacion que quiera, si por creacion del archivo o por ultima modificacion.
 Esto se aplicacria a todos los archivos en el path a organizar.
 Lo que harian estos botones es cambiar el contenido de la variable create_time y asi modificarlo a getmtime o getctime, respectivamente.
 el problema es que no puedo lograr llamar la variable por fuera de la funcion, no se como hacer eso en una funcion o vice versa.
 """

# Pop-up con manual de instrucciones
def Instructions():
    popup = tk.Toplevel()
    popup.title('Popup Window')
    popup.geometry("600x300")
    label = tk.Label(popup, text='This is where instructions should be')
    label.pack(padx=10, pady=10)

# Inicia el pop-up
def openPopoUp():
    Instructions()

# Finaliza con el programa en caso de abortar
def quitProgram():
    root.destroy()

# Pop-up con mensaje de programa ejecutado correctamente
def successfulProgram():
    suc_prog = tk.Toplevel()
    suc_prog.title('Popup Window')
    suc_prog.geometry("300x100")
    label_suc = tk.Label(suc_prog, text='Program run successfully!')
    label_suc.pack(padx=10, pady=10)





# Inicializazcion ventana tkinter
root = Tk()
root.title("Folder Organizer Program")
root.geometry('700x350')
root.resizable(False, False)
root.config(bg='#b2b2b2')

# Window body
Label(root, text='Welcome to the Folder Organizer', font=('Calibre', 15), anchor="center", bg='#b2b2b2',
      wraplength=300).place(x=240, y=10)
Button(root, text='Organize by last modification date', highlightbackground="#000000", width=30,
       font=('Times New Roman', 13), bg='#FFF1F0',
       command=byCreationDate).place(
    x=35, y=105)
Button(root, text='Organize by creation date', highlightbackground="#000000", width=30, font=('Times New Roman', 13),
       bg='#FFF1F0',
       command=byLastModifiedDate).place(
    x=370, y=105)
Label(root, text='Insert the path you want to organize below: ', justify="right", font=('Comic Sans bold', 10),
      bg='#b2b2b2',
      wraplength=300).place(x=205, y=180)

entry = Entry(root, width=40, highlightbackground="#000000", font=('Times New Roman', 13), bg="#FFF1F0")
entry.place(
    x=165, y=200)
Button(root, text='Submit', highlightbackground="#000000", width=8, font=('Times New Roman', 13), bg='#FFF1F0',
       command=runningProgram).place(
    x=300, y=235)
Button(root, text='How does this work?', highlightbackground="#0072ff", width=15, bd=0, font=('Times New Roman', 13,),
       bg='#b2b2b2',
       command=openPopoUp).place(
    x=510, y=305)
Button(root, text='Quit', highlightbackground="#ff0000", width=15, bd=0, font=('Times New Roman', 13,), bg='#b2b2b2',
       command=quitProgram).place(
    x=30, y=305)

# Correr ventana tkinter
root.update()
root.mainloop()
