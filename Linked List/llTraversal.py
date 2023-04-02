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

# Traversal through the linked list
def printLinkedList(head):
    current = head
    print("Linked List :")
    while(current != None):
        print(current.data)
        current = current.next

printLinkedList(first)

# traversal through the linked list (recursion)
print("\nLinked List using Recursion: ")
def printLLrecursion(node):
    if node == None : return
    print(node.data)
    printLLrecursion(node.next)

printLLrecursion(first)