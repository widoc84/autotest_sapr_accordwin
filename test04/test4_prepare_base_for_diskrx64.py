from pywinauto import Application
import os
import time
import datetime
import shutil
import ftplib
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

def createfile(attr):
    os.mkdir("C:\\testuser\\file\\" + attr)
    os.mkdir("C:\\testuser\\file\\" + attr + "\\On")
    folder_to = "C:\\testuser\\file\\" + attr + "\\On"
    for f in os.listdir(folder_from):
        if os.path.isfile(os.path.join(folder_from, f)):
            shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
        if os.path.isdir(os.path.join(folder_from, f)):
            shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))
    os.mkdir("C:\\testuser\\file\\" + attr + "\\Off")
    folder_to = "C:\\testuser\\file\\" + attr + "\\Off"
    for f in os.listdir(folder_from):
        if os.path.isfile(os.path.join(folder_from, f)):
            shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, f))
        if os.path.isdir(os.path.join(folder_from, f)):
            shutil.copytree(os.path.join(folder_from, f), os.path.join(folder_to, f))

def createfolder(attr):
    i = 0
    os.mkdir("C:\\testuser\\folder\\" + attr)
    folder_on = "C:\\testuser\\folder\\" + attr + "\\On"
    folder_off = "C:\\testuser\\folder\\" + attr + "\\Off"
    os.mkdir(folder_on)
    os.mkdir(folder_off)
    while i < 9: 
        istr = str(i)
        folder_on_cr = folder_on + "\\Folder" + istr
        folder_off_cr = folder_off + "\\Folder" + istr 
        os.mkdir(folder_on_cr)
        os.mkdir(folder_off_cr)
        for f in os.listdir(folder_from):
                shutil.copy(os.path.join(folder_from, f), os.path.join(folder_on_cr, f))
                shutil.copy(os.path.join(folder_from, f), os.path.join(folder_off_cr, f))
        i = i + 1

def add_atribute_file(c, d, re, h, r, w, run, path, title):
    try:
        app.window(best_match="Редактирование правил доступа ").child_window(title="Новый").click()
        app.TFDirsFiles.Edit.type_keys(path)
        if h == 1:
            app.TFDirsFiles.CheckBox9.click()#видимость
        if c == 1:
            app.TFDirsFiles.CheckBox12.click()#создание
        if d == 1:
            app.TFDirsFiles.CheckBox11.click()#удаление
        if re == 1:
            app.TFDirsFiles.CheckBox10.click()#переименование
        if r == 1:
            app.TFDirsFiles.CheckBox14.click()#чтение
        if w == 1:
            app.TFDirsFiles.CheckBox13.click()#запись
        if run == 1:
            app.TFDirsFiles.CheckBox1.click()#запуск
        app.TFDirsFiles.Button2.click()#сохранить
        app.TFDirsFiles.Button1.click()#закрыть
        f.write("При настройке " + title + " для файла проблем не обнаружено\n")
    except:
        f.write("При настройке " + title + " для файла обнаружены проблемы\n")
        print("При настройке " + title + " для файла обнаружены проблемы")
        result  =   0
        resultprd = 0 

def add_atribute_folder(c, d, re, tr, run, path, title):
    try:
        app.window(best_match="Редактирование правил доступа ").child_window(title="Новый").click()
        app.TFDirsFiles.Edit.type_keys(path)
        if c == 1:
            app.TFDirsFiles.CheckBox7.click()#создание
        if d == 1:
            app.TFDirsFiles.CheckBox6.click()#удаление
        if re == 1:
            app.TFDirsFiles.CheckBox4.click()#переименование    
        if tr == 1:
            app.TFDirsFiles.CheckBox5.click()#переход
        if run == 1:
            app.TFDirsFiles.CheckBox1.click()#запуск         
        app.TFDirsFiles.Button2.click()#сохранить
        app.TFDirsFiles.Button1.click()#закрыть
        f.write("При настройке " + title + " для каталога проблем не обнаружено\n")
    except:
        f.write("При настройке " + title + " для каталога обнаружены проблемы\n")
        print("При настройке " + title + " для каталога обнаружены проблемы")
        result  =   0
        resultprd = 0 
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

#Проверка наличия файла amz
if os.path.exists("C:\\Accord.x64\\Accord.amz"):
    os.replace("C:\\Accord.x64\\Accord.amz","C:\\Accord.x64\\Accord" + date + ".amz")
    os.replace("C:\\Accord.x64\\Accord.amz_old","C:\\Accord.x64\\Accord" + date + ".amz_old")
    f.write("Была обнаружена старая база. Старые amz файлы были переименованы\n как Accord" + date + ".amz и Accord" + date + ".amz_old\n\n")
else:
    f.write("Старая база не была обнаружена\n\n")
    pass

#Запуск приложения и создание пользователей
f.write("___Получение данных из файла___\n")
resultuser = 1

