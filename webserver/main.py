import socket
import json
import mimetypes
import os
class ServerListenable:
    def __init__(self,host,port):
        self.sckt=socket.socket()
        self.sckt.bind((host,port))
    def run(self):
        self.sckt.listen(5)
        while True:
            self.connection, (client_host, client_port) = self.sckt.accept()
            recieved=self.connection.recv(1024)
            try:
                ppt=self.parseRequest(recieved)
                if ppt["reqtype"]=="POST":
                    self.handle_post(ppt,self.connection)
                elif ppt["reqtype"]=="GET":
                    self.handle_get(ppt,self.connection)
                else:
                    raise Exception
            except Exception as e:
                self.handle_aux(recieved,self.connection)
                print(e)
            self.connection.close()
    def handle_post(self,data,connection):
        pass
    def handle_get(self,data,connection):
        pass
    def handle_aux(self,req,connection):
        pass
    def parseRequest(self,data):
        copy=data.decode()
        copy=copy.replace("\r","")
        copy=copy.split("\n")
        toreturn={}
        if copy[0][0:4]=="GET ":
            toreturn["reqtype"]="GET"
        if copy[0][0:4]=="POST":
            toreturn["reqtype"]="POST"
        toreturn["reqlocation"]=copy[0].split(" ")[1]
        toreturn["useragent"]=copy[2].split(" ")[1]
        toreturn["mimetype"]=(copy[3][8:]).split(",")
        toreturn["langtype"]=(copy[4][17:]).split(",")
        if toreturn["reqtype"]=="POST":
            toreturn["data"]=json.loads(copy[13])
        return toreturn
    def send_file_headers(self, connection, request_file):
        connection.send("HTTP/1.0 200 OK\n".encode())
        bork = "Content-Type: " + mimetypes.guess_type(request_file)[0] + "\n"
        connection.send(bork.encode())
        connection.send("\n".encode())


class Server(ServerListenable):
    def handle_post(self,data,connection):
        pass
    def handle_get(self,data,connection):
        p=open("index.html")
        self.send_file_headers(connection,"index.html")
        connection.send(p.read().encode())
        p.close()
        connection.close()
    def handle_aux(self,req,connection):
        pass

server=Server("",80)
server.run()
