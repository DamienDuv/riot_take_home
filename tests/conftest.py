from fastapi.testclient import TestClient
import pytest

from src.app import app


@pytest.fixture(scope="session")
def client():
    with TestClient(app) as c:
        yield c