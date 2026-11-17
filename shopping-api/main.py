import os
import socket

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field

app = FastAPI(title="Shopping List API")


class ShoppingItem(BaseModel):
    name: str = Field(min_length=1)
    amount: int = Field(ge=0)


shopping_list: dict[str, ShoppingItem] = {}


@app.get("/hello")
def hello() -> dict[str, str]:
    return {"message": "Good morning!", "hostname": socket.gethostname()}


@app.get("/crash")
def crash() -> None:
    raise RuntimeError("Simulated application error")


@app.get("/kill")
def kill() -> None:
    os._exit(1)


@app.get("/shopping-list")
def list_items() -> list[ShoppingItem]:
    return list(shopping_list.values())


@app.post("/shopping-list", status_code=201)
def create_item(item: ShoppingItem) -> ShoppingItem:
    if item.name in shopping_list:
        raise HTTPException(status_code=409, detail="Item already exists")
    shopping_list[item.name] = item
    return item


@app.get("/shopping-list/{name}")
def get_item(name: str) -> ShoppingItem:
    if name not in shopping_list:
        raise HTTPException(status_code=404, detail="Item not found")
    return shopping_list[name]


@app.put("/shopping-list/{name}")
def update_item(name: str, item: ShoppingItem) -> ShoppingItem:
    if name not in shopping_list:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.name != name:
        raise HTTPException(status_code=422, detail="Item name must match the path")
    shopping_list[name] = item
    return item


@app.delete("/shopping-list/{name}", status_code=204)
def delete_item(name: str) -> Response:
    if name not in shopping_list:
        raise HTTPException(status_code=404, detail="Item not found")
    del shopping_list[name]
    return Response(status_code=204)