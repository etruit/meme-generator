# Meme Generator

A simple Flask app that generates memes by combining a selected image with a quote.

## Features

- Load quotes from TXT, CSV, DOCX, and PDF files
- Generate memes with text overlay
- Serve the generated meme image through the Flask app
- Provide a simple web form to create a custom meme

## Project Structure

- `src/app.py` - Flask application entry point
- `src/meme.py` - Command-line helper for generating memes
- `src/MemeEngine/` - Meme image generation logic
- `src/QuoteEngine/` - Quote ingestion and parsing logic
- `src/templates/` - HTML templates for the web UI
- `src/_data/` - Sample quotes and images

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
