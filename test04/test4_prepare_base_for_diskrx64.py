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

try:#Блок создания Главного Администратора
    app = Application().start("C:\\Accord.x64\\aced32.exe")
    app.window(title=u'Aced32')[u"Да"].DoubleClick()
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

    acedtree.GetItem([u'Администраторы',u'Гл.Администратор']).Click()
    aced32.TWinControl6.click()
    aced32key = app.window(best_match="Операции с ключом")
    aced32key.child_window(title="Далее >", class_name="TButton").click()
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
    f.write("При создании базы пользователей проблемы не возникли\n\n")
else:
    f.write("При создании базы пользователей возникли проблемы\n\n")
    print("При создании базы пользователей возникли проблемы")
    result=0
print("Смените идентификатор на идентификатор главного администратора у вас есть 20 секунд")
time.sleep(20)

#Создание списка файлов
f.write("___Создание списка файлов___\n")
try:
    os.mkdir("C:\\testuser")
    os.mkdir("C:\\testuser\\folder")
    os.mkdir("C:\\testuser\\file")
    os.mkdir("C:\\testuser\\file\\create")
    os.mkdir("C:\\testuser\\file\\delete")
    os.mkdir("C:\\testuser\\file\\hidden")
    os.mkdir("C:\\testuser\\file\\read")
    os.mkdir("C:\\testuser\\file\\rename")
    os.mkdir("C:\\testuser\\file\\write")
    os.mkdir("C:\\testuser\\folder\\delete")
    os.mkdir("C:\\testuser\\folder\\delete\\Folder1")
    os.mkdir("C:\\testuser\\folder\\delete\\Folder2")
    os.mkdir("C:\\testuser\\folder\\delete\\Folder3")
    os.mkdir("C:\\testuser\\folder\\delete\\Folder4")
    os.mkdir("C:\\testuser\\folder\\delete\\Folder5")
    os.mkdir("C:\\testuser\\folder\\delete\\Folder6")
    os.mkdir("C:\\testuser\\folder\\delete\\Folder7")
    os.mkdir("C:\\testuser\\folder\\delete\\Folder8")
    os.mkdir("C:\\testuser\\folder\\delete\\Folder9")
    os.mkdir("C:\\testuser\\folder\\create\\Folder1")
    os.mkdir("C:\\testuser\\folder\\create")
    os.mkdir("C:\\testuser\\folder\\create\\Folder1")
    os.mkdir("C:\\testuser\\folder\\programrun")
    os.mkdir("C:\\testuser\\folder\\rename")
    os.mkdir("C:\\testuser\\folder\\rename\\Folder1")
    os.mkdir("C:\\testuser\\folder\\rename\\Folder2")
    os.mkdir("C:\\testuser\\folder\\rename\\Folder3")
    os.mkdir("C:\\testuser\\folder\\rename\\Folder4")
    os.mkdir("C:\\testuser\\folder\\rename\\Folder5")
    os.mkdir("C:\\testuser\\folder\\rename\\Folder6")
    os.mkdir("C:\\testuser\\folder\\rename\\Folder7")
    os.mkdir("C:\\testuser\\folder\\rename\\Folder8")
    os.mkdir("C:\\testuser\\folder\\rename\\Folder9")
    os.mkdir("C:\\testuser\\folder\\transition")
    os.mkdir("C:\\testuser\\folder\\transition\\Folder1")
    os.mkdir("C:\\testuser\\folder\\transition\\Folder2")
    os.mkdir("C:\\testuser\\folder\\transition\\Folder3")
    os.mkdir("C:\\testuser\\folder\\transition\\Folder4")
    os.mkdir("C:\\testuser\\folder\\transition\\Folder5")
    os.mkdir("C:\\testuser\\folder\\transition\\Folder6")
    os.mkdir("C:\\testuser\\folder\\transition\\Folder7")
    os.mkdir("C:\\testuser\\folder\\transition\\Folder8")
    os.mkdir("C:\\testuser\\folder\\transition\\Folder9")
    f.write("При создании списка файлов проблемы не возникли\n\n")
except:
    f.write("При создании списка файлов возникли проблемы\n\n")
    print("При создании списка файлов возникли проблемы")
    result=0


#Настройка ПРД пользователя
f.write("___Настройка ПРД___\n")

try:
    app = Application().start("C:\\Accord.x64\\aced32.exe")
    app.Dialog.child_window(class_name="Edit").type_keys("1qaz!QAZ")
    app.Dialog.OK.click()
    aced32 = app.window(best_match="TMainForm")
    acedtree = aced32.TreeView
    acedtree.GetItem([u'Обычные',u'USER']).Click()
    aced32.TWinControl3.click()
    f.write("При запуске окна атрибутов проблем не обнаружено\n")
except:
    f.write("При запуске окна атрибутов обнаружены проблемы\n")
    print("При запуске окна атрибутов обнаружены проблемы")
    result=0

