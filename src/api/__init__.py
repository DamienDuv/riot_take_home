from fastapi import APIRouter

from .encryption_routes import router as encryption_routes
from .signing_routes import router as signing_routes

router = APIRouter()

# Include individual routers
router.include_router(encryption_routes)
router.include_router(signing_routes)
