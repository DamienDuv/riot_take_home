from src.domain.cipher import B64Cipher, Cipher
from src.domain.signer import HMACSigner, Signer


def get_cipher() -> Cipher:
   return B64Cipher()

def get_signer() -> Signer:
   return HMACSigner()