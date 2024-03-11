from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# http://127.0.0.1:8000/items/2024?key1=hello&key2=world
@app.get("/items/{item_id}")
def read_item(item_id: int, key1: Union[str, None] = None, key2: Union[str, None] = None):
    return {"item_id": item_id, "key1": key1, "key2": key2}