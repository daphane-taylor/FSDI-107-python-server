from flask import Flask
import json
app = Flask(__name__) # working like this makes it possible to move projects from computer to computer

# creating endpoints - what happens when i request access to the named page
@app.get("/")
def home():
    return "Hello from flask"

@app.get("/test")
def test():
    return "Hello from the test page"

@app.get("/about")
def about():
    return "Daphane Taylor"

# create an endpoint that says hello using a variable instead of a string.
@app.get("/contact")
def contact():
    message = {"message":"Hello, from the contact page!"}
    return json.dumps(message)


app.run(debug=True) # means when i save the code, the changes are applied in the server
