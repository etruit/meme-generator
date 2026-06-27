"""CSV-based quote ingestion."""

from typing import List

import pandas as pd

try:
    from .ingestor_interface import IngestorInterface
    from .quote_model import QuoteModel
except ImportError:  # pragma: no cover
    from ingestor_interface import IngestorInterface
    from quote_model import QuoteModel


class CsvIngestor(IngestorInterface):
    """Parse quotes from CSV files."""

    allowed_extensions = {".csv"}

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quote rows from a CSV file."""
        quotes: List[QuoteModel] = []
        data_frame = pd.read_csv(path)

        for _, row in data_frame.iterrows():
            body = str(row.get("body", "")).strip()
            author = str(row.get("author", "")).strip()
            if body and author:
                quotes.append(QuoteModel(body, author))
        return quotes
