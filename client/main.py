import rpcclient
import json


if __name__ == '__main__':
    t = rpcclient.RPCClient()
    t.connect('127.0.0.1', 5000)
    req = {
        'method_name': 'test',
        'method_args': ('args', 1),
        'method_kwargs': {'a': 1}
    }
    t.send(json.dumps(req))
    t.receive()