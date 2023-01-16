from fastapi import APIRouter

from infrastructure.transport.rest.routers.drop_box import drop_box_commands_router, drop_box_queries_router


api_router = APIRouter(prefix='/v1')
api_router.include_router(drop_box_commands_router)
api_router.include_router(drop_box_queries_router)
