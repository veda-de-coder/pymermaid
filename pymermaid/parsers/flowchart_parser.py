from lark import Lark, Transformer
from .base_parser import BaseParser
from ..models import Diagram, Node, Edge

class FlowchartParser(BaseParser):
    """
    Parser for Mermaid flowchart diagrams.
    """
    def __init__(self):
        with open('flowchart.lark', 'r') as f:
            self.parser = Lark(f.read())

    def parse(self, content: str) -> Diagram:
        tree = self.parser.parse(content)
        transformer = FlowchartTransformer()
        return transformer.transform(tree)
