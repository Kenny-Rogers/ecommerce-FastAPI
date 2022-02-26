from fastapi import FastAPI

# create a fast API defining meta data about the API
app = FastAPI(title='Sample Docs',
              description='This is private docs',
              version='1.0')


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: int):
    return {"message": f"Hello {name}"}
