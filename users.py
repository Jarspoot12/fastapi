from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad User
class User(BaseModel): # el BaseModel permite crear la entidad, lo maneja como JSON
    id: int
    name: str
    surname: str
    url: str
    age: int

# ejemplo de listado de usuarios globales
user_list = [User(id=1, name="Jared", surname="Poot", url="http://jared.com", age=25),
         User(id=2, name="Jared2", surname="Poot2", url="http://jared2.com", age=26),
         User(id=3, name="Jared3", surname="Poot3", url="http://jared3.com", age=27)]

@app.get("/users") # raíz de la ip donde se despliega la app
async def users(): # siempre que llamamos a un servidor la petición es asíncrona
    return user_list

# recuperamos usuarios por ID, usaremos parámetros de PATH (dentro de la URL)
# usados para peticiones con parámetros fijos
@app.get("/user/{id}") 
async def user(id: int):
    users = filter(lambda user: user.id==id, user_list) # función de orden superior, operaciones complejas
    try:
        return list(users)[0]
    except:
        return {"message": "No existe el usuario solicitado"}

# parámetros que no hacen parte de los parámetros de path --> parámetros de QUERY, por ejemplo, indicar cuántos usuarios queremos traer
# usados para peticiones con parámetros no obligatorios (como la paginación)
@app.get("/user/") # vamos a acceder al user con la URL "http://127.0.0.1:8000/userquery/?id=1" 
async def user(id: int):
    users = filter(lambda user: user.id==id, user_list) # función de orden superior, operaciones complejas
    try:
        return list(users)[0]
    except:
        return {"message": "No existe el usuario solicitado"}
# anteriormente pudimos usar la misma función, una metiendo el prámetro por el path y otra en la query


