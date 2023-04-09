import json
import tcpserver


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

        res = getattr(self, method_name)(*method_args, **method_kwargs)
        data = { "res": res }
        return json.dumps(data).encode('utf-8')

    def test(self, *args, **kwargs):
        print("test: args={}, kwargs={}".format(args, kwargs))
        return "rpc 远程调用的函数成功执行，返回对应的值"


class RPCServer(tcpserver.TCPServer, JSONRPC):
    def __init__(self):
        # super(RPCServer, self).__init__() # python2
        super().__init__()    # python3

    def loop(self, host='0.0.0.0', port=5000):
        self.bind_listen(host, port)
        print('Server start at', '{}:{}.'.format(host, port))

        while True:
            self.accept_receive_close()

    def process_request(self, data):
        self.from_data(data)
        return self.call_method()