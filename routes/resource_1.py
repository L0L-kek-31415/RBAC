from fastapi import APIRouter

router = APIRouter()


@router.get("/resource1")
async def resource1():
    return {"message": "This is a resource1 route"}


@router.post("/resource1")
async def add_resource1(add: int):
    return {"message": add}


@router.delete("/resource1")
async def delete_resource1():
    return {"message": "This resource1 is deleted"}