from abc import ABC, abstractmethod
import base64
import binascii
import json
from typing import Any


class Cipher(ABC):
    @abstractmethod
    def encrypt(self, raw_payload: Any) -> str:
        """
        Encrypt a Python object into a string representation.

        Args:
            raw_payload: The value to encrypt. Can be any JSON-serializable type.

        Returns:
            str: The encrypted string.
        """
        pass

    @abstractmethod
    def decrypt(self, encrypterd_payload: str) -> Any:
        """
        Decrypt an encrypted string back to a Python object. If the object isn't encrypted,
        it remains unchanged

        Args:
            encrypted_payload: The encrypted or encoded string.

        Returns:
            Any: The decrypted Python object. Type depends on the original input.
        """
        pass

class B64Cipher(Cipher):
    """Cipher that base64-encodes/decodes JSON-serialized values."""
    
    def encrypt(self, raw_payload: Any) -> str:
        return base64.b64encode(json.dumps(raw_payload).encode("utf-8")).decode()
    
    def decrypt(self, encrypted_payload: str) -> Any:
        try:
            decrypted_payload = json.loads(base64.b64decode(encrypted_payload).decode())
            return decrypted_payload
        except (UnicodeDecodeError, json.JSONDecodeError, binascii.Error, TypeError) as e:
            return encrypted_payload