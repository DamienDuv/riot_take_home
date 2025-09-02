from pydantic import BaseModel

from src.models.common import AnyDict


class SignResponse(BaseModel):
    signature: str

class VerifyRequest(BaseModel):
    signature: str
    data: AnyDict