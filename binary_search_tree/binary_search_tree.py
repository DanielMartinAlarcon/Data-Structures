class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value >= self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    else:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    if target >= self.value:
      if self.right == None:
        return False
      else:
        return self.right.contains(target)
    if target < self.value:
      if self.left == None:
        return False
      else:
        return self.left.contains(target)


  def get_max(self):
    if self.right is None:
      return self.value
    else:
      return self.right.get_max()

  def for_each(self, cb):
    cb(self.value)
    if self.left is not None:
      self.left.for_each(cb)
    if self.right is not None:
      self.right.for_each(cb)