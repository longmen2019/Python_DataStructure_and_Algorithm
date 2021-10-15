class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
class CSLL:
    def __init__(self):
        self.head = None
#         self.tail.next = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
                    
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The node has been created"
        
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The node does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                return "The node has been inserted"
    
    def traverseCSLL(self):
        if self.head is None:
            return "The CSLL does not exist"
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                if node == self.tail.next:
                    break
                    
    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "The CSLL does not exist"
        else:
            node = self.head 
            while node:
                if node.value == nodeValue:
                    return node.value
                node = node.next                 
                if node == self.tail.next:
                    break
            return "The node value does not exist"  
               
    def deleteCSLL(self, location):
        if self.head is None:
            return "The CSLL does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail.next = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location ==1:
                if self.head == self.tail:
                    self.head = None
                    self.tail.next = None
                    self.tail = None
                else:                    
                    node = self.head
                    while node:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node

            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index = index + 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                
    def deleteEntireCSLL(self):
        if self.head is None:
            return "The CSLL does not exist"
        else:
            self.head = None
            self.tail.next = None
            self.tail = None
            
                    
                    
        
        
CSLL = CSLL()
CSLL.createCSLL(0)
CSLL.insertCSLL(1,1)
CSLL.insertCSLL(2,1)
CSLL.insertCSLL(3,1)
CSLL.insertCSLL(4,1)
CSLL.deleteCSLL(1)
CSLL.deleteEntireCSLL()
print([node.value for node in CSLL])
# CSLL.traverseCSLL()
# CSLL.searchCSLL(6)
