class Node:
    """
    Represents a node in a Mermaid diagram.
    """
    def __init__(self, id: str, label: str = None):
        self.id = id
        self.label = label or id
        self.attributes = {}
