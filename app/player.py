import re
from typing import Iterable

from .models import Channel


def parse_m3u(content: str) -> list[Channel]:
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    channels: list[Channel] = []
    current: dict | None = None

    for line in lines:
        if line.startswith("#EXTINF"):
            match = re.match(r"#EXTINF:.*?,\s*(.*)$", line)
            name = match.group(1).strip() if match else "Unknown"
            current = {"name": name}
            continue

        if line.startswith("http") and current is not None:
            channel = Channel(
                id=re.sub(r"[^a-z0-9]+", "-", current["name"].lower()).strip("-"),
                name=current["name"],
                country="Importée",
                category="M3U",
                url=line,
                logo="",
                tags=["imported"],
                is_live=True,
            )
            channels.append(channel)
            current = None

    return channels


def parse_m3u_file(path: str) -> list[Channel]:
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        return parse_m3u(handle.read())
