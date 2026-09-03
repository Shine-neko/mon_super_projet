from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Mon Super Projet")


class Item(BaseModel):
    name: str
    price: float


items: dict[int, Item] = {}


@app.get("/")
def read_root():
    return {"message": "Bonjour"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/items/{item_id}", status_code=201)
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=409, detail="Item already exists")
    items[item_id] = item
    return item


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
