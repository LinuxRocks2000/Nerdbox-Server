from serverutils import ServerListenable, Controls

class NerdController(Controls):
    def inittasks(self):
        print("Controls initiafied")
    def on_get(self,data):
        print("On get called")
    def on_post(self,data):
        print("On post called")
class MyServer(ServerListenable):
    def handle_get(self,data,connection):
        print(data["reqlocation"])
n=MyServer(port=8050,controls=NerdController)
n.run()
