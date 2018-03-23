import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
c = s.connect(('127.0.0.1', 9999))
print(c)
# 接收消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Micheal', b'Tracy', b'Search']:
    # 发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'client exit')
s.close()
