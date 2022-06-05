from tkinter import *
import speedtest


def speed_check():
    sp_test = speedtest.Speedtest()
    sp_test.get_servers()
    down = str(round(sp_test.download()/(10**6), 3)) + ' Mbps'
    upl = str(round(sp_test.upload()/(10**6), 3)) + ' Mbps'
    download.config(text=down)
    upload.config(text=upl)


sp = Tk()
sp.title('Internet Speed Test')
sp.geometry('300x400')
sp.config(bg='#202124')
label = Label(sp, text='Internet Speed Test', font=('Italic', 18), bg="#202124", fg="white")
label.place(x=40, y=40,)

label = Label(sp, text='Download Speed :', font=('Italic', 15), bg="#202124", fg="white")
label.place(x=70, y=80, )
download = Label(sp, text='00', font=('Italic', 15), bg="#202124",  fg="white")
download.place(x=75, y=120, width=150)

label = Label(sp, text='Upload Speed :', font=('Italic', 15), bg="#202124", fg="white")
label.place(x=80, y=160, )
upload = Label(sp, text='00', font=('Italic', 15), bg="#202124", fg="white")
upload.place(x=75, y=200, width=150)

button = Button(sp, text="CHECK", font=("Italic", 15), relief=RAISED, cursor="plus", command=speed_check)
button.place(x=100, y=270, width=100)

sp.mainloop()
