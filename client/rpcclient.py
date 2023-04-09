import json
import tcpclient


class RPCStub(object):
    def __init__(self):
        pass

    def __getattr__(self, item):
        def fn(*args, **kwargs):
            d = {
                'method_name': item,
                'method_args': args,
                'method_kwargs': kwargs
            }
            self.send(json.dumps(d))
            return self.receive()

        setattr(self, item, fn)
        return fn


class RPCClient(tcpclient.TCPClient, RPCStub):
    pass