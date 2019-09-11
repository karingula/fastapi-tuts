from fastapi import Depends, FastAPI
from pydantic import BaseModel
from starlette.requests import Request

# fastapi instance
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    # use None to make it just optional
    is_offer: bool = None


async def common_parameters(request: Request, item_id: int, q: str = None, limit: int = 100):
    return {"q": q, "skip": item_id, "limit": limit}

@app.get('/')
def read_root():
    return {"Hello": "World"}


@app.get('/items/{item_id}')
# give none for optional query parameter
def read_item(commons: dict = Depends(common_parameters)):
    return commons


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}
