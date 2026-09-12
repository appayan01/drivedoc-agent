from parsers.extractor import extract_text


def read_document(file_path: str) -> str:
    """
    Read a supported document and return its extracted text.
    """

    try:
        text = extract_text(file_path)

        if not text.strip():
            return "The document contains no extractable text."

        return text

    except Exception as error:
        return f"Could not read document: {error}"
