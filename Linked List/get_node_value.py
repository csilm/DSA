class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

def get_node_value(head, index):
  c_index = 0
  get_value(head, c_index, index)
  

def get_value(head, c_index, index):
  if head == None: return
  if c_index == index:
    wvalue = head.val
    print(wvalue)
  c_index = c_index+1
  get_value(head.next, c_index, index)

get_node_value(a, 2)