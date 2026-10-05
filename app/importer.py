import json
from pathlib import Path
from typing import Iterable

from .models import Channel


DATA_PATH = Path(__file__).resolve().parent.parent / "data"
FAVORITES_PATH = DATA_PATH / "favorites.json"


def ensure_data_files() -> None:
    DATA_PATH.mkdir(exist_ok=True)
    if not FAVORITES_PATH.exists():
        FAVORITES_PATH.write_text("[]", encoding="utf-8")


def load_favorites() -> list[str]:
    ensure_data_files()
    try:
        data = json.loads(FAVORITES_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def save_favorites(favorites: Iterable[str]) -> None:
    ensure_data_files()
    FAVORITES_PATH.write_text(json.dumps(list(favorites), indent=2), encoding="utf-8")


def sample_channels() -> list[Channel]:
    return [
        Channel(
            id="france-2",
            name="France 2",
            country="France",
            category="Généraliste",
            url="https://example.com/france2.m3u8",
            logo="",
            tags=["general", "france"],
            is_live=True,
        ),
        Channel(
            id="rtbf",
            name="RTBF",
            country="Belgique",
            category="Généraliste",
            url="https://example.com/rtbf.m3u8",
            logo="",
            tags=["belgique", "public"],
            is_live=True,
        ),
        Channel(
            id="rts-1",
            name="RTS 1",
            country="Suisse",
            category="Généraliste",
            url="https://example.com/rts1.m3u8",
            logo="",
            tags=["suisse"],
            is_live=True,
        ),
        Channel(
            id="canal-senegal",
            name="Canal Sénégal",
            country="Sénégal",
            category="Actualités",
            url="https://example.com/canal-senegal.m3u8",
            logo="",
            tags=["senegal", "afrique"],
            is_live=True,
        ),
        Channel(
            id="telematin",
            name="Télé Matin",
            country="Mali",
            category="Actualités",
            url="https://example.com/telematin.m3u8",
            logo="",
            tags=["mali", "afrique"],
            is_live=True,
        ),
        Channel(
            id="africa-24",
            name="Africa 24",
            country="Afrique",
            category="Actualités",
            url="https://example.com/africa24.m3u8",
            logo="",
            tags=["afrique", "news"],
            is_live=True,
        ),
    ]
