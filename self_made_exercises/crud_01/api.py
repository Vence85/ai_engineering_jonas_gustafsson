from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

books = [
    {"id": 1, "title": "Harry Potter", "author": "J.K. Rowling", "year": 1997},
    {"id": 2, "title": "Sagan om Ringen", "author": "J.R.R. Tolkien", "year": 1954},
    {"id": 3, "title": "Mio min Mio", "author": "Astrid Lindgren", "year": 1954},
]

@app.get("/books")
async def get_books():
    return books

@app.get("/book/{title}")
async def get_book_by_title(title: str):
    result = [book for book in books if book["title"].casefold() == title.casefold()]
    return result

@app.get("/book/id/{id}")
async def get_book_by_id(id: int):
    result = [book for book in books if book["id"] == id]
    return result

@app.get("/book/author/{author}")
async def get_book_by_author(author: str):
    result = [book for book in books if book["author"].casefold() == author.casefold()]
    return result

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

@app.post("/books")
async def create_book(book: Book):
    new_book = book.model_dump()
    books.append(new_book)
    return new_book
    