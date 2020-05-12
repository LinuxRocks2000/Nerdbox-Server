class HTMLELement:
    def __init__(self,elemtype,properties={},parent=None,children=[]):
        self.parent=parent
        self.children=children
        self.elemtype=elemtype
        self.properties=properties
    def setProperty(self,prop,value):
        self.properties[prop]=value
    def delProperty(self,prop):
        del self.properties[prop]
    def getProperty(self,prop):
        return self.properties[prop]
    def addChild(self,child):
        self.children.append(child)
    def recursivelyFindElement(self,prop,value):
        
class HTMLPage:
    
