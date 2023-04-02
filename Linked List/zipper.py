from Node import Node

s = Node("s")
t = Node("t")
s.next = t
# s -> t

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
one.next = two
two.next = three
three.next = four
# 1 -> 2 -> 3 -> 4

# Traversal through the linked list
def printLinkedList(head):
    current = head
    while (current != None):
        print(current.data)
        current = current.next


# Zipper List using Loop
def zipper_listsLoop(head_1, head_2):
    first_node = head_1
    count = 0
    while head_1 != None and head_2 != None:
        if(count % 2 == 0):
            temp1 = head_1.next
            head_1.next = head_2
            head_1 = temp1
        if(count % 2 != 0):
            temp2 = head_2.next
            head_2.next = temp1
            head_2 = temp2
        count = count + 1
    printLinkedList(first_node)

# zipper_listsLoop(s, one)


#Zipper List using recursion
def zipper_lists_rec(head_1, head_2):
    first_node = head_1
    count = 0
    zip_the_list(head_1, head_2, count)
    printLinkedList(first_node)

def zip_the_list(head_1, head_2, count):
    if head_1 == None or head_2 == None: return
    if count % 2 == 0 :
        temp = head_1.next
        head_1.next = head_2
        head_1 = temp
    if count % 2 != 0:
        temp = head_2.next
        head_2.next = head_1
        head_2 = temp
    
    count = count+1
    return zip_the_list(head_1, head_2, count)

zipper_lists_rec(s, one)

# Note: Run them Separately
