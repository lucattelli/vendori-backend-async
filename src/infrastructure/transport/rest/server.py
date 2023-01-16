from fastapi import FastAPI

from infrastructure.transport.rest.routers.routers import api_router



app = FastAPI()
app.include_router(api_router, prefix='/api')


