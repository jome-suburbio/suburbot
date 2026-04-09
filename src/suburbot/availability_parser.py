from __future__ import annotations

from typing import Any

from .date_range import get_nights_between

AVAILABLE_VALUES = {"disponible", "available", "libre"}


def _normalize_cell(value: Any) -> str:
    return str(value or "").strip().lower()


def find_available_rooms_from_matrix(
    values: list[list[Any]],
    check_in: str,
    check_out: str,
) -> dict[str, Any]:
    if len(values) < 2:
        raise ValueError("Availability sheet must include a header row and at least one room row")

    header = values[0]
    room_rows = values[1:]
    nights = get_nights_between(check_in, check_out)
    date_indexes: list[int] = []

    normalized_header = [_normalize_cell(cell) for cell in header]

    for night in nights:
        try:
            date_indexes.append(normalized_header.index(night))
        except ValueError as exc:
            raise ValueError(f"Date {night} was not found in the availability sheet header") from exc

    available_rooms: list[str] = []

    for row in room_rows:
        room = str(row[0] if len(row) > 0 else "").strip()

        if not room:
            continue

        is_available = all(
            index < len(row) and _normalize_cell(row[index]) in AVAILABLE_VALUES
            for index in date_indexes
        )

        if is_available:
            available_rooms.append(room)

    return {
        "check_in": check_in,
        "check_out": check_out,
        "nights": nights,
        "available_rooms": available_rooms,
    }
