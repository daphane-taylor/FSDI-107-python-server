from flask import Flask, request
import json
from config import db

app = Flask(__name__) # working like this makes it possible to move projects from computer to computer

# creating endpoints - what happens when i request access to the named page
@app.get("/")
def home():
    return "Hello from flask CH53"

@app.get("/test")
def test():
    return "Hello from the test page"

@app.get("/about")
def about():
    return "Daphane Taylor"

@app.get("/hello")
def hello():
    return "Hello there!"

#retrieve whats on the server
@app.get("/api/products")
def get_products():
    products = []
    cursor = db.products.find({})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

# add something to the server
@app.post("/api/products")
def save_product():
    product = request.get_json()
    print(f" new item {product}")
    # products.append(product)
    db.products.insert_one(product)
    return json.dumps(fix_id(product))

#update something on the server
@app.put("/api/products/<int:index>")
def update_product(index):
    updated_product = request.get_json()
    print(f"Product: {updated_product}: {index}")

    if 0 <= index <= len(products):
        products[index] = updated_product
        return json.dumps(updated_product)
    else:
        return "That index does not exist"


def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

# delete from server
@app.delete("/api/products/<int:index>") #inside angle brackets the first is the type, the second is the parameter
def delete_product(index):
    print(f"delete: {index}")

    if index>= 0 and index <len(products):
        deleted_product = products.pop(index)
        return json.dumps(deleted_product)
    else:
       return "That index does not exist"


# create an endpoint that says hello using a variable instead of a string.
@app.get("/contact")
def contact():
    message = {"message":"Hello, from the contact page!"}
    return json.dumps(message)

app.run(
    debug=True) # means when i save the code, the changes are applied in the server
