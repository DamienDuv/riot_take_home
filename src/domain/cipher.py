from abc import ABC, abstractmethod
import base64
import binascii

class DecryptionError(Exception):
    """Raised when a cipher cannot decrypt a given payload."""
    pass

class Cipher(ABC):
    """
    Abstract interface for encryption.

    Implementations are responsible for managing any keys or secrets they require.
    """

    @abstractmethod
    def encrypt(self, payload: bytes) -> str:
        """Encrypt raw bytes into a string representation"""
        pass

    @abstractmethod
    def decrypt(self, payload: str) -> bytes:
        """
        Decrypt an encrypted string back to raw bytes.
        """
        pass

class B64Cipher(Cipher):
    """Cipher that base64-encodes/decodes"""
    
    def encrypt(self, payload: bytes) -> str:
        return base64.b64encode(payload).decode()
    
    def decrypt(self, payload: str) -> bytes:
        try:
            return base64.b64decode(payload)
        except (binascii.Error, UnicodeDecodeError, ValueError, TypeError):
            raise DecryptionError()

        
       