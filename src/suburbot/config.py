from __future__ import annotations

import os
from pathlib import Path


def load_env_file(path: str = ".env") -> None:
    env_path = Path(path)
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()

        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue

        key, value = stripped.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value or value.strip() == "":
        raise RuntimeError(f"Missing required environment variable: {name}")

    return value


def get_env(name: str, default: str | None = None) -> str | None:
    value = os.getenv(name)
    return value if value and value.strip() != "" else default