try:
    app.window(best_match="Редактирование правил доступа ").child_window(title="Новый").click()
    app.TFDirsFiles.Edit.type_keys("C:\\testuser\\file\\create")
    app.TFDirsFiles.CheckBox9.click()#видимость
    app.TFDirsFiles.CheckBox10.click()#переименование
    app.TFDirsFiles.CheckBox11.click()#удаление
    app.TFDirsFiles.CheckBox14.click()#чтение
    app.TFDirsFiles.CheckBox13.click()#запись
    app.TFDirsFiles.Button2.click()#сохранить
    app.TFDirsFiles.Button1.click()#закрыть
    f.write("При настройке атрибутов создания проблем не обнаружено\n")
except:
    f.write("При настройке атрибутов создания обнаружены проблемы\n")
    print("При настройке атрибутов создания обнаружены проблемы")
    result=0

try:
    app.window(best_match="Редактирование правил доступа ").child_window(title="Новый").click()
    app.TFDirsFiles.Edit.type_keys("C:\\testuser\\file\\delete")
    app.TFDirsFiles.CheckBox12.click()#создание
    app.TFDirsFiles.CheckBox9.click()#видимость
    app.TFDirsFiles.CheckBox10.click()#переименование
    app.TFDirsFiles.CheckBox14.click()#чтение
    app.TFDirsFiles.CheckBox13.click()#запись
    app.TFDirsFiles.Button2.click()#сохранить
    app.TFDirsFiles.Button1.click()#закрыть
    f.write("При настройке атрибутов удаления проблем не обнаружено\n")
except:
    f.write("При настройке атрибутов удаления обнаружены проблемы\n")
    print("При настройке атрибутов удаления обнаружены проблемы")
    result=0

try:
    app.window(best_match="Редактирование правил доступа ").child_window(title="Новый").click()
    app.TFDirsFiles.Edit.type_keys("C:\\testuser\\file\\hidden")
    app.TFDirsFiles.CheckBox12.click()#создание
    app.TFDirsFiles.CheckBox10.click()#переименование
    app.TFDirsFiles.CheckBox11.click()#удаление
    app.TFDirsFiles.CheckBox14.click()#чтение
    app.TFDirsFiles.CheckBox13.click()#запись
    app.TFDirsFiles.Button2.click()#сохранить
    app.TFDirsFiles.Button1.click()#закрыть
    f.write("При настройке атрибутов видимости проблем не обнаружено\n")
except:
    f.write("При настройке атрибутов видимости обнаружены проблемы\n")
    print("При настройке атрибутов видимости обнаружены проблемы")
    result=0

try:
    app.window(best_match="Редактирование правил доступа ").child_window(title="Новый").click()
    app.TFDirsFiles.Edit.type_keys("C:\\testuser\\file\\read")
    app.TFDirsFiles.CheckBox12.click()#создание
    app.TFDirsFiles.CheckBox9.click()#видимость
    app.TFDirsFiles.CheckBox10.click()#переименование
    app.TFDirsFiles.CheckBox11.click()#удаление
    app.TFDirsFiles.CheckBox13.click()#запись
    app.TFDirsFiles.Button2.click()#сохранить
    app.TFDirsFiles.Button1.click()#закрыть
    f.write("При настройке атрибутов чтения проблем не обнаружено\n")
except:
    f.write("При настройке атрибутов чтения обнаружены проблемы\n")
    print("При настройке атрибутов чтения обнаружены проблемы")
    result=0

try:
    app.window(best_match="Редактирование правил доступа ").child_window(title="Новый").click()
    app.TFDirsFiles.Edit.type_keys("C:\\testuser\\file\\rename")
    app.TFDirsFiles.CheckBox12.click()#создание
    app.TFDirsFiles.CheckBox9.click()#видимость
    app.TFDirsFiles.CheckBox11.click()#удаление
    app.TFDirsFiles.CheckBox14.click()#чтение
    app.TFDirsFiles.CheckBox13.click()#запись
    app.TFDirsFiles.Button2.click()#сохранить
    app.TFDirsFiles.Button1.click()#закрыть
    f.write("При настройке атрибутов переименования проблем не обнаружено\n")
except:
    f.write("При настройке атрибутов переименования обнаружены проблемы\n")
    print("При настройке атрибутов переименования обнаружены проблемы")
    result=0

try:
    app.window(best_match="Редактирование правил доступа ").child_window(title="Новый").click()
    app.TFDirsFiles.Edit.type_keys("C:\\testuser\\file\\write")
    app.TFDirsFiles.CheckBox12.click()#создание
    app.TFDirsFiles.CheckBox9.click()#видимость
    app.TFDirsFiles.CheckBox10.click()#переименование
    app.TFDirsFiles.CheckBox11.click()#удаление
    app.TFDirsFiles.CheckBox14.click()#чтение
    app.TFDirsFiles.Button2.click()#сохранить
    app.TFDirsFiles.Button1.click()#закрыть
    f.write("При настройке атрибутов записи проблем не обнаружено\n")
