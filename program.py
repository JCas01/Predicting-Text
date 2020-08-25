# Implement the following Node class API.
# If you delete something important, this code is copied in specification.py

class Node:
  def __init__(self, prefix):
    """
    Creates a Node with the given string prefix.
    The root node will be given prefix ''.
    You will need to track:
    - the prefix
    - whether this prefix is also a complete word
    - child nodes
    """
    pass
  
  def get_prefix(self):
    """
    Returns the string prefix for this node.
    """
    pass
  
  def get_children(self):
    """
    Returns a list of child Node objects, in any order.
    """
    pass
  
  def is_word(self):
    """
    Returns True if this node prefix is also a complete word.
    """
    pass
  
  def add_word(self, word):
    """
    Adds the complete word into the trie, causing child nodes to be created as needed.
    We will only call this method on the root node, e.g.
    >>> root = Node('')
    >>> root.add_word('cheese')
    """
    pass
  
  def find(self, prefix):
    """
    Returns the node that matches the given prefix, or None if not found.
    We will only call this method on the root node, e.g.
    >>> root = Node('')
    >>> node = root.find('te')
    """
    pass
  
  def words(self):
    """
    Returns a list of complete words that start with my prefix.
    The list should be in lexicographical order.
    """
    pass


if __name__ == '__main__':
  # Write your test code here. This code will not be run by the marker.

  # The first example in the question.
  root = Node('')
  for word in ['tea', 'ted', 'ten']:
    root.add_word(word)
  node = root.find('te')
  print(node.get_prefix())
  print(node.is_word())
  print(node.words())

  # The second example in the question.
  root = Node('')
  for word in ['inn', 'in', 'into', 'idle']:
    root.add_word(word)
  node = root.find('in')
  print(node.get_prefix())
  children = node.get_children()
  print(sorted([n.get_prefix() for n in children]))
  print(node.is_word())
  print(node.words())

  # The third example in the question.
  with open('the-man-from-snowy-river.txt') as f:
    words = f.read().split()
  root = Node('')
  for word in words:
    root.add_word(word)
  print(root.find('th').words())