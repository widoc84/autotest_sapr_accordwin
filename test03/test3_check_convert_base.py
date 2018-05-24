from pywinauto import Application
import os
import time
import datetime
import shutil
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


#Получение даты
day = datetime.datetime.now().day
month = datetime.datetime.now().month
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
date = str(day) + str(month) + "_" + str(hour) +  str(minute)
dt = datetime.datetime.strptime(date, "%d%m_%H%M")
date = dt.strftime("%d%m_%H%M")

#Создание и старт записи в файл
path = "c:\\testlog\\test3_" + date  + ".txt"
f = open(path, "tw", encoding='utf-8')
f.write("_________________________________Начало записи лога_________________________________\n\n")
datestart = datetime.datetime.now()
timestart = gettime()
f.write("Проверка началась в " + timestart + "\n\n")

#Проверка наличия файла amz
if os.path.exists("C:\\Accord.x64\\Accord.amz"):
    os.replace("C:\\Accord.x64\\Accord.amz","C:\\Accord.x64\\Accord" + date + ".amz")
    os.replace("C:\\Accord.x64\\Accord.amz_old","C:\\Accord.x64\\Accord" + date + ".amz_old")
    f.write("Была обнаружена старая база. Старые amz файлы были переименованы\n как Accord" + date + ".amz и Accord" + date + ".amz_old\n\n")
else:
    f.write("Старая база не была обнаружена\n\n")
    pass

#Запуск aced
app = Application().start("C:\\Accord.x64\\aced32.exe")
app.window(title=u'Aced32').wait('visible',timeout=3)
app.window(title=u'Aced32')[u"Да"].DoubleClick()
app.window(best_match="TMainForm").wait('visible',timeout=3)
aced32 = app.window(best_match="TMainForm")
acedtree = aced32.TreeView
aced32.MenuItem(u"#0->#3").click()#сохранение
app.window(best_match="TFMsgBox").child_window(best_match="Да").click()

#Копирование баз
shutil.copy('C:\\in\Accord.amz', 'C:\\in\Accord_old.amz')
shutil.copy('C:\\in\Accord.amz', 'C:\\in\Accord_new.amz')

#Конвертация баз
aced32.MenuItem(u"#0->#6").click()#открытие меню импорта
app.TbsOpenDlgForm.Edit.type_keys('C:\\in\\')
app.TbsOpenDlgForm.Edit.type_keys('{ENTER}')
app.TbsOpenDlgForm.Edit.SetEditText('')
app.TbsOpenDlgForm.Edit.type_keys('Accord_new.amz')
app.TbsOpenDlgForm.Button2.click()

app.Dialog.Button.click()#подтверждение конвертации
acedtree.GetItem([u'Администраторы',u'Гл.Администратор']).Click()
aced32.TWinControl11.click()
app.TFPP.button2.click()
aced32.MenuItem(u"#0->#3").click()#сохранение
app.window(best_match="TFMsgBox").child_window(best_match="Да").click()
aced32.MenuItem(u"#0->#10").click()#закрытие

try:
    aced32.MenuItem(u"#0->#6").click()
    app.TbsOpenDlgForm.Edit.type_keys('C:\\in\\')
    app.TbsOpenDlgForm.Edit.type_keys('{ENTER}')
    app.TbsOpenDlgForm.Edit.SetEditText('')
    app.TbsOpenDlgForm.Edit.type_keys('Accord_old.amz')
    app.TbsOpenDlgForm.Button2.click()
    app.window(best_match="TFMsgBox").child_window(best_match="Нет").click()

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