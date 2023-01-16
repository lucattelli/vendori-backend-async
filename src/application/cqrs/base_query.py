from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar('T')

@dataclass
class BaseQueryPaginationOptions:
    page: int
    page_size: int | None = None


@dataclass
class BaseQueryPagination(BaseQueryPaginationOptions):
    pages: int | None = None
    total_items: int | None = None


@dataclass
class BaseQueryOptions:
    pagination: BaseQueryPaginationOptions


@dataclass
class BaseQueryResultMetadata:
    pagination: BaseQueryPagination


@dataclass
class BaseQueryBaseResult(Generic[T]):
    items_page: list[T]
    metadata: BaseQueryResultMetadata

