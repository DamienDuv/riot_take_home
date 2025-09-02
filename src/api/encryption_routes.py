import logging
from fastapi import APIRouter, Depends

from src.dependencies import get_cipher
from src.models.common import AnyDict
from src.services.encryption_services import decrypt_service, encrypt_service

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


router = APIRouter(tags=["encryption"])

@router.post("/encrypt")
async def encrypt_route(payload: AnyDict, cipher = Depends(get_cipher)) -> AnyDict:
   logger.info("Encrypting payload with %s", cipher.__class__.__name__)
   return encrypt_service(payload.model_dump(), cipher)
    
@router.post("/decrypt")
async def decrypt_route(payload: AnyDict, cipher = Depends(get_cipher)) -> AnyDict:
   logger.info("Decrypting payload with %s", cipher.__class__.__name__)
   return decrypt_service(payload.model_dump(), cipher)