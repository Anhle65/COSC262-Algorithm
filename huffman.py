"""An incomplete Huffman Coding module, for use in COSC262.
   Richard Lobb, April 2021.
"""
import re
import heapq

HAS_GRAPHVIZ = True
try:
    from graphviz import Graph
except ModuleNotFoundError:
    HAS_GRAPHVIZ = False

class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count,
       minimum character in the tree, and left and right subtrees, assumed to be
       the '0' and '1' children respectively. The frequency count of the node
       is the sum of the children counts and its minimum character (min_char)
       is the minimum of the children min_chars.
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.count = left.count + right.count
        self.min_char = min(left.min_char, right.min_char)

    def __repr__(self, level=0):
        return ((2 * level) * ' ' + f"Node({self.count},\n" +
            self.left.__repr__(level + 1) + ',\n' +
            self.right.__repr__(level + 1) + ')')

    def is_leaf(self):
        return False

    def plot(self, graph):
        """Plot the tree rooted at self on the given graphviz graph object.
           For graphviz node ids, we use the object ids, converted to strings.
        """
        graph.node(str(id(self)), str(self.count)) # Draw this node
        if self.left is not None:
            # Draw the left subtree
            self.left.plot(graph)
            graph.edge(str(id(self)), str(id(self.left)), '0')
        if self.right is not None:
            # Draw the right subtree
            self.right.plot(graph)
            graph.edge(str(id(self)), str(id(self.right)), '1')


class Leaf:
    """A leaf node in a Huffman encoding tree. Contains a character and its
       frequency count.
    """
    def __init__(self, count, char):
        self.count = count
        self.char = char
        self.min_char = char

    def __repr__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True

    def plot(self, graph):
        """Plot this leaf on the given graphviz graph object."""
        label = f"{self.count},{self.char}"
        graph.node(str(id(self)), label) # Add this leaf to the graph


class HuffmanTree:
    """Operations on an entire Huffman coding tree.
    """
    def __init__(self, root=None):
        """Initialise the tree, given its root. If root is None,
           the tree should then be built using one of the build methods.
        """
        self.root = root

    def encode(self, text):
        """Return the binary string of '0' and '1' characters that encodes the
           given string text using this tree.
        """
        dict_char = self.dict_encoding_char(self.root)
        binary_string = ''
        for char in text:
            binary_string += dict_char[char]
        return binary_string

    def dict_encoding_char(self, current_node, code = '', dict_char = {}):
        if current_node.is_leaf():
            dict_char[current_node.char] = code
        else:
            self.dict_encoding_char(current_node.left, code + '0')
            self.dict_encoding_char(current_node.right, code + '1')
        return dict_char

    def decode(self, binary):
        """Return the text string that corresponds the given binary string of
           0s and 1s
        """
        result = ''
        current_node = self.root
        for char in binary:
            if char == "0":
                next_node = current_node.left
            else:
                next_node = current_node.right
            if next_node.is_leaf():
                result += next_node.char
                current_node = self.root
            else:
                current_node = next_node
        return result
    def plot(self):
        """Plot the tree using graphviz, rendering to a PNG image and
           displaying it using the default viewer.
        """
        if HAS_GRAPHVIZ:
            g = Graph()
            self.root.plot(g)
            g.render('tree', format='png', view=True)
        else:
            print("graphviz is not installed. Call to plot() aborted.")

    def __repr__(self):
        """A string representation of self, delegated to the root's repr method"""
        return repr(self.root)

    def build_from_freqs(self, freqs):
        """Define self.root to be the Huffman tree for encoding a set of characters,
           given a map from character to frequency.
        """
        keys = freqs.keys()
        list_leaves= []
        list_freq= []
        for char in keys:
            list_leaves.append(Leaf(freqs[char], char))
            list_freq.append(freqs[char])
        if len(list_freq) == 1:
            self.root = list_leaves.pop()
        while len(list_freq) > 1:
            sorted_list = sorted(list_freq, reverse=True)
            minimum = sorted_list.pop()
            for i in list_leaves:
                if i.count == minimum:
                    list_leaves.remove(i)
                    minimum_char = i.min_char
                    branch1 = i
                    break
            second_min = sorted_list.pop()
            for j in list_leaves:
                if j.count == second_min:
                    list_leaves.remove(j)
                    second_min_char = j.min_char
                    branch2 = j
                    break
            if minimum == second_min:
                minimum = minimum_char
                second_min = second_min_char
            if minimum < second_min:
                self.root = Node(branch1, branch2)
            else:
                self.root = Node(branch2, branch1)
            list_freq = sorted_list
            list_freq.append(self.root.count)
            list_leaves.append(self.root)
        return tree

    def build_from_string(self, s):
        """Convert the string representation of a Huffman tree, as generated
           by its __str__ method, back into a tree (self). There are no syntax
           checks on s so it had better be valid!
        """
        s = s.replace('\n', '')  # Delete newlines
        s = re.sub(r'Node\(\d+,', 'Node(', s)
        self.root = eval(s)

# The example from the notes
 	

# Example from Q11
freqs = {
   'p': 27,
   'q': 11,
   'r': 27,
   'u': 8,
   't': 5,
   's': 3}
tree = HuffmanTree()
tree.build_from_freqs(freqs)
print(tree)