import json
from typing import Any

from src.domain.cipher import Cipher, DecryptionError
from src.services.helper_functions import obj_to_bytes

ENC_KEY = "enc"
VAL_KEY = "val"

def encrypt_service(json_payload: dict[str, Any], cipher: Cipher) -> dict[str, Any]:
    """Encrypt all top-level values and wrap them in a small envelope."""
    out: dict[str, Any] = {}

    for k, v in json_payload.items():
        out[k] = {
            ENC_KEY: cipher.__class__.__name__,
            VAL_KEY: cipher.encrypt(obj_to_bytes(v)),
        }

    return out

def decrypt_service(json_payload: dict[str, Any], cipher: Cipher) -> dict[str, Any]:
    """
    Decrypt only enveloped values that declare this cipher's algorithm.
    Non-enveloped (unencrypted) values remain unchanged.
    """
    out: dict[str, Any]  = {}

    for k, v in json_payload.items():
        if isinstance(v, dict) and v.get(ENC_KEY) == cipher.__class__.__name__ and isinstance(v.get(VAL_KEY), str):
            try:
                out[k] = json.loads(cipher.decrypt(v.get(VAL_KEY)).decode())
            except DecryptionError:
                out[k] = v
        else:
            out[k] = v

    return out


