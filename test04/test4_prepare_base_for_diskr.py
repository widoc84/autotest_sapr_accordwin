from pywinauto import Application
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
path = "c:\\testlog\\test4_" + date  + ".txt"
f = open(path, "tw", encoding='utf-8')
f.write("_________________________________Начало записи лога_________________________________\n\n")
datestart = datetime.datetime.now()
timestart = gettime()
f.write("Проверка началась в " + timestart + "\n\n")

#Запуск приложения и создание пользователей
f.write("___Получение данных из файла___\n")
resultuser = 1

try:#Блок создания Главного Администратора
    app = Application().start("C:\\Accord.x64\\aced32.exe")
    app.window(title=u'Aced32')[u"Да"].DoubleClick()
    aced32 = app.window(best_match="TMainForm")
    acedtree = aced32.TreeView
    acedtree.GetItem([u'Администраторы',u'Гл.Администратор']).Click()
    aced32.TWinControl6.click()
    aced32key = app.window(best_match="Операции с ключом")
    aced32key.child_window(title="Далее >", class_name="TButton").click()
    aced32.TWinControl7.click()
    app.window(best_match="Ввод пароля").Edit2.type_keys("1qaz!QAZ")
    app.window(best_match="Ввод пароля").Edit.type_keys("1qaz!QAZ")
    app.window(best_match="Ввод пароля").OK.click()
    print("У вас есть 30 секунд чтобы удалить всех ненужных пользователей")
    time.sleep(30)
    aced32.MenuItem(u"#0->#3").click()
    app.window(best_match="TFMsgBox").child_window(best_match="Да").click()
    aced32.MenuItem(u"#0->#10").click()
    f.write("Гланый администратор был успешно создан\n")
except:
    f.write("При создании главного администратора возникли проблемы\n")
    print("При создании главного администратора возникли проблемы")
    result = 0
    resultuser = 0

time.sleep(1)

try:#Блок создания администратора
    app = Application().start("C:\\Accord.x64\\aced32.exe")
    app.Dialog.child_window(class_name="Edit").type_keys("1qaz!QAZ")
    app.Dialog.OK.click()
    print("У вас есть 20 секунд чтобы приложить идентификатор администратора")
    time.sleep(20)
    aced32 = app.window(best_match="TMainForm")
    acedtree = aced32.TreeView
    acedtree.GetItem([u'Администратор']).Click()
    aced32.MenuItem(u"#1->#0").click()
    app.window(best_match="TFCreate").Edit.type_keys("ADMIN")
    app.window(best_match="TFCreate").OK.click()
    aced32.TWinControl6.click()
    aced32key = app.window(best_match="Операции с ключом")
    aced32key.child_window(title="Далее >", class_name="TButton").click()
    aced32.TWinControl7.click()
    app.window(best_match="Ввод пароля").Edit2.type_keys("1qaz@WSX")
    app.window(best_match="Ввод пароля").Edit.type_keys("1qaz@WSX")
    app.window(best_match="Ввод пароля").OK.click()
    f.write("Администратор был успешно создан\n")
except:
    f.write("При создании администратора возникли проблемы\n")
    print("При создании администратора возникли проблемы")
    result = 0
    resultuser = 0

try:
    acedtree.GetItem([u'Обычные']).Click()
    aced32.MenuItem(u"#1->#0").click()
    print("У вас есть 20 секунд чтобы приложить идентификатор пользователя")
    time.sleep(20)
    app.window(best_match="TFCreate").Edit.type_keys("USER")
    app.window(best_match="TFCreate").OK.click()
    aced32.TWinControl6.click()
    aced32key = app.window(best_match="Операции с ключом")
    aced32key.child_window(title="Далее >", class_name="TButton").click()
    aced32.TWinControl7.click()
    app.window(best_match="Ввод пароля").Edit2.type_keys("1qaz@WSX")
    app.window(best_match="Ввод пароля").Edit.type_keys("1qaz@WSX")
    app.window(best_match="Ввод пароля").OK.click()
    aced32.MenuItem(u"#0->#3").click()
    app.window(best_match="TFMsgBox").child_window(best_match="Да").click()
    aced32.MenuItem(u"#0->#10").click()
    f.write("Пользователь был успешно создан\n")
except:
    f.write("При создании пользователя возникли проблемы\n")
    print("При создании пользователя возникли проблемы")
    result = 0
    resultuser = 0

if resultuser == 1:
    f.write("При создании базы пользователей проблемы не возникли\n")
else:
    f.write("При создании базы пользователей возникли проблемы\n")
    print("При создании базы пользователей возникли проблемы")


datefinish = datetime.datetime.now()
timefinish = gettime()
f.write("Проверка завершилась в " + timefinish + "\n")
de = datefinish - datestart
de = str(de.seconds)
f.write("Общее время составило " + de + " секунд\n" )
print("Общее время составило " + de + " секунд")
f.write("_________________________________Конец записи лога_________________________________\n\n")
f.close()