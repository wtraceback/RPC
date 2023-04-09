import json
import tcpserver


class RPCStub(object):
    def __init__(self):
        self.funs = {}

    def register_function(self, fn, name=None):
        """Server 端方法的注册，已注册的方法可以在 Client 端调用"""
        if name is None:
            name = fn.__name__
        self.funs[name] = fn


class JSONRPC(object):
    def __init__(self):
        self.data = None

    def from_data(self, data):
        """解析数据"""
        self.data = json.loads(data.decode('utf-8'))

    def call_method(self):
        """根据解析的数据，调用对应的方法"""
        method_name = self.data['method_name']
        method_args = self.data['method_args']
        method_kwargs = self.data['method_kwargs']

        res = self.funs[method_name](*method_args, **method_kwargs)
        data = { "res": res }
        return json.dumps(data).encode('utf-8')


class RPCServer(tcpserver.TCPServer, JSONRPC, RPCStub):
    def __init__(self):
        # super(RPCServer, self).__init__() # 多继承的情况下，默认初始化 TCPServer
        # super().__init__()                # 多继承的情况下，默认初始化 TCPServer
        tcpserver.TCPServer.__init__(self)
        JSONRPC.__init__(self)
        RPCStub.__init__(self)

    def loop(self, host='0.0.0.0', port=5000):
        self.bind_listen(host, port)
        print('Server start at', '{}:{}.'.format(host, port))
        while True:
            self.accept_receive_close()

    def process_request(self, data):
        self.from_data(data)
        return self.call_method()