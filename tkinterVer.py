# Importing the required libraries
from tkinter import *
import tkinter as tk
import datetime
import calendar
import os
import shutil


# Function creating folder named after month of the file
def createFolder(path: str, date: str):
    os.chdir(path)
    os.makedirs(date)


# Function moving the file to its designated folder
def moveFile(file_to_organize, path, folder):
    destination_folder = path + folder
    shutil.move(file_to_organize, destination_folder)


def inputObtain():
    path_to_organize = entry.get()
    list_of_files = os.listdir(path_to_organize)
    for file in list_of_files:
        path_to_file = path_to_organize + file
        create_time = os.path.getmtime(path_to_file)
        create_month = int(datetime.datetime.fromtimestamp(create_time).strftime("%m"))
        year_created = int(datetime.datetime.fromtimestamp(create_time).strftime("%Y"))
        month_name = calendar.month_name[create_month]
        new_folder_name = f"{month_name}-{year_created}"
        if not os.path.exists(path_to_organize + new_folder_name):
            createFolder(path_to_organize, new_folder_name)
            moveFile(file, path_to_organize, new_folder_name)
        else:
            moveFile(file, path_to_organize, new_folder_name)


# Function modifying the organizing regimen
# Creation date or Last modified
def byCreationDate():
    global create_time
    create_time = os.path.getctime(path_to_file)
    print(create_time)


def byLastModifiedDate():
    global create_time
    create_time = os.path.getmtime(path_to_file)
    print(create_time)


def Instructions():
    popup = tk.Toplevel()
    popup.title('Popup Window')
    popup.geometry("600x300")
    label = tk.Label(popup, text='This is where instructions should be')
    label.pack(padx=10, pady=10)


def openPopoUp():
    Instructions()


def quitProgram():
    root.destroy()


# #Listing the files on the path organizing


"""
After obtaining the necessary date information for each file
It checks if there is a folder named after the month of the file analyzing-
if there is, it moves the file into that folder. Otherwise, it creates a folder-
named the month of the file analyzing and moves the file into it.
"""

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
       command=inputObtain).place(
    x=300, y=235)
Button(root, text='How does this work?', highlightbackground="#0072ff", width=15, bd=0, font=('Times New Roman', 13,),
       bg='#b2b2b2',
       command=openPopoUp).place(
    x=510, y=305)
Button(root, text='Quit', highlightbackground="#ff0000", width=15, bd=0, font=('Times New Roman', 13,), bg='#b2b2b2',
       command=quitProgram).place(
    x=30, y=305)

# Initiating the window
root.update()
root.mainloop()
