"""
Main application logic for PyMermaid.
"""
from .parsers import FlowchartParser
from .renderers import GraphvizRenderer

def parse_and_render(content: str, format: str = 'png') -> str:
    """
    Parse Mermaid content and render it in the specified format.
    """
    parser = FlowchartParser()
    renderer = GraphvizRenderer(format=format)
    
    diagram = parser.parse(content)
    return renderer.render(diagram)
