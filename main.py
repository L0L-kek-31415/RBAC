from fastapi import FastAPI
from routes.resource_1 import router as resource_1_router
from routes.resource_2 import router as resource_2_router

from rbac.middleware import RBACMiddleware

app = FastAPI()
app.add_middleware(RBACMiddleware)
app.include_router(resource_1_router)
app.include_router(resource_2_router)


@app.get('/')
async def root():
    return {"message": "Hi, Admin"}

