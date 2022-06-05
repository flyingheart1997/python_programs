from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title='*** Take Rest ***',
            message="Rest is vital for better mental health, increased concentration and memory",
            app_icon='K:/Python Project/Python-Program/notification.ico',
            timeout=5,
        )
        time.sleep(3600)

# if you want to run the program as background then u have to run the command : pythonw <filename>
# and if you want to stop the background process then goto the task manager, find python file and click ['End Task'].
