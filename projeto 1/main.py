from fastapi import FastAPI
from routers import router

app = FastAPI()
app.include_router(router=router)

@app.get('/')
def say_hello_to_user():
    return {'message': 'Hello world'}
