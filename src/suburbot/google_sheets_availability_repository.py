from __future__ import annotations

from typing import Any

from .config import get_required_env
from .google_sheets_client import create_google_sheets_client


def read_availability_matrix() -> list[list[Any]]:
    spreadsheet_id = get_required_env("GOOGLE_SHEETS_SPREADSHEET_ID")
    tab_name = get_required_env("GOOGLE_SHEETS_TAB_NAME")
    sheets = create_google_sheets_client()
    range_name = f"{tab_name}!A:ZZ"

    print(f"[google-sheets] Reading availability from {range_name}")

    response = (
        sheets.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range=range_name)
        .execute()
    )

    return response.get("values", [])
