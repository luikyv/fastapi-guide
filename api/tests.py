from typing import Generator, AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from main import app

from tortoise.contrib.test import finalizer, initializer
from tortoise import Tortoise

import schemas
import models

user = schemas.User(username="testuser", password="password")
book = schemas.Book(title="Test Book", author="Test Author", description="Test book description", price=50.0)    

@pytest.fixture
def client() -> Generator:
    with TestClient(app) as c:
        yield c

class TestBooks:
    url = "/books"

    @pytest.mark.asyncio
    async def test_user_without_books(self, client: TestClient) -> None:
        await models.User(**user.dict()).save()

        response = client.get(
            self.url,
            auth=(user.username, user.password),
        )
        assert response.status_code == 200
        assert response.json() == []
    
    @pytest.mark.asyncio
    async def test_user_with_book(self, client: TestClient) -> None:
        await models.User(**user.dict()).save()
        await models.Book(**book.dict(), user_id=user.username).save()

        response = client.get(
            self.url,
            auth=(user.username, user.password),
        )
        assert response.status_code == 200
        assert response.json() == [book.dict()]