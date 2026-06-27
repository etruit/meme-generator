"""Abstract interface for quote ingestors."""

import os
from abc import ABC, abstractmethod
from typing import List, Set

try:
    from .quote_model import QuoteModel
except ImportError:  # pragma: no cover
    from quote_model import QuoteModel


class IngestorInterface(ABC):
    """Define the interface for quote ingestors."""

    allowed_extensions: Set[str] = set()

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Return True if the ingestor can process the given file."""
        return os.path.splitext(path)[1].lower() in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse and return quotes from the given file path."""
