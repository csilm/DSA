from Node import Node

# Nodes
first = Node("A")
second = Node("B")
third = Node("C")
four = Node("D")

# Node Links
first.next = second
second.next = third
third.next = four

list = []

def addLinkedListinArray(head):
    if head == None: return
    list.append(head.data) # adding Linked List values in Array
    addLinkedListinArray(head.next)

addLinkedListinArray(first)
print(list)