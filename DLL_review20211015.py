# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 13:33:18 2021

@author: men_l
"""

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head 
        while node:
            yield node
            node = node.next
            
        
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        return "The DLL has been created"
    
    def insertDLL(self, value, location):
        if self.head is None:
            return "The DLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = None
                self.head = newNode
            elif location == 1:
                newNode.next = self.tail.next
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode 
                tempNode.next = newNode
    
    def traverseDLL(self):
        if self.head is None:
            return "The DLL does not exist"
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                
    def reverseDLL(self):
        if self.head is None:
            return "The DLL does not exist"
        else:
            node = self.tail
            while node :
                print(node.value)
                node = node.prev
            
    def deleteDLL(self, location):
        if self.head is None:
            return "The DLL does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                tempNode.next = tempNode.next.next                
                tempNode.next.prev = tempNode
    def deleteEntireDLL(self):
        if self.head is None:
            return "The DLL does not exist"
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next        
        self.head = None
        self.tail = None 
        print("The DLL has been deleted")
                
                    
                
        
DLL = DLL()
DLL.createDLL(0)
DLL.insertDLL(1,1)
DLL.insertDLL(2,1)
DLL.insertDLL(3,1)
DLL.insertDLL(4,1)
DLL.insertDLL(5,2)
# DLL.deleteDLL(2)
DLL.deleteEntireDLL()
print([node.value for node in DLL])
# DLL.traverseDLL()
# DLL.reverseDLL()