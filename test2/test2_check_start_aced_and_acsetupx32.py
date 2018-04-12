from pywinauto import Application
import os
import time
import datetime

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


#Получение даты
day = datetime.datetime.now().day
month = datetime.datetime.now().month
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
date = str(day) + str(month) + "_" + str(hour) +  str(minute)
dt = datetime.datetime.strptime(date, "%d%m_%H%M")
date = dt.strftime("%d%m_%H%M")


#Создание и старт записи в файл
path = "c:\\testlog\\test2_" + date  + ".txt"
f = open(path, "tw", encoding='utf-8')
f.write("_________________________________Начало записи лога_________________________________\n\n")
datestart = datetime.datetime.now()
timestart = gettime()
f.write("Проверка началась в " + timestart + "\n\n")


#Проверка запуска aced
try:
    app = Application().start("C:\\Accord.NT\\Aced32.exe")
    app.window(best_match="ACED32 Редактор базы ", class_name='TMainForm').wait('visible',timeout=20)
    app.kill()
    print("Aced32 корректно открылся")
except:
    print("Aced32 не открылся")
    app.kill()
    result = 0
time.sleep(5)


#Проверка запуска acsetup
try:
    app = Application().start("C:\\Accord.NT\\AcSetup.exe")
    app.window(best_match="Настройка Комплекс СЗИ НСД").wait('visible',timeout=20)
    app.kill()
    print("AcSetup корректно открылся")
except:
    print("AcSetup не открылся")
    app.kill()
    result = 0


#Завершение проверки
datefinish = datetime.datetime.now()
timefinish = gettime()
f.write("Проверка завершилась в " + timefinish + "\n")
de = datefinish - datestart
de = str(de.seconds)
f.write("Общее время составило " + de + " секунд\n" )
print("Общее время составило " + de + " секунд")
f.write("_________________________________Конец записи лога_________________________________\n\n")
f.close()
