from __future__ import annotations

from datetime import date, timedelta


def parse_iso_date(value: str, field_name: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{field_name} must be a valid date using YYYY-MM-DD format") from exc


def get_nights_between(check_in: str, check_out: str) -> list[str]:
    start = parse_iso_date(check_in, "check_in")
    end = parse_iso_date(check_out, "check_out")

    if start >= end:
        raise ValueError("check_out must be after check_in")

    nights: list[str] = []
    current = start

    while current < end:
        nights.append(current.isoformat())
        current += timedelta(days=1)

    return nights
