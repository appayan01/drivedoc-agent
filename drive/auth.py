import os

from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


def get_drive_credentials():
    """Authenticate the application with Google Drive."""

    load_dotenv()

    credentials = None

    token_file = "token.json"
    client_secret_file = os.getenv(
        "GOOGLE_CLIENT_SECRET_FILE",
        "client_secret.json"
    )

    if os.path.exists(token_file):
        credentials = Credentials.from_authorized_user_file(
            token_file,
            SCOPES
        )

    if not credentials or not credentials.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            client_secret_file,
            SCOPES
        )

        credentials = flow.run_local_server(port=0)

    return credentials
