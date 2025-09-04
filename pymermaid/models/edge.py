class Edge:
    """
    Represents an edge connecting two nodes in a Mermaid diagram.
    """
    def __init__(self, source: str, target: str, label: str = None):
        self.source = source
        self.target = target
        self.label = label
