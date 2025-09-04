import pytest
from pymermaid.renderers import GraphvizRenderer
from pymermaid.models import Diagram, Node, Edge

def test_graphviz_renderer():
    renderer = GraphvizRenderer()
    diagram = Diagram()
    
    # Add test nodes and edges
    diagram.add_node(Node("A", "Start"))
    diagram.add_node(Node("B", "End"))
    diagram.add_edge(Edge("A", "B", "Process"))
    
    output = renderer.render(diagram)
    assert isinstance(output, str)
    assert "digraph" in output
