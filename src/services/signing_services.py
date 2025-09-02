import json
from typing import Any

from src.domain.signer import Signer
from src.services.helper_functions import obj_to_bytes


def sign_service(payload: dict[str,Any], signer: Signer) -> dict[str, str]:
    """Sign a JSON payload using the provided signer."""
    serialized_payload = obj_to_bytes(payload)
    return {
        "signature": signer.sign(serialized_payload)
    }

def verify_service(signature: str, payload: dict[str, Any], signer: Signer) -> bool:
    """Verify a JSON payload against a signature using the provided signer."""
    serialized_payload = obj_to_bytes(payload)
    return signer.verify(signature, serialized_payload)