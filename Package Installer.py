import os
from tkinter import messagebox

def trynow():
    try:
        os.system('pip install qrcode')
        os.system('pip install pyzbar')
        os.system('pip install pilllow')
        os.system('pip install tk')
        os.system('pip install tkinter')
        print('\n\nAll Packages are succesfully installed')

    except:
        messagebox.showerror('Package Installer',"Sorry we failed to install packages.")
try:
    os.system('pip install qrcode')
    os.system('pip install pyzbar')
    os.system('pip install pilllow')
    print('\n\nAll Packages are succesfully installed')

except:
    messagebox.showerror('Package Installer','Check your internet connection and storage capacity and try again')
    input('Press Enter to try again')
    os.system('cls')
    trynow()
