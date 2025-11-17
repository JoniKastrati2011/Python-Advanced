# @app.get("/items/{item_id")
# def read_item(item_id: int):
#     return {"item_id": item_id}
from module20.main import app


# @app.get("/")
# def root():
#     return {"message": "Hello World"}
#
# #path parameters
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {"user_id": user_id, "name": "John Doe"}
#
# #Query Parameters
# @app.get("/items/")
# def get_items(skip: int = 0, limit: int = 10):
#     return{"skip": skip, "limit": limit}
#GET Method
@app.get("/items/")
def read_items():
    return{"items": ["item1", "item2", "item3"]}

#POST Method
@app.post("/item/")
def create_item(name:str, price:float):
    return{"name": name, "price": price}
#PUT Method
@app.put("/items/{item_id}")
def update_item(item_id:int, name:str, price:float):
    return{"item_id": item_id, "name": name, "price": price}

#DELETE Method
@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    return{"message": f"Item {item_id} deleted"}