#Блок создания Главного Администратора
app = Application().start("C:\\Accord.x64\\aced32.exe")
app.window(title=u'Aced32').wait('visible',timeout=3)
app.window(title=u'Aced32')[u"Да"].DoubleClick()
app.window(best_match="TMainForm").wait('visible',timeout=20)
aced32 = app.window(best_match="TMainForm")
acedtree = aced32.TreeView   
i=0
admin_array=[]
try:
        while i < 20:
            name = acedtree.GetItem([0]).GetChild(i).Text()
            admin_array.append(name)
            i= i + 1
except:
        pass

admin_array.remove('Гл.Администратор')
for element in admin_array:
        acedtree.GetItem([u'Администраторы',element]).Click()
        f.write("Удалёна запись администратора " + element + "\n")
        aced32.MenuItem(u"#1->#2").click()
        app.Dialog.child_window(best_match="Да").click()

i=0
user_array=[]
try:
        while i < 20:
            name = acedtree.GetItem([1]).GetChild(i).Text()
            user_array.append(name)
            i= i + 1
except:
        pass
    
for element in user_array:
        acedtree.GetItem([u'Обычные',element]).Click()
        f.write("Удалёна запись пользователя " + element + "\n")
        aced32.MenuItem(u"#1->#2").click()
        app.Dialog.child_window(best_match="Да").click()
try:
    acedtree.GetItem([u'Администраторы',u'Гл.Администратор']).Click()
    aced32.TWinControl6.click()
    aced32key = app.window(best_match="Операции с ключом")
    aced32key.child_window(title="Далее >", class_name="TButton").click()
    app.window(best_match="TMainForm").wait('active',timeout=22)
    aced32.TWinControl7.click()
    app.window(best_match="Ввод пароля").Edit2.type_keys("1qaz!QAZ")
    app.window(best_match="Ввод пароля").Edit.type_keys("1qaz!QAZ")
    app.window(best_match="Ввод пароля").OK.click()
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

#Блок создания администратора
app = Application().start("C:\\Accord.x64\\aced32.exe")
app.Dialog.child_window(class_name="Edit").type_keys("1qaz!QAZ")
app.Dialog.OK.click()
print("Приложите идентификатор администратора")
app.window(best_match="TMainForm").wait('visible',timeout=3)
time.sleep(5)
aced32 = app.window(best_match="TMainForm")
acedtree = aced32.TreeView
acedtree.GetItem([u'Администратор']).Click()
aced32.MenuItem(u"#1->#0").click()
app.window(best_match="TFCreate").Edit.type_keys("ADMIN")
app.window(best_match="TFCreate").OK.click()
try:
    aced32.TWinControl6.click()
    aced32key = app.window(best_match="Операции с ключом")
    aced32key.child_window(title="Далее >", class_name="TButton").click()
    app.window(best_match="TMainForm").wait('active',timeout=22)
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
    print("Приложите идентификатор пользователя")
    time.sleep(5)
    app.window(best_match="TFCreate").Edit.type_keys("USER")
    app.window(best_match="TFCreate").OK.click()
    aced32.TWinControl6.click()
    aced32key = app.window(best_match="Операции с ключом")
    aced32key.child_window(title="Далее >", class_name="TButton").click()
    app.window(best_match="TMainForm").wait('active',timeout=22)
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
    f.write("При создании базы пользователей проблемы не возникли\n\n")
else:
    f.write("При создании базы пользователей возникли проблемы\n\n")
    print("При создании базы пользователей возникли проблемы")
    result=0

print("Приложите идентификатор главного администратора")
time.sleep(15)

#Создание списка файлов
f.write("___Создание списка файлов___\n")

#Настройка FTP соеденения
path = "temp\\test"
ftp = ftplib.FTP('192.168.51.222')
ftp.login('tester')
ftp.cwd(path)
filenames = ftp.nlst()

if os.path.exists("C:\\testuser"):
    shutil.rmtree("C:\\testuser")
os.mkdir("C:\\testuser")
os.mkdir('C:\\testuser\\temp') 
folder_from = 'C:\\testuser\\temp'

for filename in filenames:
        host_file = os.path.join(
            'C:\\testuser\\temp', filename
        )
    
        try:
            with open(host_file, 'wb') as local_file:
                ftp.retrbinary('RETR ' + filename, local_file.write)
        except ftplib.error_perm:
            pass 
ftp.quit()

try:
    os.mkdir("C:\\testuser\\folder")
    os.mkdir("C:\\testuser\\file")
    createfile('create')
    createfile('delete')
    createfile('read')
    createfile('rename')
    createfile('write')
    createfile('hidden')
    createfile('run')
    createfolder('create')
    createfolder('run')
    createfolder('rename')
    createfolder('transition')
    createfolder('delete')
    f.write("Файлы были созданы успешно\n")
except:
    f.write("Возникла проблема при создании файлов\n")
    print("Возникла проблема при создании файлов")
    result = 0

#Настройка ПРД пользователя
f.write("___Настройка ПРД___\n")
resultprd = 1
app = Application().start("C:\\Accord.x64\\aced32.exe")
time.sleep(2)
app.Dialog.child_window(class_name="Edit").type_keys("1qaz!QAZ")
app.Dialog.OK.click()
aced32 = app.window(best_match="TMainForm")
acedtree = aced32.TreeView
acedtree.GetItem([u'Обычные',u'USER']).Click()
aced32.TWinControl3.click()


