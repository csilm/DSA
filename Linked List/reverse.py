from Node import Node

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

def printLinkedList(head):
    current = head
    while(current != None):
        print(current.data)
        current = current.next

print("Initial Linked List : ")
printLinkedList(a)

# a -> b -> c -> d -> e -> f

def reverse_list(head):
  current = head
  prev = None
  while current != None:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev

newHead = reverse_list(a) # f -> e -> d -> c -> b -> a

print("\nLinked List Reversed : ")
printLinkedList(newHead)