except:
    f.write("При настройке атрибутов записи обнаружены проблемы\n")
    print("При настройке атрибутов записи обнаружены проблемы")
    result=0

try:
    app.window(best_match="Редактирование правил доступа ").child_window(title="Новый").click()
    app.TFDirsFiles.Edit.type_keys("C:\\testuser\\folder\\create")
    app.TFDirsFiles.CheckBox6.click()#удаление
    app.TFDirsFiles.CheckBox5.click()#переход
    app.TFDirsFiles.CheckBox4.click()#переименование
    app.TFDirsFiles.CheckBox1.click()#запуск
    app.TFDirsFiles.Button2.click()#сохранить
    app.TFDirsFiles.Button1.click()#закрыть
    f.write("При настройке атрибутов создания на каталог проблем не обнаружено\n")
except:
    f.write("При настройке атрибутов создания на каталог обнаружены проблемы\n")
    print("При настройке атрибутов создания на каталог обнаружены проблемы")
    result=0

try:
    app.window(best_match="Редактирование правил доступа ").child_window(title="Новый").click()
    app.TFDirsFiles.Edit.type_keys("C:\\testuser\\folder\\delete")
    app.TFDirsFiles.CheckBox7.click()#создание
    app.TFDirsFiles.CheckBox5.click()#переход
    app.TFDirsFiles.CheckBox4.click()#переименование
    app.TFDirsFiles.CheckBox1.click()#запуск
    app.TFDirsFiles.Button2.click()#сохранить
    app.TFDirsFiles.Button1.click()#закрыть
    f.write("При настройке атрибутов удаление на каталог проблем не обнаружено\n")
except:
    f.write("При настройке атрибутов удаление на каталог обнаружены проблемы\n")
    print("При настройке атрибутов удаление на каталог обнаружены проблемы")
    result=0

try:
    app.window(best_match="Редактирование правил доступа ").child_window(title="Новый").click()
    app.TFDirsFiles.Edit.type_keys("C:\\testuser\\folder\\rename")
    app.TFDirsFiles.CheckBox7.click()#создание
    app.TFDirsFiles.CheckBox6.click()#удаление
    app.TFDirsFiles.CheckBox5.click()#переход
    app.TFDirsFiles.CheckBox1.click()#запуск
    app.TFDirsFiles.Button2.click()#сохранить
    app.TFDirsFiles.Button1.click()#закрыть
    f.write("При настройке атрибутов переименование на каталог проблем не обнаружено\n")
except:
    f.write("При настройке атрибутов переименование на каталог обнаружены проблемы\n")
    print("При настройке атрибутов переименование на каталог обнаружены проблемы")
    result=0

try:
    app.window(best_match="Редактирование правил доступа ").child_window(title="Новый").click()
    app.TFDirsFiles.Edit.type_keys("C:\\testuser\\folder\\transition")
    app.TFDirsFiles.CheckBox7.click()#создание
    app.TFDirsFiles.CheckBox6.click()#удаление
    app.TFDirsFiles.CheckBox4.click()#переименование
    app.TFDirsFiles.CheckBox1.click()#запуск
    app.TFDirsFiles.Button2.click()#сохранить
    app.TFDirsFiles.Button1.click()#закрыть
    f.write("При настройке атрибутов переход на каталог проблем не обнаружено\n")
except:
    f.write("При настройке атрибутов переход на каталог обнаружены проблемы\n")
    print("При настройке атрибутов переход на каталог обнаружены проблемы")
    result=0

try:
    app.window(best_match="Редактирование правил доступа ").child_window(title="Новый").click()
    app.TFDirsFiles.Edit.type_keys("C:\\testuser\\folder\\programrun")
    app.TFDirsFiles.CheckBox7.click()#создание
    app.TFDirsFiles.CheckBox6.click()#удаление
    app.TFDirsFiles.CheckBox5.click()#переход
    app.TFDirsFiles.CheckBox4.click()#переименование
    app.TFDirsFiles.Button2.click()#сохранить
    app.TFDirsFiles.Button1.click()#закрыть
    f.write("При настройке атрибутов запуск на каталог проблем не обнаружено\n")
except:
    f.write("При настройке атрибутов запуск на каталог обнаружены проблемы\n")
    print("При настройке атрибутов запуск на каталог обнаружены проблемы")
    result=0

app.window(best_match="Редактирование правил доступа ").child_window(title="Сохранить").click()
time.sleep(1)
app.window(best_match="TMainForm").MenuItem(u"#0->#3").click()
app.window(best_match="TFMsgBox").child_window(best_match="Да").click()
app.window(best_match="TMainForm").MenuItem(u"#0->#10").click()

datefinish = datetime.datetime.now()
timefinish = gettime()
f.write("Проверка завершилась в " + timefinish + "\n")
de = datefinish - datestart
de = str(de.seconds)
f.write("Общее время составило " + de + " секунд\n" )
print("Общее время составило " + de + " секунд")
f.write("_________________________________Конец записи лога_________________________________\n\n")
f.close()