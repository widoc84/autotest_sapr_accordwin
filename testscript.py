from pywinauto import Application
import os
import time
import datetime

try:
    app = Application().start("C:\\Accord.x64\\Aced32.exe")
    print("20 sec")
    app.window(best_match="ACED32 Редактор базы ", class_name='TMainForm').wait('visible',timeout=20)
    app.kill()
    print("Aced32 корректно открылся")
    f.write("Aced32 корректно открылся\n\n")
except:
    print("Aced32 не открылся")
    f.write("Aced32 не открылся\n\n")
    app.kill()
    result = 0
time.sleep(5)
