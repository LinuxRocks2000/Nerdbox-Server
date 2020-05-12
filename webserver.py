from serverutils import TCPServer
import importlib, os

class MyServer(ServerListenable):
    def handle_filereq(self,data,connection):
        if os.path.exists(data["reqlocation"]):
            if data["reqlocation"][-3:]==".py":
                importlib.import_module(data["reqlocation"]
        else:
            Headers.broadcast_404(connection)
    def handle_get(self,data,connection):
        self.handle_filereq(data,connection)
n=MyServer(port=8050)
n.run()
