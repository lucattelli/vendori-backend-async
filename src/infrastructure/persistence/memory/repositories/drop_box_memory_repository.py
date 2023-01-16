


from domain.drop_box.entities.drop_box import DropBox
from domain.drop_box.ports.drop_box_repository import DropBoxRepository, FindFilters
from infrastructure.persistence.memory.client import MemoryPersistenceClient


class DropBoxMemoryRepository(DropBoxRepository):
    __db_client: MemoryPersistenceClient

    def __init__(self, *, db_client: MemoryPersistenceClient):
        self.__db_client = db_client

    async def find(self, *, filters: FindFilters) -> list[DropBox]:
        if len(filters.uuids) == 0:
            return self.__db_client.drop_boxes

        return [
            drop_box for drop_box in self.__db_client.drop_boxes
            if drop_box.uuid in filters.uuids
        ]
