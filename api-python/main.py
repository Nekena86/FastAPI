from fastapi import FastAPI
from pydantic import BaseModel

# Créer une instance FastAPI
app = FastAPI()

# Route GET basique
@app.get("/")
def read_root():
    return {"message": "Bienvenue dans FastAPI 🎉"}

# Définir un modèle de données pour POST
class Item(BaseModel):
    name: str
    price: float

# Route POST
@app.post("/items")
def create_item(item: Item):
    return {
        "name": item.name,
        "price": item.price,
        "status": "Item bien reçu ✅"
    }