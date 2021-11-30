from fastapi import APIRouter

index = APIRouter()

@index.get('/')
def cek_api():
    return {
        "/":"Cek Link for api",
        "/product":{
            "/list/":"get all list product",
            "/create/":"create new list",
            "/update/":"update product by id",
            "/delete/":"delete product by id",
        },
        }
