from dataclasses import dataclass, field


@dataclass
class Channel:
    id: str
    name: str
    country: str
    category: str
    url: str
    logo: str = ""
    tags: list[str] = field(default_factory=list)
    is_live: bool = True

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "category": self.category,
            "url": self.url,
            "logo": self.logo,
            "tags": self.tags,
            "is_live": self.is_live,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Channel":
        return cls(
            id=data.get("id", ""),
            name=data.get("name", ""),
            country=data.get("country", ""),
            category=data.get("category", ""),
            url=data.get("url", ""),
            logo=data.get("logo", ""),
            tags=data.get("tags", []),
            is_live=data.get("is_live", True),
        )
