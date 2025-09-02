import json
from typing import Any


def obj_to_bytes(obj: Any) -> bytes:
    # Deterministic JSON: no spaces, stable key order, UTF-8
    return json.dumps(
        obj,
        separators=(",", ":"),
        sort_keys=True,
        ensure_ascii=False,
    ).encode()