"""DOCX-based quote ingestion."""

from typing import List

import docx

try:
    from .ingestor_interface import IngestorInterface
    from .quote_model import QuoteModel
except ImportError:  # pragma: no cover
    from ingestor_interface import IngestorInterface
    from quote_model import QuoteModel


class DocxIngestor(IngestorInterface):
    """Parse quotes from DOCX files."""

    allowed_extensions = {".docx"}

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from a DOCX file."""
        quotes: List[QuoteModel] = []
        document = docx.Document(path)

        for paragraph in document.paragraphs:
            text = paragraph.text.strip()
            if not text or " - " not in text:
                continue
            body, author = text.rsplit(" - ", 1)
            quotes.append(QuoteModel(body.strip(), author.strip()))
        return quotes
