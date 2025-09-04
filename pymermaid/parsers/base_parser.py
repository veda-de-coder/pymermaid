from abc import ABC, abstractmethod
from ..models import Diagram

class BaseParser(ABC):
    """
    Base class for all Mermaid diagram parsers.
    """
    @abstractmethod
    def parse(self, content: str) -> Diagram:
        """Parse the Mermaid diagram content and return a Diagram object."""
        pass
