import socket


class TCPServer(object):
    def __init__(self):
        # 初始化 socket；socket.AF_INET 表示因特网 IPv4 地址族，SOCK_STREAM 表示使用 TCP 的 socket 类型
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind_listen(self, host, port):
        # 套接字绑定的 IP 与 端口
        self.serversocket.bind((host, port))
        # 将套接字变为一个服务区套接字，进行监听，数字 5 将端口上的等待队列长度限制为 5，即超过 5 个的请求将被拒绝。
        self.serversocket.listen(5)

    def accept_receive_close(self):
        # 接收外部连接请求，当有客户端过来连接的时候, serversocket.accept 函数就会返回 2 个值
        clientsocket, address = self.serversocket.accept()
        r = clientsocket.recv(1024)
        print("r = {}".format(r.decode('utf-8')))

        response = 'tcp 服务器端接收到请求后，返回的响应'
        clientsocket.sendall(response.encode('utf-8'))            # 用 sendall 发送给客户端

        clientsocket.close()