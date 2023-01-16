from fastapi import APIRouter, HTTPException
from pydantic import UUID4, BaseModel

from application.drop_box.queries import find_by_filters
from application.cqrs import base_query
from infrastructure.persistence.memory.repositories.drop_box_memory_repository import DropBoxMemoryRepository
from infrastructure.persistence.memory.client import MemoryPersistenceClient

db_client = MemoryPersistenceClient()
drop_box_repository = DropBoxMemoryRepository(db_client=db_client)

drop_box_queries_router = APIRouter(prefix="/drop_boxes/v1/queries")


class BaseQueryPaginationOptionsDto(BaseModel, base_query.BaseQueryPaginationOptions):
    page: int
    page_size: int | None = None


class BaseQueryOptionsDto(BaseModel, find_by_filters.BaseQueryOptions):
    pagination: BaseQueryPaginationOptionsDto


class QueryFiltersDto(BaseModel, find_by_filters.QueryFilters):
    uuids: list[UUID4]


class QueryParametersDto(BaseModel, find_by_filters.QueryParameters):
    filters: QueryFiltersDto
    options: BaseQueryOptionsDto


queries_map = {
    "find-by-filters": find_by_filters.Query(drop_box_repository=drop_box_repository),
}

@drop_box_queries_router.post('/{query_name}')
async def drop_box_queries_endpoint(query_name, parameters: QueryParametersDto) -> find_by_filters.QueryResult:
    query = queries_map[query_name]
    if not query:
        raise HTTPException(status_code=404, detail="Query not found")

    result = await query.execute(parameters=parameters)
    return result

drop_box_commands_router = APIRouter(prefix="/drop_boxes/v1/commands")

commands_map = {
    "keep-alive": None,
}

@drop_box_commands_router.post('/{command_name}')
async def drop_box_commands_endpoint(command_name, command_data: dict):
    command = commands_map[command_name]
    if not command:
        raise HTTPException(status_code=404, detail="Command not found")

    result = await command.execute(command_data=command_data)
    return result
