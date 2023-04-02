from Node import Node

# Sum of linked List recursive function
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e


def sum_list(head):
    if head == None:
        return 0
    values = head.data + sum_list(head.next)
    return values


x = sum_list(a)
print(x)

