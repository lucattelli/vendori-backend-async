from __future__ import annotations
from dataclasses import dataclass
import math

from application.cqrs.base_query import BaseQueryBaseResult, BaseQueryOptions, BaseQueryPagination, BaseQueryResultMetadata
from domain.drop_box.entities.drop_box import DropBox
from domain.drop_box.ports.drop_box_repository import DropBoxRepository, FindFilters


@dataclass
class QueryResult(BaseQueryBaseResult):
    items_page: list[DropBox]


@dataclass
class QueryFilters(FindFilters):
    pass


@dataclass
class QueryParameters:
    filters: QueryFilters
    options: BaseQueryOptions


class Query:
    __drop_box_repository: DropBoxRepository

    __page_size: int = 25

    def __init__(self, drop_box_repository: DropBoxRepository) -> None:
        self.__drop_box_repository = drop_box_repository

    def __build_result(self, *, options: BaseQueryOptions, items: list[DropBox]) -> QueryResult:
        page = options.pagination.page if options.pagination.page >= 1 else 1
        page_size = options.pagination.page_size or self.__page_size
        total_items = len(items)
        page_rest = total_items % page_size
        pages = math.floor(total_items / page_size) + (1 if page_rest > 0 else 0)
        first_index = (page - 1) * page_size
        last_index = first_index + page_size

        items_page = items[first_index:last_index]

        print({
            "page": page,
            "page_size": page_size,
            "total_items": total_items,
            "pages": pages,
            "first_index": first_index,
            "last_index": last_index,
        })

        return QueryResult(
            items_page=items_page,
            metadata=BaseQueryResultMetadata(
                pagination=BaseQueryPagination(
                    page=page,
                    page_size=page_size,
                    pages=pages,
                    total_items=total_items,
                ),
            ),
        )


    async def execute(self, *, parameters: QueryParameters) -> QueryResult:
        print("Query.execute: ", parameters)
        items = await self.__drop_box_repository.find(filters=parameters.filters)
        return self.__build_result(options=parameters.options, items=items)
