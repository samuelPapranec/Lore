import socket

def finally_instead_of_context_manager(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.sendall(b'Hello, world')
    finally:
        s.close()

finally_instead_of_context_manager('127.0.0.1', 8000)
