from abc import ABC, abstractmethod
from ..models import Diagram

class BaseRenderer(ABC):
    """
    Base class for all diagram renderers.
    """
    @abstractmethod
    def render(self, diagram: Diagram) -> str:
        """
        Render the diagram and return the output as a string.
        """
        pass
