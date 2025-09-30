# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 22:43:32 2025

@author: Nimra
"""

class  Node: 
    def __init__(self,data=None):  #constructor
        self.data=data
        self.next=None
class sLList:
    def __init__(self):
        self.head=Node()    #Sentinal node
        self.length=0
    def insert_at_first(self,item):
        new_node=Node(item)       #Make new node
        new_node.next=self.head.next
        self.head.next=new_node
        self.length+=1
    def insert_at_last(self,item):
        new_node=Node(item)
        curr=self.head
        while curr.next is not None:
            curr=curr.next     #Moves forward
        curr.next=new_node
        self.length+=1
    def insert_at_ith(self,index,item):
        if index<0 or index>self.length:
            raise(ValueError)
        new_node=Node(item)
        curr=self.head
        position=0
        while position<index:
            curr=curr.next
            position+=1
        new_node.next=curr.next
        curr.next=new_node
        self.length+=1
    def cal_length(self):
        return self.length
    def get_first(self):
        if self.head.next is None:
            return None
        else:
            element=self.head.next.data   #Gives value
            return element
    def print_list(self):
        curr=self.head.next  #Original list begins from here
        while curr:
            print(curr.data,"->",end=" ")
            curr=curr.next
        print("None")
Linked_List=sLList() 
Linked_List.insert_at_first(15) 
Linked_List.insert_at_first(10) 
Linked_List.insert_at_first(5) 
Linked_List.insert_at_last(25) 
Linked_List.insert_at_ith(3,20) 
Linked_List.print_list()
print("The length of Linked List is",Linked_List.cal_length())
print("The first elemnt of a list is",Linked_List.get_first())
 
        