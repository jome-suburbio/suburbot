from __future__ import annotations

from typing import Any

from .availability_parser import find_available_rooms_from_matrix
from .google_sheets_availability_repository import read_availability_matrix


def check_availability(check_in: str, check_out: str) -> dict[str, Any]:
    values = read_availability_matrix()
    return find_available_rooms_from_matrix(values, check_in, check_out)
