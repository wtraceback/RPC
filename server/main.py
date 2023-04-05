import tcpserver


if __name__ == '__main__':
    t = tcpserver.TCPServer()
    t.bind_listen()
    while True:
        t.accept_receive_close()
