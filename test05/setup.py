# coding: utf-8

from cx_Freeze import setup, Executable
import sys
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\tester\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\tester\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable('test5_check_correct_file_on_distrx64.py', base = base)]

excludes = ['unicodedata', 'logging', 'unittest', 'email', 'html', 'http', 'urllib',
            'xml', 'bz2']


includes = ["atexit", "re"]

build_exe_options = {"packages": ["os", "tkinter", "pywinauto", "time", "datetime", "winreg", "win32api"], "includes": includes, "include_files": ["C:/Users/tester/AppData/Local/Programs/Python/Python36-32/DLLs/tcl86t.dll", "C:/Users/tester/AppData/Local/Programs/Python/Python36-32/DLLs/tk86t.dll", "C:/libusb/libusb-1.0.dll"]}

setup(
    name = "Test5",
    version = "1.2",
    description = "Проверка корректности версий в установленном продукте Аккорд Win",
    options = {"build_exe": build_exe_options},
    executables = executables
   )
