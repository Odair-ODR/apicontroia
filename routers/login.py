from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from dataBase.models.usuario import Usuario
from controlers import usuario as user_controller

# Instancias
router = APIRouter(prefix="/login",
                   tags=["login"], responses={404: {"datail": "Not found"}})
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# ALGORITMO PARA ENCRIPTAR CONTRASEÑA
# bcrypt => algoritmo de incriptación
ALGORITHM = "HS256"
SECRET_KEY = "$2a$12$8ZG1VpgE7ZXlp4h9TEVbo.4N6qF0xhwNr/gkFje8tt9NyphOuumQ."
crypt = CryptContext(schemes=["bcrypt"])

# SOBRE EL TOKEN
ACCESS_TOKEN_EXPIRET_MINUTES = 50


# OAuth2PasswordBearer => gestiona la autenticación
# OAuth2PasswordRequestForm => forma de cómo se va enviar los datos de autenticación al backend y capturarlos en el backend


@router.post("/")
async def login(form_autentiation: OAuth2PasswordRequestForm = Depends()):
    usuario = user_controller.buscar_usuario_nickname(form_autentiation.username)
    if not usuario:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            "El usurio ingresado no es correcto")

    usuariodb = user_controller.buscar_usuario_nickname_db(form_autentiation.username)
    # verificamos si la contraseña es igual a la contraseña encriptada de la base de datos
    if not crypt.verify(form_autentiation.password, usuariodb.CONTRASEÑA_USUARIO):
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            "La contraseña no es correcta")

    # agregar el valor de ACCESS_TOKEN_EXPIRET_MINUTES en minutos a la fecha actual
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRET_MINUTES)
    access_token = {
        "sub": usuariodb.NICK_USUARIO,
        "exp": expire,
    }

    return {"access_token": jwt.encode(access_token, SECRET_KEY, ALGORITHM), "token_type": "bearer"}


async def oauth2_usuario(token: str = Depends(oauth2)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación no válidas",
        headers={"www.autenticate": "Bearer"})
    try:
        nick_name = jwt.decode(token, SECRET_KEY, ALGORITHM).get("sub")
        if nick_name is None:
            raise exception
        usuario = user_controller.buscar_usuario_nickname(nick_name)
        return usuario
    except JWTError:
        raise exception


async def usuario_logueado(usuario: Usuario = Depends(oauth2_usuario)):
    if usuario.ESTADO == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return usuario


@router.get("/perfil")
async def perfil(usuario: Usuario = Depends(usuario_logueado)):
    return usuario