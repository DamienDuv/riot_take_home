from fastapi import APIRouter, Depends

from src.dependencies import get_cipher
from src.models.common import AnyDict
from src.services.encryption_services import decrypt_service, encrypt_service

router = APIRouter(tags=["encryption"])

@router.post("/encrypt")
async def encrypt_route(payload: AnyDict, cipher = Depends(get_cipher)):
   return encrypt_service(payload.model_dump(), cipher)
    
@router.post("/decrypt")
async def decrypt_route(payload: AnyDict, cipher = Depends(get_cipher)):
   return decrypt_service(payload.model_dump(), cipher)