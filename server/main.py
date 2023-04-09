import rpcserver


def test(*args, **kwargs):
    print("服务器端注册的 test 被调用了")
    print("test: args = {}, kwargs = {}".format(args, kwargs))
    return 'the test function has been called'


if __name__ == '__main__':
    s = rpcserver.RPCServer()
    s.register_function(test)       # 注册函数
    s.loop('127.0.0.1', 5000)       # 要监听的 IP 和端口
