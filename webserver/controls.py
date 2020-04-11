import json
class webserver_controller:
    def __init__(self,server):
        self.index={"auth":[self.post_auth,self.get_auth]} ## Commands must have two endpoints, a post and a get
        self.server=server
        self.users={}
        print("Controls initiated")
    def run(self,location,data): ## Location must be everything after "/CONTROLS/"
        '''Location is the location requested, E.g. if the original one was /CONTROLS/auth/login,
the passed location would be auth/login.
Data is the parsed request data.'''
        args=location.split("/")
        if data["reqtype"]=="POST":
            self.index[args[0]][0](args[1:],self.server,data)
        if data["reqtype"]=="GET":
            self.index[args[0]][1](args[1:],self.server,data)
    def post_auth(self,args,server,data):
        print("POST AUTH CALLED")
        print(data)
        d=json.loads(data["content"])
        if args[0]=="login":
            if self.users[args[1]][0]==d["passwd"]: ## Each entry in self.users is a list, with the password and a logged on boolean
                self.users[args[1]][1]==True
    def get_auth(self,args,server):
        
