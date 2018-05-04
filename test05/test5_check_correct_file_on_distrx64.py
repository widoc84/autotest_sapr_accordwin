from pywinauto import Application
import pywinauto
import time
import os
import datetime
import winreg
from win32api import GetFileVersionInfo, HIWORD, LOWORD
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
    return date  #Функция получения текущего времени


def button_clicked():
    sys.exit()

def getver(file):
    info = GetFileVersionInfo(file ,"\\")
    ms = info['FileVersionMS']
    ls = info['FileVersionLS']
    vertest = str(HIWORD (ms)) + "." + str(LOWORD (ms)) + "." + str(HIWORD (ls)) + "." + str(LOWORD (ls))
    return vertest  #Функция получения версии файла

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

#Получение данных из файла
f.write("___Получение данных из файла___\n")
try:
    datefile = time.ctime(os.path.getctime("c:\\in\\acc.exe"))
    f.write("Получена дата " + datefile + "\n")
    ver = getver("c:\\in\\acc.exe")
    f.write("Получена версия файла " + ver +"\n")
    filesize = os.stat("C:\\in\\acc.exe")
    filesize = str(int(filesize.st_size / 1000))
    f.write("Получен размер файла " + filesize +"kb\n")
    f.write("Тест получения информации из файла прошёл успешно\n\n")
except:
    f.write("Тест получения информации из файла не прошёл\n\n")
    print("ошибка получения информации из файла")
    result = 0


#Начало установки клиента
f.write("___Установка клиента___\n")
try:
    Application().start("C:\\in\\acc.exe")
    time.sleep(1)
    app = Application(backend='uia').connect(path="C:\\in\\acc.exe", title="Установка Комплекс ")
    w_handle = pywinauto.findwindows.find_windows(best_match="Установка Комплекс")[0]
    app.window(handle=w_handle).child_window(title="Далее >", auto_id="587").click_input()#первое далее
    w_handle = pywinauto.findwindows.find_windows(best_match="Установка Комплекс")[0]
    app.window(handle=w_handle).child_window(title="Я принимаю условия лицензионного соглашения", auto_id="47", control_type="RadioButton").click_input()#принятие соглашения
    app.window(handle=w_handle).child_window(title="Далее >", auto_id="587", control_type="Button").click_input()#второе далее
    w_handle = pywinauto.findwindows.find_windows(best_match="Установка Комплекс")[0]
    app.window(handle=w_handle).child_window(title="Далее >", auto_id="587", control_type="Button").click_input()#третье далее
    time.sleep(12)
    w_handle = pywinauto.findwindows.find_windows(best_match="Установка Комплекс")[0]
    app.window(handle=w_handle).child_window(title="Готово", auto_id="592", control_type="Button").click_input()#нажатие на кнопку готово
except:
	f.write("Завершение установки клиента\n\n")



#Проверка acrun
f.write("___Получение данных из файла acrun___\n")
try:
    datefile = time.ctime(os.path.getctime("c:\\Accord.x64\\acrun.sys"))
    f.write("Получена дата " + datefile + "\n")
    veracrun = getver("c:\\Accord.x64\\acrun.sys")
    f.write("Получена версия файла " + veracrun +"\n")
    filesize = os.stat("c:\\Accord.x64\\acrun.sys")
    filesize = str(int(filesize.st_size / 1000))
    f.write("Получен размер файла " + filesize +"kb\n")
    f.write("Тест получения информации из файла acrun прошёл успешно\n\n")
except:
    f.write("Тест получения информации из файла acrun не прошёл\n\n")
    print("Ошибка получения информации из файла acrun")
    result = 0


f.write("___Проверка корректности acrun___\n")
if ver == veracrun:
    f.write("Сверка acrun прошла успешно\n\n")
else:
    f.write("Сверка acrun прошла неудачно\n\n")
    print("Сверка acrun прошла неудачно")
    result = 0

#Проверка версии в реестре
f.write("___Сверка версии в реестре___\n")
try:
    hKey = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\WOW6432Node\OKB SAPR\Accord')
    regtemp = winreg.QueryValueEx(hKey,"Version")
    verreg = regtemp[0]
    f.write("Получена версия " + verreg + "\n")
    if ver == verreg:
        f.write("Сверка версий прошла успешно\n\n")
    else:
        f.write("Сверка версий прошла не удачно\n\n")
        result = 0
except:
    f.write("Возникли проблемы при сверке версии\n\n")
    result = 0
    

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
button.pack()
f.write("Общее время составило " + de + " секунд\n" )
print("Общее время составило " + de + " секунд")
f.write("_________________________________Конец записи лога_________________________________\n\n")
f.close()
main.mainloop()