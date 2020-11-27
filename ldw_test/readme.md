mqtt  客户端请求接口

config 配置文件
cert  证书存放
sub_cli.py / pub_cli.py 本地验证测试
test_ca_mqtt.py  证书和用户添加测试

1.连接服务ip 和port（默认1883）
2.有证书认证的需要认证，通过tls_set函数设置证书，以及通道版本
3.设置用户名密码连接
4.返回连接结果connect code

返回值  16进制  含义
0   0x00    Connection Accepted   正常连接
1   0x01    Connection Refused: unacceptable protocol version   协议版本不被接受
2   0x02    Connection Refused: identifier rejected   连接拒绝
3   0x03    Connection Refused: server unavailable   服务不可用
4   0x04    Connection Refused: bad user name or password    账号密码错误
5   0x05    Connection Refused: not authorized    权限不足
6-255       Reserved for future use

5.通过subscribe指定订阅的topic 

6.on_message接收到server发布的内容后，保存为一个json

最终：
mqtt_client.py  # 接口函数类
get_nome_info.py  # 执行以调用接口
