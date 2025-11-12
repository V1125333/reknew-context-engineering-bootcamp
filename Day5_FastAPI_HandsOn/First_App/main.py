from fastapi import FastAPI                                   #Here we are importing FastAPI class from fastapi modeule.  

app = FastAPI()                     #creating a FastAPI instance

@app.get("/")                       #defining a route using the decorator syntax
def read_root():                    #defining a function that will be called when the route is accessed
    return {"Hello": "World"}       #returning a JSON response

@app.get("/items")
def read_items():                  #defining another route
    return {"items": ["item1", "item2", "item3"]}  #returning a JSON response with a list of items
