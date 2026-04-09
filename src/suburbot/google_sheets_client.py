from __future__ import annotations

import json

from google.oauth2 import service_account
from googleapiclient.discovery import build

from .config import get_env

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def create_google_sheets_client():
    credentials_json = get_env("GOOGLE_SERVICE_ACCOUNT_JSON")

    if credentials_json:
        credentials_info = json.loads(credentials_json)
        credentials = service_account.Credentials.from_service_account_info(
            credentials_info,
            scopes=SCOPES,
        )
    else:
        credentials_path = get_env("GOOGLE_APPLICATION_CREDENTIALS")
        if not credentials_path:
            raise RuntimeError(
                "Set GOOGLE_APPLICATION_CREDENTIALS or GOOGLE_SERVICE_ACCOUNT_JSON"
            )

        credentials = service_account.Credentials.from_service_account_file(
            credentials_path,
            scopes=SCOPES,
        )

    return build("sheets", "v4", credentials=credentials)
