import pprint
from server import Server

pp = pprint.PrettyPrinter(indent=2)

def test_create_server():
    server = Server('127.0.0.1', 2345)
    stype, sfamily = (server.s.type, server.s.family)
    host, port = server.s.getsockname()
    assert stype.name == 'SOCK_STREAM' and sfamily.name == 'AF_INET'
    assert host == '127.0.0.1' and port == 2345
    # TODO: check listen()

def test_listen():
    server = Server('127.0.0.2', 3456)
    assert True
