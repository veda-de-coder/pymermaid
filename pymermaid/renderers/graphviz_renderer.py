from graphviz import Digraph
from .base_renderer import BaseRenderer
from ..models import Diagram

class GraphvizRenderer(BaseRenderer):
    """
    Renderer that uses Graphviz to generate diagram images.
    """
    def __init__(self, format='png'):
        self.format = format

    def render(self, diagram: Diagram) -> str:
        dot = Digraph(format=self.format)
        
        # Add nodes
        for node in diagram.nodes:
            dot.node(node.id, node.label)
            
        # Add edges
        for edge in diagram.edges:
            dot.edge(edge.source, edge.target, edge.label)
            
        return dot.source
