import socket

class NetworkInterfaceLayer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect((self.ip, self.port))

    def accept(self):
        self.sock.bind((self.ip, self.port))
        self.sock.listen(1)
        conn, addr = self.sock.accept()
        return conn

    def send(self, conn, data):
        conn.sendall(data.encode())

    def receive(self, conn, buffer_size=1024):
        return conn.recv(buffer_size).decode()

    def close(self):
        self.sock.close()
