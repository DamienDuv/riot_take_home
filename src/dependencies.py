from src.domain.cipher import B64Cipher, Cipher


def get_cipher() -> Cipher:
   return B64Cipher()