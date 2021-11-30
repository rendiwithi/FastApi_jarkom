from fastapi import APIRouter
from config.db import conn
from models.product import products
from schemas.product import Product


product = APIRouter()


@product.get('/product/list/')
def list_product():
    return conn.execute(products.select()).fetchall()


@product.post('/product/add/{name}/{type}/{quantity}/')
def add_product(name: str, type: str, quantity: int):
    return conn.execute(products.insert().values(
        name=name,
        type=type,
        quantity=quantity)
    )


@product.put('/product/update/{id}/{name}/{type}/{quantity}/')
def update_product(id: int, name: str, type: str, quantity: int):
    return conn.execute(
        products.update().values(
            name=name,
            type=type,
            quantity=quantity)
        .where(products.c.id == id))


@product.delete('/product/remove/{id}')
def delete_product(id: int):
    return conn.execute(products.delete().where(products.c.id == id))
