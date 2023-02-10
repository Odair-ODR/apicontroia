from pandas.core import series
from dataBase.models.usuario import Usuario

def user_schema_odbc(usuario) -> dict:
    return {
        'ID_USUARIO': usuario.ID_USUARIO,
        'NOMBRE_USUARIO': usuario.NOMBRE_USUARIO,
        'NICK_USUARIO': usuario.NICK_USUARIO,
        'ESTADO': usuario.ESTADO,
        'FECHA_CREACION': str(usuario.FECHA_CREACION),
        'FECHA_MODIFICACION': str(usuario.FECHA_MODIFICACION)
    }

def user_schema(usuario: series) -> dict:
    return {
        'ID_USUARIO': usuario["ID_USUARIO"],
        'NOMBRE_USUARIO': usuario["NOMBRE_USUARIO"],
        'NICK_USUARIO': usuario["NICK_USUARIO"],
        'ESTADO': usuario["ESTADO"],
        'FECHA_CREACION': str(usuario["FECHA_CREACION"]),
        'FECHA_MODIFICACION': str(usuario["FECHA_MODIFICACION"])
    }

def users_schema_odbc(usuarios) -> list:
    """lista_usuario = []
    for row in usuarios:
        usuario = user_schema_odbc(row)
        lista_usuario.append(Usuario(**usuario))
    return lista_usuario"""
    return [user_schema_odbc(row) for row in usuarios]

def user_schema_odbc_db(usuario) -> dict:
    return {
        'ID_USUARIO': usuario.ID_USUARIO,
        'NOMBRE_USUARIO': usuario.NOMBRE_USUARIO,
        'NICK_USUARIO': usuario.NICK_USUARIO,
        'CONTRASEÑA_USUARIO': usuario.CONTRASEÑA_USUARIO,
        'ESTADO': usuario.ESTADO,
        'FECHA_CREACION': str(usuario.FECHA_CREACION),
        'FECHA_MODIFICACION': str(usuario.FECHA_MODIFICACION)
    }