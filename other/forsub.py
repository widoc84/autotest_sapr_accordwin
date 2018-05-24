import usb
import usb.backend.libusb1
import ftplib
import os
import shutil
from tkinter import *


main = Tk()

def button_clicked():
    sys.exit()

#Получение библиотек
path = "temp\\libusb"
ftp = ftplib.FTP('192.168.51.222')
ftp.login('tester')
ftp.cwd(path)

try:
    os.mkdir("C:\\libusb")
except FileExistsError:
    pass

host_file = os.path.join(
    'C:\\libusb', 'libusb-1.0.dll'
)
try:
    with open(host_file, 'wb') as local_file:
        ftp.retrbinary('RETR ' + 'libusb-1.0.dll', local_file.write)
except ftplib.error_perm:
    pass 
ftp.quit()

#копирование дистрибутива

back = usb.backend.libusb1.get_backend(find_library=lambda x: "C:\\libusb\libusb-1.0.dll")
dev = usb.core.find(backend=back , idVendor=0x17e4, idProduct=0x0051)
endpoint = dev[0][(0,0)][0]
test = endpoint.wMaxPacketSize
textres = ''
if test == 512:
    textres = "Эта шипка 512 байт"
else:
    teststr = str(test)
    textres = "Эта шипка не 512 байт, а " + teststr

shutil.rmtree("C:\\libusb",ignore_errors=True)

label = Label(main, text=textres)
button = Button(main,
                        compound=CENTER,width=20, text='Закрыть', command=button_clicked)
label.pack()
button.pack()
main.mainloop()