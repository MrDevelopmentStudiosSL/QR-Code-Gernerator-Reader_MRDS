import qrcode
from pyzbar import pyzbar
from PIL import Image
from tkinter import messagebox
import os

def gen():
    try:
        os.system('cls')

        print('<----- QR Code Generation Wizard ----->\n')
        data = input('Enter the "Data" or "Values"   : ')
        while len(data) == 0:
            data = input('Enter the "Data" or "Values"   : ')
        print('')
        border = input('Enter the "Boder Width"      : ')
        while len(border) == 0:
            border = input('Enter the "Boder Width"      : ')
        print('')
        box = input('Enter the "Box size"            : ')
        while len(box) == 0:
            box = input('Enter the "Box size"            : ')
        print('')
        fill = input('Enter the "Fill Colour"        : ')
        while len(fill) == 0:
            fill = input('Enter the "Fill Colour"        : ')
        print('')
        back = input('Enter the "Back Colour"        : ')
        while len(back) == 0:
            back = input('Enter the "Back Colour"        : ')
        print('')
        name = input('Enter the "Output Name"        :')
        while len(name) == 0:
            name = input('Enter the "Output Name"        :')
            
        qr = qrcode.QRCode(border=(border), box_size=(box))
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=(fill), back_color=(back))
        img.save(name)
        print('\nQR Code was succesfuly created\n')
        input("\nPress Enter to Return to Main Menu [ENTER]")
        os.system('cls')

    except:
        messagebox.showerror('QR Error', 'Somthing Went Wrong')
        os.system('cls')

def read():
    try:
        os.system('cls')
        print('<----- QR Code Reading Wizard ----->\n')
        file = input('Enter the QR Code File Name or Location : ')
        while len(file) == 0:
            file = input('Enter the QR Code File Name or Location : ')
        print('')

        img = Image.open(file)
        output = pyzbar.decode(img)

        print("Data & Informations - ",output[0][0].decode('utf-8'),'\n')

        print('\nQR Code was succesfuly readed. No errors found.\n')
        input("\nPress Enter to Return to Main Menu [ENTER]")
        os.system('cls')


    except:
        messagebox.showerror('QR Error', 'Somthing Went Wrong')
        os.system('cls')



while True:
    try:
        print('''
|-------------------------------------------------------------------------------------------|
|                                                                                           |
|                               QR Code Reader & Generator                                  |
|                                                                                           |
|                 QR_CODE_GENERATOR_&_READER (C) 2022 MR Development Studio                 |
|                                                                                           |
|-------------------------------------------------------------------------------------------|
''')
        print('''
< Options >

[1]. Generate a QR CODE
[2]. Read a QR Code
[3]. Help
''')
        opt = (input('Enter the Option Number Here : '))
        while len(opt) == 0:
            opt = (input('Enter the Option Number Here : '))

        if opt == '1':
            gen()
            
        elif opt == '2':
            read()

        elif opt == '3':
            print('''
< Help >

You Can use this software to create and read qr codes.
Developed & Published by MR Development Studios''')

        else:
            os.system('cls')

    except:
        messagebox.showerror('QR Error','Somthing Went Wrong')
        os.system('cls')

# MR Development Studios


