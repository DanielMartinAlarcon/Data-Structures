class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    top = self.storage.pop(0)
    self._sift_down(0)

    return top

  def get_max(self):
    if len(self.storage) == 0:
      return None
    else:
      return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    import math
    if index == 0:
      pass
    else:
      parent_idx = math.floor((index-1)/2)
      if self.storage[parent_idx] < self.storage[index]:
        self.storage[parent_idx], self.storage[index] = self.storage[index], self.storage[parent_idx]
      self._bubble_up(parent_idx)

  def _sift_down(self, index):
    import numpy as np
    if len(self.storage) == 0:
      return None

    l_idx = 2*index + 1
    r_idx = 2*index + 2

    l = self.storage[l_idx] if l_idx < len(self.storage) else -(np.inf)
    r = self.storage[r_idx] if r_idx < len(self.storage) else -(np.inf)
    parent = self.storage[index]

    largest_child = max(l, r)
    largest_child_idx = l_idx if largest_child == l else r_idx

    if parent < largest_child:
      self.storage[index], self.storage[largest_child_idx] = largest_child, parent

    if l > -(np.inf):
      self._sift_down(l_idx)

    if r > -(np.inf):
      self._sift_down(r_idx)
