from abc import ABC, abstractmethod
import base64
import binascii
import json

from src.services.helper_functions import obj_to_bytes


class Cipher(ABC):
    """
    Abstract interface for encryption.

    Implementations are responsible for managing any keys or secrets they require.
    """

    @abstractmethod
    def encrypt(self, payload: bytes) -> str:
        """Encrypt a Python object into a string representation"""
        pass

    @abstractmethod
    def decrypt(self, payload: str) -> bytes:
        """
        Decrypt an encrypted string back to a Python object.
        If the input isn't encrypted, it returns unchanged.
        """
        pass

class B64Cipher(Cipher):
    """Cipher that base64-encodes/decodes"""
    
    def encrypt(self, payload: bytes) -> str:
        return base64.b64encode(payload).decode()
    
    def decrypt(self, payload: str) -> bytes:
        try:
            decrypted_payload = base64.b64decode(payload)
            return decrypted_payload
        except: # This methods of catching unencrypted input could be fine tuned
            return payload.encode()