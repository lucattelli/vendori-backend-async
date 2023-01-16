from dataclasses import dataclass
from uuid import UUID


@dataclass
class DropBox:
    uuid: UUID
    name: str
    location: str

