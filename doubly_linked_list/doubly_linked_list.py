"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if self.head is None:
      self.head = ListNode(value, prev=None, next=None)
      self.tail = self.head
      self.length += 1
    elif self.head == self.tail:
      self.head.insert_before(value)
      self.head = self.head.prev
      self.tail = self.head.next
      self.length += 1
    else:
      self.head.insert_before(value)
      self.head = self.head.prev
      self.length += 1

  def remove_from_head(self):
    if self.head is None:
      return None
    elif self.head.next is None:
      old_head = self.head
      self.head = None
      self.tail = None
      self.length -= 1
      return old_head.value
    else:
      old_head = self.head
      self.head.delete()
      self.head = old_head.next
      self.length -= 1
      return old_head.value

  def add_to_tail(self, value):
    if self.tail is None:
      self.head = ListNode(value, prev=None, next=None)
      self.tail = self.head
      self.length += 1
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next
      self.length += 1

  def remove_from_tail(self):
    if self.tail is None:
      return None
    elif self.tail.prev is None:
      old_tail = self.tail
      self.head = None
      self.tail = None
      self.length -= 1
      return old_tail.value
    else:
      old_tail = self.tail
      self.tail = old_tail.prev
      self.length -= 1
      return old_tail

  def move_to_front(self, node):
    if self.head == node:
      pass
    else:
      old_head = self.head
      node.delete()
      old_head.prev = node
      self.head = node
      self.head.next = old_head
      if self.tail == node:
        self.tail = node.prev

  def move_to_end(self, node):
    if self.tail == node:
      pass
    else:
      old_tail = self.tail
      node.delete()
      self.head = node.next
      old_tail.next = node
      node.next = None
      node.prev = old_tail
      self.tail = node
      if self.head == node:
        self.head = node.next

  def delete(self, node):
    self.length -= 1
    node.delete()
    if self.head == node:
      self.head = node.next
    if self.tail == node:
      self.tail = node.prev
    
    
  def get_max(self):
    current_max = self.head.value
    current_node = self.head
    while True:
      if current_node.value > current_max:
        current_max = current_node.value 
      if current_node == self.tail:
        break
      else:
        current_node = current_node.next
    
    return current_max

