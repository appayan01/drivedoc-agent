from pathlib import Path

from parsers.pdf_parser import extract_pdf_text
from parsers.docx_parser import extract_docx_text
from parsers.txt_parser import extract_txt_text


def extract_text(file_path: str) -> str:
    """Extract text using the parser appropriate for the file type."""

    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return extract_pdf_text(file_path)

    if extension == ".docx":
        return extract_docx_text(file_path)

    if extension == ".txt":
        return extract_txt_text(file_path)

    raise ValueError(f"Unsupported file type: {extension}")
