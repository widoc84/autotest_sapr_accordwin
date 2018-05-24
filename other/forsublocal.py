from tkinter import *
import usb
import os
#import usb.backend.libusb1 as libusb



main = Tk()

def button_clicked():
    sys.exit()


#копирование дистрибутив
textres = ""
dev = usb.core.find(idVendor=0x17e4, idProduct=0x0051)
endpoint = dev[0][(0,0)][0]
test = endpoint.wMaxPacketSize
if test == 512:
        textres = "Эта шипка 512 байт"
else:
        teststr = str(test)
        textres = "Эта шипка не 512 байт, а " + teststr


label = Label(main, text=textres)
button = Button(main, compound=CENTER,width=20, text='Закрыть', command=button_clicked)
label.pack()
button.pack()
main.mainloop()