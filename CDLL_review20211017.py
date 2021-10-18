# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 09:15:11 2021

@author: men_l
"""

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class CDLL:
    def __init__(self):
        self.head = None           
        self.tail = None
#         self.tail.next = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    def createCDLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        node.prev = node
        self.head = node
        self.tail = node
        return "The DLL has been created"
    
    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode 
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev= newNode
                self.tail.next = newNode
                self.tail = newNode 
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index = index + 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
                return "The node has been successfully inserted"
    
    def traverseCDLL(self):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
                    
    def reverseCDLL(self):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
                if tempNode == self.tail.next:
                    break
    def deleteCDLL(self, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            if location == 0:
                if self.head == self.tail :
                    self.head.prev = None
                    self.head = None
                    self.head.next = None
                    self.tail.next = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head = None
                    self.head.next = None
                    self.tail.next = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                tempNode.next = tempNode.next.next
                tempNode.prev = tempNode #this line does not change anything
                tempNode.next.prev = tempNode
                
    def deleteEntireCDLL(self):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next                
            self.head = None            
            self.tail = None
            
                
                    
                    
                
CDLL = CDLL()
CDLL.createCDLL(0)
CDLL.insertCDLL(1,1)
CDLL.insertCDLL(2,1)
CDLL.insertCDLL(3,1)
CDLL.insertCDLL(4,1)
CDLL.insertCDLL(5,1)
# CDLL.deleteCDLL(2)
CDLL.deleteEntireCDLL()
print([node.value for node in CDLL])
# CDLL.traverseCDLL()
# CDLL.reverseCDLL()