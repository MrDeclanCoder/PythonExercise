# -*- coding: utf-8 -*-
import chardet
import requests
import psutil

print(psutil.net_connections())
print(psutil.pids())
for p in psutil.pids():
    print(psutil.Process(p).name())
    name = psutil.Process(p).name()
    if name == 'adb.exe':
        print(psutil.Process(p))

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())

# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))

print(psutil.virtual_memory())
print(psutil.disk_partitions())

print('***************************\n')
print(chardet.detect(b'Hello,world!'))

r = requests.get('https://www.douban.com')
r.encoding = 'utf-8'
print(r.encoding)
print(r.url)
print('***************************\n')

r = requests.post('http://accounts.douban.com/login', data={'form_email': 'abv@exapmle.com', 'form_password': '123456'})
print(r.status_code)
print(r.headers['Content-Type'])
print(r.cookies['bid'])
print('***************************\n')
data = '离离原上草'.encode('gb2312')
print(str(data))
print(chardet.detect(data))


