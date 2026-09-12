from googleapiclient.discovery import build

from drive.auth import get_drive_credentials


def get_drive_service():
    """Create and return an authenticated Google Drive service."""
    credentials = get_drive_credentials()

    return build(
        "drive",
        "v3",
        credentials=credentials
    )
