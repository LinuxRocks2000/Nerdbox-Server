import socket
import json
import mimetypes
import os
import controls
from serverutils import ServerListenable

class Server(ServerListenable):
    def inittasks(self,host,port):
        self.users={"pinky":["My Password",False]}
        self.cont=controls.webserver_controller(self)
    def handle_post(self,data,connection):
        pass
    def send_file(self,data,connection):
        if data["reqlocation"][0]=="/":
            data["reqlocation"]=data["reqlocation"][1:]
        location="pages/"+data["reqlocation"]
        if os.path.isdir(location): ## Server index.html from a directory
            if location[-1]=="/":
                location+="index.html"
            else:
                location+="/index.html"
        p=open(location)
        self.send_file_headers(connection,mimetypes.guess_type(location)[0])
        connection.send(p.read().encode())
        p.close()
        connection.close()
    def handle_get(self,data,connection):
        try:
            if len(data["reqlocation"])==9 and data["reqlocation"][0:9]=="/CONTROLS":
                self.cont.run(data["reqlocation"][10:],data)
                connection.close()
            else:
                self.send_file(data,connection)
        except Exception as e:
            print(str(e))
    def handle_post(self,data,connection):
        try:
            if data["reqlocation"][0:9]=="/CONTROLS":
                self.cont.run(data["reqlocation"][10:],data)
                connection.close()
        except Exception as e:
            print(str(e))

def begin():
    print("Beginning PID file logging\n")
    pidfile=open("PIDFILE","w+")
    pidfile.write(str(os.getpid()))
    server=Server("",80)
    server.run()
begin()
