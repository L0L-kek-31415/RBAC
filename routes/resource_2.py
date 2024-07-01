from fastapi import APIRouter

router = APIRouter()


@router.get("/resource2")
async def resource2():
    return {"message": "This is an resource2 route"}


@router.post("/resource2")
async def add_resource2(add: int):
    return {"message": add}


@router.delete("/resource2")
async def delete_resource2():
    return {"message": "This resource2 is deleted"}
