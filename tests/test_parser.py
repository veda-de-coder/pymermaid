import pytest
from pymermaid.parsers import FlowchartParser
from pymermaid.models import Diagram, Node, Edge

def test_flowchart_parser():
    parser = FlowchartParser()
    content = """
    A[Start] --> B[Process]
    B --> C[End]
    """
    
    diagram = parser.parse(content)
    assert isinstance(diagram, Diagram)
    assert len(diagram.nodes) == 3
    assert len(diagram.edges) == 2
