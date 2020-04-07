import socket
import json
import mimetypes
import os
import controls
from serverutils import ServerListenable

class Server(ServerListenable):
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
        self.send_file_headers(connection,location)
        connection.send(p.read().encode())
        p.close()
        connection.close()
        print("Successfully initiated send_file")
    def handle_get(self,data,connection):
        print("Loading data")
        if data["reqlocation"][0:9]=="/CONTROLS":
            controls.webserver_specialized(self,connection,data)
            connection.close()
        else:
            self.send_file(data,connection)
    def handle_post(self,data,connection):
        if data["reqlocation"][0:9]=="/CONTROLS":
            controls.trigger_top(self,connection,data)
            connection.close()
    def handle_aux(self,req,connection):
        print("Auxiliary initiated")

def begin():
    print("Beginning PID file logging\n")
    pidfile=open("PIDFILE","w+")
    pidfile.write(str(os.getpid()))
    server=Server("",80)
    server.run()
begin()
