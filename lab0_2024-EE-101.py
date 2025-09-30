# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 04:34:37 2025

@author: Nimra
"""
#%%
def foo(string):
    if string[::1]==string[::-1]:      #Reverse string
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")
foo("maam")
#%% (#using stack)
def foo(string):
    stack=[]
    for i in string:
        stack.append(i)
    new_string=""
    while len(stack)!=0:
        new_string+=stack.pop()  #concatenate string
    if new_string==string:
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")
string=input("Enter string:")
foo(string)
#%%
class Stack:
    def __init__(self):
        self.stack=[]
    def push_item(self,item1):
        self.stack.append(item1)  #put item in stack
        print("After pushing,the stack is",self.stack)
    def peek(self):
        if self.is_empty():    #calling is_empty fun to check len of stack
            return None
        else:
            print("After peeking, the element is",self.stack[-1])
    def pop_item(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("The popped item is",self.stack.pop())  #remove last element
    def is_empty(self):
        return len(self.stack)==0
stack=Stack()
stack.push_item(1)
stack.push_item(2)
stack.peek()
stack.pop_item()
stack.is_empty()
