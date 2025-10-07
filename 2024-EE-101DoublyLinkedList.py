# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 22:03:27 2025

@author: Nimra
"""

class Node:
    def __init__(self,item=None):  #constructor
        self.item=item
        self.prev=None
        self.next=None
class DLList:
    def __init__(self):
        self.head=Node(None)     #instance of class Node
        self.length=0
    def insert_first(self,item):
        new_node=Node(item)
        new_node.next=self.head.next
        if self.head.next:       #if list is not empty
            self.head.next.prev=new_node
        new_node.prev=self.head
        self.head.next=new_node
        self.length+=1
    def insert_last(self,item):
        new_node=Node(item)
        curr=self.head
        while curr.next is not None:
            curr=curr.next
        curr.next=new_node
        new_node.prev=curr
        self.length+=1
    def del_first(self):
        if self.head.next is None:
            return None
        del_node=self.head.next
        self.head.next=del_node.next
        if del_node.next:
            del_node.next.prev=self.head
        self.length-=1
    def del_last(self):
        curr=self.head
        if self.head.next is None:
            return None
        while curr.next is not None:
            curr=curr.next
        curr.prev.next=None  #Previous pointer is None
        self.length-=1
    def get_length(self):
        return self.length
    def to_list(self):
        self.List=[]
        curr=self.head.next
        while curr is not None:
            self.List.append(curr.item)
            curr=curr.next
        return self.List
    def is_empty(self):
        return self.head.next is None
    def get_at(self,index):
        curr=self.head.next
        position=0
        while position!=index and curr is not None:
            curr=curr.next
            position+=1
        if curr is not None:
            print("The elemnt at",index,"position is",curr.item)
        else:
            print("Index out of range")
    def display_list(self):
        curr=self.head.next
        while curr:
            print(curr.item,"->",end="")
            curr=curr.next
        print("None")
d=DLList()
print(d.is_empty())
print("List:",d.to_list())
print("After inserting first node:")
d.insert_first(3)
d.insert_first(2)
d.insert_first(1)
d.display_list()
print(d.is_empty())
print("List:",d.to_list())
print("After inserting Last node:")
d.insert_last(4)
d.insert_last(5)
d.insert_last(6)
d.display_list()
print(d.is_empty())
print("List:",d.to_list())
print("After deleting first node:")
d.del_first()
d.display_list()
print(d.is_empty())
print("List:",d.to_list())
print("After deleting last node:")
d.del_last()
d.display_list()
d.get_at(2)
print(d.is_empty())
print("List:",d.to_list())
print("The length of a list is",d.get_length())
print(d.is_empty())
print("List:",d.to_list())
               
        
        