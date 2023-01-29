from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import UUID

from domain.drop_box.entities.drop_box import DropBox


@dataclass
class FindFilters:
    uuids: list[UUID]


class DropBoxRepository(ABC):
    @abstractmethod
    async def find(self, *, filters: FindFilters) -> list[DropBox]:
        pass

    @abstractmethod
    async def save(self, *, drop_box: DropBox) -> None:
        pass
