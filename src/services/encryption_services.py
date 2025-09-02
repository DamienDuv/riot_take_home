import json
from typing import Any

from src.domain.cipher import Cipher
from src.services.helper_functions import obj_to_bytes


def encrypt_service(json_payload: dict[str, Any], cipher: Cipher) -> dict[str, str]:
    """ Encrypt all top-level values of the input dictionary. """
    out = {}

    for k, v in json_payload.items():
        out[k] = cipher.encrypt(obj_to_bytes(v))

    return out

def decrypt_service(json_payload: dict[str, Any], cipher: Cipher) -> dict[str, Any]:
    """ Decrypt all encrypted values of the input dictionary. """
    out = {}

    for k, v in json_payload.items():
        if not isinstance(v, str):
            # Only string values are passed to the cipher; other types are left as-is.
            # Detecting whether a string is actually encrypted is the responsibility
            # of the cipher implementation.
            # This allows us to safely call .decode() on decrypted bytes.
            out[k] = v
            continue

        out[k] = json.loads(cipher.decrypt(v).decode())

    return out

