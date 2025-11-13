from fastapi import FastAPI, status
from db import get_connection
from models import Product
from pydantic import BaseModel

class Product(BaseModel):
    Name: str
    Price: float

import logging

# 🔹 Configure logging
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI(
    title="Products API",
    description="API to manage products in SQL Server",
    version="1.0.0",
    contact={
        "name": "pritpalkaur",
        "email": "pritpal@example.com"
    }
)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/anime/{title}")
def get_anime(title: str):
    return {"title": title, "status": "searching..."}

@app.get("/products", tags=["Products"])
def get_products():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT [Id],[Name],[Price] FROM [ProductsDb].[dbo].[Products]")
        rows = cursor.fetchall()
        conn.close()

        products = [
            {"id": row.Id, "Name": row.Name, "Price": row.Price, "Price": row.Price}
            for row in rows
        ]
        return {"products": products}

    except Exception as e:
        logging.error(f"Error fetching products: {e}")
        return {"error": "Failed to fetch products"}

@app.post("/products",   tags=["Products"], summary="Create a new product",response_description="The created product",
    status_code=status.HTTP_201_CREATED
)

def create_product(product: Product):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO [ProductsDb].[dbo].[Products] ([Name], [Price]) VALUES (?, ?)",
            (product.Name, product.Price)
        )
        conn.commit()
        conn.close()
        return {"message": "Product created successfully"}
    except Exception as e:
        logging.error(f"Error creating product: {e}")
        return {"error": "Failed to create product"}
    
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE [ProductsDb].[dbo].[Products] SET [Name] = ?, [Price] = ? WHERE [Id] = ?",
            (product.Name, product.Price, product_id)
        )
        conn.commit()
        conn.close()
        return {"message": "Product updated successfully"}
    except Exception as e:
        logging.error(f"Error updating product {product_id}: {e}")
        return {"error": "Failed to update product"}
    
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM [ProductsDb].[dbo].[Products] WHERE [Id] = ?",
            (product_id,)
        )
        conn.commit()
        conn.close()
        return {"message": "Product deleted successfully"}
    except Exception as e:
        logging.error(f"Error deleting product {product_id}: {e}")
        return {"error": "Failed to delete product"}
