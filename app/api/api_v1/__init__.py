from fastapi import APIRouter

from config import settings

router = APIRouter(prefix=settings.api.v1.prefix)
