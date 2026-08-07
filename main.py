from fastapi import FastAPI

app = FastAPI()

@app.get("/") # raíz de la ip donde se despliega la app
async def root(): # siempre que llamamos a un servidor la petición es asíncrona
    return {"message": "Hello fastAPI"}

@app.get("/url")
async def url():
    return {"url":"https://miurl.com"}

