from typing import Any
from pydantic import RootModel


class AnyDict(RootModel[dict[str, Any]]):
    pass