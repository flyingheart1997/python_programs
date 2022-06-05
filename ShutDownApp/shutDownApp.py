from tkinter import *
import os


def restart():
    os.system("shutdown /r /t 1")


def restart_time():
    os.system("shutdown /r /t 30")


def logout():
    os.system("shutdown -1")


def shut_down():
    os.system("shutdown /s /t 1")


st = Tk()
st.title("ShutDown")
st.geometry("300x200")
st.config(bg="black")
restarts = Button(st, text="Restart", font=("Time New Roman", 10, "bold"),
                  relief=RAISED, cursor="heart", command=restart)
restarts.place(x=20, y=30, height=30, width=90)

restart_Time = Button(st, text="Restart Time", font=("Time New Roman", 10, "bold"),
                      relief=RAISED, cursor="heart", command=restart_time)
restart_Time.place(x=180, y=30, height=30, width=100)

logOut = Button(st, text="Log Out", font=("Time New Roman", 10, "bold"),
                relief=RAISED, cursor="heart", command=logout)
logOut.place(x=20, y=110, height=30, width=90)

shutDown = Button(st, text="shut Down", font=("Time New Roman", 10, "bold"),
                  relief=RAISED, cursor="heart", command=shut_down)
shutDown.place(x=180, y=110, height=30, width=100)
st.mainloop()
