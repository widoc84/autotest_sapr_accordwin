# coding: utf-8

from cx_Freeze import setup, Executable
import sys
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\tester\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\tester\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable('test.py', base = base)]

excludes = ['unicodedata', 'logging', 'unittest', 'email', 'html', 'http', 'urllib',
            'xml', 'bz2']


includes = ["atexit", "re"]

build_exe_options = {"packages": ["os", "tkinter", "usb", "usb.backend.libusb1"], "includes": includes, "include_files": ["C:/Users/tester/AppData/Local/Programs/Python/Python36-32/DLLs/tcl86t.dll", "C:/Users/tester/AppData/Local/Programs/Python/Python36-32/DLLs/tk86t.dll", "C:/libusb/libusb-1.0.dll"]}

setup(
    name = "testing",
    version = "1.0",
    description = "Testing of tkinter",
    options = {"build_exe": build_exe_options},
    executables = executables
   )