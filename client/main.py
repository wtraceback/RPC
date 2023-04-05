import tcpclient


if __name__ == '__main__':
    t = tcpclient.TCPClient()
    t.connect()
    t.send("tcp 客户端发出的请求")
    t.receive()