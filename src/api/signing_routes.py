import logging
from fastapi import APIRouter, Depends, HTTPException, status

from src.dependencies import get_signer
from src.domain.signer import Signer
from src.models.common import AnyDict
from src.models.signing import SignResponse, VerifyRequest
from src.services.signing_services import sign_service, verify_service

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(tags=["signing"])

@router.post("/sign")
async def sign_route(payload: AnyDict, signer: Signer = Depends(get_signer)) -> SignResponse:
   """Generate a signature for the given JSON payload."""
   logger.info("Signing payload with %s", signer.__class__.__name__)

   return sign_service(payload.model_dump(), signer)
    
@router.post("/verify", status_code=status.HTTP_204_NO_CONTENT)
async def verify_route(req: VerifyRequest, signer: Signer = Depends(get_signer)) -> None:
   """Verify that the provided signature matches the given JSON payload."""
   logger.info("Verifying payload's signature with %s", signer.__class__.__name__)

   if not verify_service(req.signature, req.data.model_dump(), signer):
      raise HTTPException(status_code=400, detail="Invalid signature")