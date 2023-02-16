import logging
import secrets
from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from tortoise.contrib.fastapi import register_tortoise

import schemas
import models

app = FastAPI()

security = HTTPBasic()


async def get_current_user(credentials: HTTPBasicCredentials = Depends(security)) -> models.User:
    user_db = await models.User.filter(username=credentials.username).first()
    if user_db is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    password_bytes = credentials.password.encode("utf8")
    is_correct_password = secrets.compare_digest(
        password_bytes, user_db.password.encode("utf8")
    )

    if not (is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user_db

@app.post("/user", status_code=status.HTTP_201_CREATED)
async def get_user(user: schemas.User):
    """Create a new user in the table 'users'"""
    logging.info("test")
    user_db = await models.User.create(**user.dict())
    logging.info(f"User {user_db.username} was created")

@app.post("/book", status_code=status.HTTP_201_CREATED)
async def create_book(book: schemas.Book) -> None:
    """Create a new book in the table 'books'"""
    book_db = await models.Book.create(**book.dict(exclude_unset=True))
    logging.info(f"Book {book_db.title} was created with id: {book_db.id}")

@app.get("/book", status_code=status.HTTP_200_OK)
async def get_book(title: str) -> schemas.Book:
    """Get a book by its title"""
    book_db = await models.Book.filter(title=title).first()
    if book_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with title {title} was not found"
        )

    logging.info(f"Book {book_db.title} was retrieved")
    return book_db.to_book()

@app.post("/book/sell", status_code=status.HTTP_201_CREATED)
async def sell_book(title: str, credentials: HTTPBasicCredentials = Depends(get_current_user)) -> None:
    """Sell a book to the authenticated user"""
    book_db = await models.Book.filter(title=title, sold=False).first()
    if book_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with title {title} was not found"
        )

    logging.info(f"Book {book_db.title} was retrieved")
    book_db.update_from_dict({"sold": True, "user_id": credentials.username})
    await book_db.save()

@app.get("/books", status_code=status.HTTP_200_OK)
async def get_books(user_db: models.User = Depends(get_current_user)) -> List[schemas.Book]:
    """Fetch all books of the authenticated user"""
    logging.info(f"User {user_db.username} was retrieved")
    return [book_db.to_book() async for book_db in user_db.books]

register_tortoise(
    app,
    db_url="sqlite://:memory:",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)