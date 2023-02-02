class Node(object):
    """This class represents a node in a graph."""
    
    def init(self, label: str=None):
        """
        Initialize a new node.
        
        Args:
            label: the string identifier for the node
        """
        self.label = label
        self.children = []
        
    def lt(self,other):
        """
        Perform the less than operation (self < other).
        
        Args:
            other: the other Node to compare to
        """
        return (self.label < other.label)
    
    def gt(self,other):
        """
        Perform the greater than operation (self > other).
        
        Args:
            other: the other Node to compare to
        """
        return (self.label > other.label)
    
    def repr(self):
        """Return a string form of this node."""
        return '{} -> {}'.format(self.label, self.children)
    
    def add_child(self, node, cost=1):
        """
        Add a child node to this node.
        
        Args:
            node: the node to add to the children
            cost: the cost of the edge (default 1)
        """
        edge = Edge(self, node, cost)
        self.children.append(edge)
    
    
class Edge(object):
    """This class represents an edge in a graph."""
    
    def init(self, source: Node, destination: Node, cost: int=1):
        """
        Initialize a new edge.
        
        Args:
            source: the source of the edge
            destination: the destination of the edge
            cost: the cost of the edge (default 1)
        """
        self.source = source
        self.destination = destination
        self.cost = cost
    
    def repr(self):
        """Return a string form of this edge."""
        return '{}: {}'.format(self.cost, self.destination.label)
S = Node('S')
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
G = Node('G')
S.add_child(A, 1)
S.add_child(G, 12)

A.add_child(B, 3)
A.add_child(C, 1)
