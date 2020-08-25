# Predicting-Text

[Older mobile phones](https://en.wikipedia.org/wiki/T9_(predictive_text)) have a feature called [predictive text](https://en.wikipedia.org/wiki/Predictive_text) that allows the phone to guess what word the user might be typing, based on the keys pressed so far.

How does the phone know what words to suggest to the user? This problem is typically solved using a [prefix tree](https://en.wikipedia.org/wiki/Trie). A trie (pronounced "try") is a recursive data structure that consists of nodes, each storing characters that make up part (or all) of a word.

The nodes are connected together in a tree shape, with each node containing many child nodes. This is is why we call this data structure recursive. Each branch to a child node is associated with a single character, which concatenates to the prefix in the child node.

Here is an example of a trie, with some sample words:

![Trie](/trie.svg)

A trie for keys a, to, tea, ted, ten, i, in, and inn.

If you are given a certain prefix of characters, say, `te`, you can find all the words that start with that prefix by starting at the root node and using each letter from the prefix to traverse through the tree.

Whenever you encounter a highlighted node, this indicates the stored prefix represents a whole word. In the example above, i is such a node. It is both a complete word, as well as being a prefix for other words.

Once you have reached the node that stores the relevant prefix, you can find all of the words that begin with that prefix by visiting all the nodes that branch off that node. For the example prefix te we can predict words: `tea`, `ted`, and `ten`.

Here is a summary of a Node:

* A node stores a prefix.
* A node also stores a Boolean flag that is true when the prefix is also a complete word.
* A node has multiple child nodes, each associated with a single letter.
* The top node in the trie is called the root node.

Your task is to implement the Node class that conforms to the API we have given you (in the editor). This API will allow us to create a trie using some sample words, and then predict some text.

Here is an example of how we will use your `Node` class:

```python
root = Node('')
for word in ['tea', 'ted', 'ten']:
  root.add_word(word)
node = root.find('te')
print(node.get_prefix())
print(node.is_word())
print(node.words())
```
which should output:
```
te
False
['tea', 'ted', 'ten']
```

Here is another example:
```python
root = Node('')
for word in ['inn', 'in', 'into', 'idle']:
  root.add_word(word)
node = root.find('in')
print(node.get_prefix())
children = node.get_children()
print(sorted([n.get_prefix() for n in children]))
print(node.is_word())
print(node.words())
```
which should output
```
in
['inn', 'int']
True
['in', 'inn', 'into']
```
This final example demonstrates how we can use a larger text with punctuation and arbirtary characters (The Man From Snowy River) to predict words:
```python
with open('the-man-from-snowy-river.txt') as f:
  words = f.read().split()
root = Node('')
for word in words:
  root.add_word(word)
print(root.find('th').words())
```
which should output
```
['that', 'the', 'their', 'them', 'them,', 'then', 'there,', 'they', 'thickly,', 'think', 'thoroughbred', 'those', 'thousand', 'three', 'throw', 'thunder']
```

## Important
We will be testing your class by constructing instances of your `Node` class and invoking their methods. Any code inside the `if __name__ == '__main__':` block will not affect the marking.
