from tortoise import fields
from tortoise.models import Model

import api.schemas as schemas

class User(Model):
    """
    This represents a book in the database.
    """

    class Meta:
        table="users"

    username = fields.CharField(max_length=100, pk=True)
    password = fields.CharField(max_length=100)
    books: fields.ReverseRelation["Book"]

    def to_user(self) -> schemas.User:
        """Create a book of type schemas.Book from models.Book"""
        return schemas.User(**dict(self))

class Book(Model):
    """
    This represents a book in the database.
    """

    class Meta:
        table="books"

    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    description = fields.CharField(max_length=100)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    sold = fields.BooleanField(default=False)
    user: fields.ForeignKeyNullableRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="books"
    )

    def to_book(self) -> schemas.Book:
        """Create a book of type schemas.Book from models.Book"""
        return schemas.Book(**dict(self))