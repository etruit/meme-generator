# Meme Generator

A simple Flask app that generates memes by combining a selected image with a quote.

## Features

- Load quotes from TXT, CSV, DOCX, and PDF files
- Generate memes with text overlay
- Serve the generated meme image through the Flask app
- Provide a simple web form to create a custom meme

## Project Structure

- `src/app.py` - Flask application entry point that serves random and custom memes.
- `src/meme.py` - Command-line helper for generating memes from an image and quote.
- `src/MemeEngine/` - Meme image generation logic, including text placement and image resizing.
- `src/QuoteEngine/` - Quote ingestion and parsing logic for multiple file formats.
- `src/templates/` - HTML templates for the web UI.
- `src/_data/` - Sample quotes and images used by the app.

## Submodule Roles and Responsibilities

### `src/MemeEngine/meme_engine.py`
- Responsible for creating the final meme image.
- Loads an image, resizes it, overlays quote text, and saves the output.
- Dependencies: Pillow (`PIL`).
- Example:

```python
from MemeEngine.meme_engine import MemeEngine

engine = MemeEngine("./tmp")
path = engine.make_meme("./dog.jpg", "Hello", "World")
print(path)
```

### `src/QuoteEngine/ingestor.py`
- Acts as the dispatcher that selects the correct ingestor based on the file extension.
- Dependencies: none directly; it uses the concrete ingestors.
- Example:

```python
from QuoteEngine.ingestor import Ingestor

quotes = Ingestor.parse("./sample_quotes.txt")
print(quotes)
```

### `src/QuoteEngine/txt_ingestor.py`
- Parses quotes from plain text files.
- Dependencies: none beyond the standard library.
- Example:

```python
from QuoteEngine.txt_ingestor import TxtIngestor

quotes = TxtIngestor.parse("./quotes.txt")
```

### `src/QuoteEngine/csv_ingestor.py`
- Parses quotes from CSV files.
- Dependencies: pandas.
- Example:

```python
from QuoteEngine.csv_ingestor import CsvIngestor

quotes = CsvIngestor.parse("./quotes.csv")
```

### `src/QuoteEngine/docx_ingestor.py`
- Parses quotes from DOCX files.
- Dependencies: python-docx.
- Example:

```python
from QuoteEngine.docx_ingestor import DocxIngestor

quotes = DocxIngestor.parse("./quotes.docx")
```

### `src/QuoteEngine/pdf_ingestor.py`
- Parses quotes from PDF files using `pdftotext` when available.
- Dependencies: subprocess (standard library) and an Xpdf-compatible `pdftotext` binary.
- Example:

```python
from QuoteEngine.pdf_ingestor import PdfIngestor

quotes = PdfIngestor.parse("./quotes.pdf")
```

### `src/QuoteEngine/quote_model.py`
- Defines the `QuoteModel` data structure used throughout the app.
- Dependencies: none.
- Example:

```python
from QuoteEngine.quote_model import QuoteModel

quote = QuoteModel("Hello world", "Ada")
print(quote.body)
print(quote.author)
```

## Setup

1. Create and activate a virtual environment
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

From the project root:

```bash
python src/app.py
```

Then open your browser to:

- `http://127.0.0.1:5000/` for a random meme
- `http://127.0.0.1:5000/create` to create a custom meme

## Run Tests

```bash
pytest
```

## Notes

The PDF quote ingestion uses `pdftotext` from Xpdf when available. If it is not installed, PDF ingestion will return no quotes gracefully.
