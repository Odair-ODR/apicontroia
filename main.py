from fastapi import FastAPI
from routers import usuario, login
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Para que hacepte peticiones de diferentes sitios, habilitamos el CORS (Cross-Origin Resource Sharing)
origins = [
    "http://127.0.0.1:5500",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routers
app.include_router(usuario.router)
app.include_router(login.router)
app.mount("/static", StaticFiles(directory="static"), name="stat")

@app.get("/root")
async def root():
    return "Hola"
