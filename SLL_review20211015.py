# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 09:18:02 2021

@author: men_l
"""

class Node:
    def __init__(self, value= None):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next 
            
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode 
        else:
            if location == 0:
                newNode.next = self.head 
                self.head = newNode 
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode 
            else:
                tempNode = self.head 
                index = 0
                while index < location -1:
                    tempNode = tempNode.next 
                    index = index +1 
                nextNode = tempNode.next 
                tempNode.next = newNode 
                newNode.next = nextNode
                if self.tail == tempNode: 
                    self.tail = newNode 
    
    def traversalSLL(self):
        if self.head is None:
            return "The SLL does not exist"
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                
    def searchSLL(self, nodeValue):
        if self.head is None:
            print ("The SLL does not exist")
        else:
            node = self.head 
            while node:
                if node.value == nodeValue:
                    return node.value 
                node = node.next 
            return "The nodeValue does not exist"
    
    def deleteSLL(self, location):
        if self.head is None:
            return "The SLL does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next 
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head 
                    while node:
                        if node.next == self.tail:
                            break 
                        node = node.next 
                    node.next = None
                    self.tail = node 
            else:
                tempNode = self.head 
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next 
                    index = index +1
                nextNode = tempNode.next 
                tempNode.next = nextNode.next 
                    
                    
SLL = SLL()
SLL.insertSLL(0,0)
SLL.insertSLL(2,1)
SLL.insertSLL(3,1)
SLL.insertSLL(4,1)
SLL.insertSLL(5,1)
SLL.insertSLL(6,4)
# SLL.searchSLL(2)
SLL.deleteSLL(1)
print([node.value for node in SLL])
# SLL.traversalSLL()
