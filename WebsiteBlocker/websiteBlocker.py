import datetime
import time
end_time = datetime.datetime(2022, 5, 10)
site_block = ['www.facebook.com', 'www.instagram.com']
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect_no = '127.0.0.1'
while True:
    if datetime.datetime.now() < end_time:
        print("Start Blocking....")
        with open(host_path, 'r+') as host_file:
            file = host_file.read()
            for website in site_block:
                if website not in file:
                    host_file.write(redirect_no + ''+website+'\n')
                    host_file.close()
                else:
                    pass
    else:
        print('End Blocking.....')
        with open(host_path, 'r+') as host_file:
            file = host_file.readlines()
            host_file.seek(0)
            for lines in file:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)
            host_file.truncate()
        time.sleep(5)
