from typing import List
from .node import Node
from .edge import Edge

class Diagram:
    """
    Base class for all Mermaid diagrams.
    """
    def __init__(self):
        self.nodes: List[Node] = []
        self.edges: List[Edge] = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def add_edge(self, edge: Edge):
        self.edges.append(edge)
