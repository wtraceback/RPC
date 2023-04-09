import socket


class TCPClient(object):
    def __init__(self):
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host='127.0.0.1', port=5000):
        self.clientsocket.connect((host, port))

    def send(self, data):
        self.clientsocket.sendall(data.encode('utf-8'))

    def receive(self):
        r = self.clientsocket.recv(1024)
        r = r.decode('utf-8')
        print("response is: {}".format(r))
