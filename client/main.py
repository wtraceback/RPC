import rpcclient


if __name__ == '__main__':
    t = rpcclient.RPCClient()
    t.connect('127.0.0.1', 5000)
    t.send("tcp 客户端发出的请求")
    t.receive()