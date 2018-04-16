class Block():
    def __init__(self,data):
        self.data  = None
        self.next = None
        self.prev = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
    
    def setData(self,data):
        self.data = data
        return
    
    def setNext(self, block):
        self.next = block
        return
    
    def setPrev(self, block):
        self.prev = block
        return

class Chain():
    def __init__(self):
        self.head = None
        self.top = None

    def addBlock(self, item):
        current = self.head
        if current == None:
            current.setData(item)
            current.setNext(None)
            self.top = current
        else:
            current.setNext(item)
            temp = current
            current = current.getNext()
            current.setPrev(temp)
            current.setNext(None)

    def removeBlock(self,item):
        current = self.top
        while current.getData() != item:
            current = current.getNext()
        previous = current.getPrev()
        nextblock = current.getNext()
        previous.setNext(nextblock)
        nextblock.setPrev(previous)
