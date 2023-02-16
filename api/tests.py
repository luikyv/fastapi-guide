from typing import Generator, AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from main import app

from tortoise.contrib.test import finalizer, initializer

import schemas
import api.models as models

user = schemas.User(username="testuser", password="password")
book = schemas.Book(title="Test Book", author="Test Author", description="Test book description", price=50.0)

@pytest.fixture
def set_up_teardown() -> Generator:
    initializer(
        ["models"],
        # db_url="sqlite://:memory:",
    )
    yield None
    finalizer()

@pytest.fixture
def client(set_up_teardown: Generator) -> Generator:
    with TestClient(app) as c:
        yield c

@pytest.fixture
@pytest.mark.asyncio
async def populated_user_client(set_up_teardown: Generator) -> AsyncGenerator:
    await models.User(**user.dict()).save()
    # raise Exception()
    yield None

@pytest.fixture
@pytest.mark.asyncio
async def populate_user_and_books_client(set_up_teardown: Generator) -> AsyncGenerator:
    await models.User(**user.dict()).save()
    await models.Book(**book.dict(), user_id=user.username).save()
    yield None

@pytest.mark.asyncio
class TestBooks:
    url = "/books"

    async def test(self, populated_user_client: AsyncGenerator) -> None:
        print(await models.User.all())
        assert False

    # def test_user_without_books(self, populated_user_client: AsyncGenerator, client: TestClient) -> None:
    #     response = client.get(
    #         self.url,
    #         auth=(user.username, user.password),
    #     )
    #     assert response.status_code == 200
    #     assert response.json() == []
    
    # def test_user_with_book(self, populate_user_and_books_client: AsyncGenerator, client: TestClient) -> None:
    #     response = client.get(
    #         self.url,
    #         auth=(user.username, user.password),
    #     )
    #     assert response.status_code == 200
    #     assert response.json() == [book.dict()]