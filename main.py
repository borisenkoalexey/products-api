from fastapi import FastAPI, HTTPException, status
from typing import Any

app = FastAPI()

PRODUCTS: list[dict[str, Any]] = [
    {
        "id": 1,
        "name": "Ноутбук",
        "category": "Электроника",
        "price": 89990.0,
        "description": "Лёгкий ноутбук для работы и учёбы",
    },
    {
        "id": 2,
        "name": "Смартфон",
        "category": "Электроника",
        "price": 54990.0,
        "description": "Смартфон с хорошей камерой",
    },
    {
        "id": 3,
        "name": "Кофеварка",
        "category": "Бытовая техника",
        "price": 12990.0,
        "description": "Капельная кофеварка для дома",
    },
    {
        "id": 4,
        "name": "Чайник",
        "category": "Бытовая техника",
        "price": 2990.0,
        "description": "Электрический чайник, объём 1.7 л",
    },
    {
        "id": 5,
        "name": "Книга по Python",
        "category": "Книги",
        "price": 1490.0,
        "description": "Введение в язык программирования Python",
    },
    {
        "id": 6,
        "name": "Книга по FastAPI",
        "category": "Книги",
        "price": 1990.0,
        "description": "Практическое руководство по фреймворку FastAPI",
    },
]


@app.get("/health")
async def healthcheck():
    return {"status": "ok"}


@app.get("/products")
async def read_all_products():
    return PRODUCTS


@app.get("/products/{product_id}")
async def read_product(product_id: int) -> dict[str, Any]:
    for product in PRODUCTS:
        if product.get("id") == product_id:
            return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Продукт не найден"
    )
