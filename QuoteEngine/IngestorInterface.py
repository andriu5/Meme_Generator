from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """Abstract base class, IngestorInterface defines two methods with the 
    following class method signatures:

    def can_ingest(cls, path: str) -> boolean
    def parse(cls, path: str) -> List[QuoteModel]
    """
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass