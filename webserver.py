from serverutils import ServerListenable, Controls

class NerdController(Controls):
    def inittasks(self):
        print("Controls initiafied")
    def onget(self,data):
        print("On get called")
    def onpost(self,data):
        print("On post called")
class MyServer:
    def handle_get(self,data,connection):
        print("get called")
n=MyServer(controls=NerdController)
n.run()
