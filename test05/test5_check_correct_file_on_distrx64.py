from pywinauto import Application
from win32api import GetFileVersionInfo, HIWORD, LOWORD
import os
import time
import datetime
from tkinter import *


main = Tk()
result = 1

#Создание функций
def gettime():
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    date = str(day) + "/" + str(month) + "/" + str(year) + " " + str(hour) + ":" + str(minute) + ":" + str(second)
    dt = datetime.datetime.strptime(date, '%d/%m/%Y %H:%M:%S')
    date = dt.strftime('%d/%m/%Y %H:%M:%S')
    return date

def verfile(file):
    
    
    return testver


def button_clicked():
    sys.exit()

#Получение даты
day = datetime.datetime.now().day
month = datetime.datetime.now().month
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
date = str(day) + str(month) + "_" + str(hour) +  str(minute)
dt = datetime.datetime.strptime(date, "%d%m_%H%M")
date = dt.strftime("%d%m_%H%M")


#Создание и старт записи в файл
path = "c:\\testlog\\test5_" + date  + ".txt"
f = open(path, "tw", encoding='utf-8')
f.write("_________________________________Начало записи лога_________________________________\n\n")
datestart = datetime.datetime.now()
timestart = gettime()
f.write("Проверка началась в " + timestart + "\n\n")


datefile = time.ctime(os.path.getctime("c:\\in\\acc.exe"))#получение даты создания
f.write("Получена дата " + datefile + "\n")
info = win32api.GetFileVersionInfo("c:\\in\\acc.exe", "\\")
ms = info['FileVersionMS']
ls = info['FileVersionLS']
ver = str(HIWORD (ms)) + "." + str(LOWORD (ms)) + "." + str(HIWORD (ls)) + "." + str(LOWORD (ls))
f.write("Получена версия файла " + ver +"\n")
f.write("Тест получения информации из файла прошёл успешно\n\n")
filesize = os.stat("C:\\in\\acc.exe")
filesize = filesize.st_size / 1000
f.write("Получен размер файла " + filesize +"\n")

#Завершение работы
if result == 1:
    f.write("Итоговое тестирование завершилось успешно \n")
    print ("В результате проверки ошибок не обнаружено")

    button = Button(main,
                        width=35, height=20, compound=CENTER,
                        bg="green", command=button_clicked)
else:
    f.write("Итоговое тестирование завершилось неудачно \n")
    print ("В результате проверки были обнаружены ошибки")
    button = Button(main,
                        width=35, height=20, compound=CENTER,
                        bg="red", command=button_clicked)

datefinish = datetime.datetime.now()
timefinish = gettime()
f.write("Проверка завершилась в " + timefinish + "\n")
de = datefinish - datestart
de = str(de.seconds)
f.write("Общее время составило " + de + " секунд\n" )
print("Общее время составило " + de + " секунд")
f.write("_________________________________Конец записи лога_________________________________\n\n")
f.close()