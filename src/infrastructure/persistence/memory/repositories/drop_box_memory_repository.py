from domain.drop_box.entities.drop_box import DropBox
from domain.drop_box.ports.drop_box_repository import DropBoxRepository, FindFilters
from infrastructure.persistence.memory.client import MemoryPersistenceClient


class DropBoxMemoryRepository(DropBoxRepository):
    __db_client: MemoryPersistenceClient

    def __init__(self, *, db_client: MemoryPersistenceClient):
        self.__db_client = db_client

    async def find(self, *, filters: FindFilters) -> list[DropBox]:
        drop_boxes: list[DropBox] = []
        for uuid, drop_box in self.__db_client.drop_boxes_dict.items():
            if len(filters.uuids) == 0 or uuid in filters.uuids:
                drop_boxes.append(drop_box)
        return drop_boxes

    async def save(self, *, drop_box: DropBox) -> None:
        self.__db_client.drop_boxes_dict[drop_box.uuid] = drop_box
