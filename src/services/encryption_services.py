from typing import Any

from src.domain.cipher import Cipher


def encrypt_service(json_payload: dict[str, Any], cipher: Cipher) -> dict[str, str]:
    """
    Encrypt all top-level values of the input dictionary.

    Args:
        json_payload: A dictionary with arbitrary values.
        cipher: A Cipher implementation (e.g., B64Cipher).

    Returns:
        dict[str, str]: New dict with top-level values encrypted as strings.
    """
    return apply_cipher(json_payload, cipher.encrypt)

def decrypt_service(json_payload: dict[str, Any], cipher: Cipher) -> dict[str, Any]:
    """
    Decrypt values of the input dictionary, unencrypted values remain untouched.

    Args:
        json_payload: A dictionary with encrypted values.
        cipher: A Cipher implementation (e.g., B64Cipher).

    Returns:
        dict[str, Any]: New dict with decrypted values restored to original types.
    """
    return apply_cipher(json_payload, cipher.decrypt)

def apply_cipher(json_payload: dict[str, Any], cipher_function) -> dict[str, Any]:
    """
    Apply a transformation function to all top-level values of a dictionary.

    Args:
        json_payload: Input dictionary.
        cipher_function: Function that takes a value and returns a transformed value.

    Returns:
        dict[str, Any]: New dict with transformed top-level values.
    """
    out = {}

    for k, v in json_payload.items():
        out[k] = cipher_function(v)

    return out