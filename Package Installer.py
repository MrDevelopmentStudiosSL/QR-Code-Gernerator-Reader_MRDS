import os

def trynow():
    try:
        os.system('pip install qrcode')
        os.system('pip install pyzbar')
        os.system('pip install pilllow')
        os.system('pip install tk')
        print('\n\nAll Packages are succesfully installed')
        input('Press Enter to Exit [ENTER]')

    except:
        print('Somthing Went Wrong')
try:
    os.system('pip install qrcode')
    os.system('pip install pyzbar')
    os.system('pip install pilllow')
    os.system('pip install tk')
    print('\n\nAll Packages are succesfully installed')
    input('Press Enter to Exit [ENTER]')

except:
    print('Somthing Went Wrong')
    input('Press Enter to try again')
    os.system('cls')
    trynow()
