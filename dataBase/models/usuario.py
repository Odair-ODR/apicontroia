from pydantic import BaseModel
from typing import Optional


class Usuario(BaseModel):
    ID_USUARIO: int
    NOMBRE_USUARIO: str
    NICK_USUARIO: str
    ESTADO: int
    FECHA_CREACION: str
    FECHA_MODIFICACION: Optional[str] = None

class UsuarioDB(BaseModel):
    ID_USUARIO: Optional[int] = None
    NOMBRE_USUARIO: str
    NICK_USUARIO: str
    CONTRASEÑA_USUARIO: str
    ESTADO: Optional[int] = None
    FECHA_CREACION: Optional[str] = None
    FECHA_MODIFICACION: Optional[str] = None


class UsuarioTo():
    def __init__(self):
        self._usuario: Usuario
        self._CONTRASEÑA_USUARIO: str

    def usuario(self):
        return self._usuario

    def usuario(self, usuario: Usuario):
        self._usuario = usuario

    def constraseña(self):
        return self._CONTRASEÑA_USUARIO
    
    def constraseña(self, constraseña: str):
        self._CONTRASEÑA_USUARIO = constraseña