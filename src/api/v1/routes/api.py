from fastapi import APIRouter
from src.api.v1.endpoints import item

router = APIRouter()
router.include_router(item.router)
