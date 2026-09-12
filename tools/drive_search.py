from typing import List, Dict


def search_drive(query: str) -> List[Dict]:
    """
    Search Google Drive for files matching a query.

    Google Drive API integration will be added next.
    """

    if not query.strip():
        return []

    return [
        {
            "name": "Placeholder document",
            "file_id": "placeholder",
            "mime_type": "text/plain",
        }
    ]
