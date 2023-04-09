import tcpserver


class RPCServer(tcpserver.TCPServer):
    def __init__(self):
        # super(RPCServer, self).__init__() # python2
        super().__init__()    # python3

    def loop(self, host='0.0.0.0', port=5000):
        self.bind_listen(host, port)
        print('Server start at', '{}:{}.'.format(host, port))

        while True:
            self.accept_receive_close()
