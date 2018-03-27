import socket
import threading
import time

#
# def udplink(sock, addr):
#     print('Accept new connection from %s:%s...')
#     sock.send(b'Welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8') == 'client exit':
#             break
#         sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
#     sock.close()
#     print('Connection from %s:%s closed' % addr)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 监听端口
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')

while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    reply = 'Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)
