from typing import List, Dict

from drive.client import get_drive_service


def search_drive(query: str) -> List[Dict]:
    """
    Search Google Drive for files whose names contain the query.
    """

    if not query.strip():
        return []

    service = get_drive_service()

    response = service.files().list(
        q=(
            "trashed = false "
            "and name contains '{query}'"
        ).format(query=query.replace("'", "\\'")),
        fields="files(id, name, mimeType, modifiedTime, webViewLink)",
        pageSize=20,
    ).execute()

    return response.get("files", [])
