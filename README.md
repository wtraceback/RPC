# RPC

基于 Python Socket 模块实现的 RPC


## 目录结构
```bash
│
├── client                     # 客户端
│   ├── main.py                # 客户端入口文件
│   ├── rpcclient.py           # 对外暴露的接口
│   └── tcpclient.py           # 网络传输 TCP Client
├── server                     # 服务器端
│   ├── main.py                # 服务器端入口文件
│   ├── rpcserver.py           # 对外暴露的接口
└── └── tcpserver.py           # 网络传输 TCP Server
```


## 项目运行
```bash
# 克隆项目
$ git clone https://github.com/wtraceback/RPC.git
# 切换至目录
$ cd RPC


# 服务器端
cd server           # 切换进 server 目录
python main.py      # 启动服务器


# 客户端
cd client           # 切换进 client 目录
python main.py      # 启动客户端，向服务器端发送请求并接收响应
```