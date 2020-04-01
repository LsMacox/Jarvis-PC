from server.app import app
import server.view


class JarvisServer:
    def __init__(self, server_address, port = '8000'):
        self.server_address = server_address
        self.port = port

    def start(self):
        app.run(host=self.server_address, port=self.port)