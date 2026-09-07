from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def decir_hola():
    return {"mensaje": "Hola mundo! mi servidor FastAPI está funcionando"}
  