add_atribute_file(c=1, d=0, re=0, h=0, r=0, w=0, run=0, path='C:\\testuser\\file\\create\\On\\', 
                  title='разрешение создания')
add_atribute_file(c=0, d=1, re=1, h=1, r=1, w=1, run=1, path = 'C:\\testuser\\file\\create\\Off\\', 
                  title='запрещение создания')
add_atribute_file(c=0, d=1, re=0, h=0, r=0, w=0, run=0, path='C:\\testuser\\file\\delete\\On\\', 
                  title='разрешение удаления')
add_atribute_file(c=1, d=0, re=1, h=1, r=1, w=1, run=1, path = 'C:\\testuser\\file\\delete\\Off\\', 
                  title='запрещение удаления')
add_atribute_file(c=0, d=0, re=1, h=0, r=0, w=0, run=0, path='C:\\testuser\\file\\rename\\On\\', 
                  title='разрешение переименования')
add_atribute_file(c=1, d=1, re=0, h=1, r=1, w=1, run=1, path = 'C:\\testuser\\file\\rename\\Off\\', 
                  title='запрещение переименования')
add_atribute_file(c=0, d=0, re=0, h=1, r=0, w=0, run=0, path='C:\\testuser\\file\\hidden\\On\\', 
                  title='разрешение видимости')
add_atribute_file(c=1, d=1, re=1, h=0, r=1, w=1, run=1, path = 'C:\\testuser\\file\\hidden\\Off\\', 
                  title='запрещение видимости')
add_atribute_file(c=0, d=0, re=0, h=0, r=1, w=0, run=0, path='C:\\testuser\\file\\read\\On\\', 
                  title='разрешение чтения')
add_atribute_file(c=1, d=1, re=1, h=1, r=0, w=1, run=1, path = 'C:\\testuser\\file\\read\\Off\\', 
                  title='запрещение чтения')
add_atribute_file(c=0, d=0, re=0, h=0, r=0, w=1, run=0, path='C:\\testuser\\file\\write\\On\\', 
                  title='разрешение записи')
add_atribute_file(c=1, d=1, re=1, h=1, r=1, w=0, run=1, path = 'C:\\testuser\\file\\write\\Off\\', 
                  title='запрещение записи')
add_atribute_file(c=0, d=0, re=0, h=0, r=0, w=0, run=1, path='C:\\testuser\\file\\run\\On\\', 
                  title='разрешение запуска')
add_atribute_file(c=1, d=1, re=1, h=1, r=1, w=1, run=0, path = 'C:\\testuser\\file\\run\\Off\\', 
                  title='запрещение запуска')

add_atribute_folder(c=1, d=0, re=0, tr=0, run=0, path='C:\\testuser\\folder\\create\\On\\', 
                  title='разрешение создания')
add_atribute_folder(c=0, d=1, re=1, tr=1, run=1, path='C:\\testuser\\folder\\create\\Off\\', 
                  title='запрещение создания')
add_atribute_folder(c=0, d=1, re=0, tr=0, run=0, path='C:\\testuser\\folder\\delete\\On\\', 
                  title='разрешение удаления')
add_atribute_folder(c=1, d=0, re=1, tr=1, run=1, path='C:\\testuser\\folder\\delete\\Off\\', 
                  title='запрещение удаления')
add_atribute_folder(c=0, d=0, re=1, tr=0, run=0, path='C:\\testuser\\folder\\rename\\On\\', 
                  title='разрешение переименования')
add_atribute_folder(c=1, d=1, re=0, tr=1, run=1, path='C:\\testuser\\folder\\rename\\Off\\', 
                  title='запрещение переименования')
add_atribute_folder(c=0, d=0, re=0, tr=1, run=0, path='C:\\testuser\\folder\\transition\\On\\', 
                  title='разрешение перехода')
add_atribute_folder(c=1, d=1, re=1, tr=0, run=1, path='C:\\testuser\\folder\\transition\\Off\\', 
                  title='запрещение перехода')
add_atribute_folder(c=0, d=0, re=0, tr=0, run=1, path='C:\\testuser\\folder\\run\\On\\', 
                  title='разрешение запуска')
add_atribute_folder(c=1, d=1, re=1, tr=1, run=0, path='C:\\testuser\\folder\\run\\Off\\', 
                  title='запрещение запуска')

if resultprd == 1:
    f.write("При создании ПРД проблем не обнаружено\n\n")
else:
    f.write("При создании ПРД обнаружены проблемы\n\n")
    print("При создании ПРД обнаружены проблемы")
    result=0

app.window(best_match="Редактирование правил доступа ").child_window(title="Сохранить").click()
time.sleep(1)
app.window(best_match="TMainForm").MenuItem(u"#0->#3").click()
app.window(best_match="TFMsgBox").child_window(best_match="Да").click()
app.window(best_match="TMainForm").MenuItem(u"#0->#10").click()

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