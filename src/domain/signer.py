from abc import ABC, abstractmethod
import hashlib
import hmac
from typing import Any


class Signer(ABC):
    """
    Abstract interface for cryptographic signing.

    Implementations are responsible for managing any keys or secrets they require.
    """

    @abstractmethod
    def sign(self, payload: bytes) -> str:
        """Generate a signature string for the given payload."""
        pass

    @abstractmethod
    def verify(self, signature: str, payload: bytes) -> bool:
        """Return True if the signature is valid for the given payload."""
        pass

class HMACSigner(Signer): 
    # A secure key storage is required here, could be retreived from a key store, cloud secret manager...
    key: bytes = b"this_is_a_secure_key_please_push_in_prod"

    def sign(self, payload: bytes) -> str:
        return hmac.digest(HMACSigner.key, payload, hashlib.sha256).hex()
    
    def verify(self, signature: str, payload: bytes) -> bool:
        return hmac.compare_digest(self.sign(payload), signature)
