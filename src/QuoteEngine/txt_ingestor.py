"""Plain-text quote ingestion."""

from typing import List

try:
    from .ingestor_interface import IngestorInterface
    from .quote_model import QuoteModel
except ImportError:  # pragma: no cover
    from ingestor_interface import IngestorInterface
    from quote_model import QuoteModel


class TxtIngestor(IngestorInterface):
    """Parse quotes from plain-text files."""

    allowed_extensions = {".txt"}

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from a text file."""
        quotes: List[QuoteModel] = []
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line or " - " not in line:
                    continue
                body, author = line.rsplit(" - ", 1)
                quotes.append(QuoteModel(body.strip(), author.strip()))
        return quotes
