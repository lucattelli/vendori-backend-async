from domain.drop_box.entities.drop_box import DropBox
from uuid import uuid4


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class MemoryPersistenceClient(metaclass=SingletonMeta):
    drop_boxes: list[DropBox] = []
    drop_box_items = []
    delivery_requests = []

    def __init__(self):
        for item in range(0,100):
            drop_box = DropBox(uuid=uuid4(), name=f"Drop Box {item}", location=f"Sim #{item}")
            self.drop_boxes.append(drop_box)
