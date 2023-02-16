from typing import Generator, AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from main import app

from tortoise.contrib.test import finalizer, initializer

import schemas
import models

user = schemas.User(username="testuser", password="password")
book = schemas.Book(title="Test Book", author="Test Author", description="Test book description", price=50.0)

@pytest.fixture(scope="module")
def client() -> Generator:
    initializer(["models"])
    with TestClient(app) as c:
        yield c
    finalizer()

@pytest.fixture()
async def populate_user() -> AsyncGenerator:
    await models.User(**user.dict()).save()
    yield None

@pytest.fixture()
async def populate_user_and_books() -> AsyncGenerator:
    await models.User(**user.dict()).save()
    await models.Book(**book.dict(), user_id=user.username).save()
    yield None

class TestBooks:
    url = "/books"
    headers = {"Authorization": "Basic {user.username}{user.password}"}

    @populate_user
    def test_user_without_books(self, _, client: TestClient) -> None:
        response = client.get(
            self.url,
            headers=self.headers
        )
        assert response.status_code == 200
        assert response.json() == []
    
    @populate_user_and_books
    def test_user_with_book(self, client: TestClient, _) -> None:
        response = client.get(
            self.url,
            headers=self.headers
        )
        assert response.status_code == 200
        assert response.json() == [book.dict()]