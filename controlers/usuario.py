from dataBase.connectionDB import connection_db as cn
import pandas as pd
from dataBase.models.usuario import Usuario, UsuarioDB
import dataBase.schemas.usuario as usuario_eschema

def listarUsurios() -> list:
    try:
        sentencia = "SELECT * FROM USUARIO"
        data_reader = pd.read_sql(sentencia, cn)
        #data_redear = pd.DataFrame(data_reader, columns=data_reader.columns)
        return usuario_eschema.users_schema_odbc(data_reader.iloc)
    except Exception as ex:
        raise ex
    #finally:
        #cn.close()


def buscar_usuario_id(idUsuario: int) -> Usuario:
    cursor = cn.cursor()
    try:
        sentencia = "SELECT * FROM USUARIO WHERE ID_USUARIO = ?"
        parameter = (idUsuario)
        cursor.execute(sentencia, parameter)
        row = cursor.fetchone()
        if row == None:
            return None

        if len(row):
            usuario = usuario_eschema.user_schema_odbc(row)
            return Usuario(**usuario)
        return None
    except Exception as ex:
        raise ex
    finally:
        cursor.close()
        #cn.close()


def buscar_usuario_nickname(nick_name: str) -> Usuario:
    cursor = cn.cursor()
    try:
        sentencia = "SELECT * FROM USUARIO WHERE NICK_USUARIO = ?"
        parameter = (nick_name)
        cursor.execute(sentencia, parameter)
        row = cursor.fetchone()
        if row == None:
            return None

        if len(row):
            usuario = usuario_eschema.user_schema_odbc(row)
            return Usuario(**usuario)
        return None
    except Exception as ex:
        raise ex
    finally:
        cursor.close()
        #cn.close()

def buscar_usuario_nickname_db(nick_name: str) -> UsuarioDB:
    cursor = cn.cursor()
    try:
        sentencia = "SELECT * FROM USUARIO WHERE NICK_USUARIO = ?"
        parameter = (nick_name)
        cursor.execute(sentencia, parameter)
        row = cursor.fetchone()
        if row == None:
            return None

        if len(row):
            usuario = usuario_eschema.user_schema_odbc_db(row)
            return UsuarioDB(**usuario)
        return None
    except Exception as ex:
        raise ex
    finally:
        cursor.close()
        #cn.close()


def insertar_usuario(usuario: UsuarioDB) -> Usuario:
    cursor = cn.cursor()
    try:
        sentencia = "{call dsp_InsertarUsuario(?,?,?)}"
        parameter = (usuario.NOMBRE_USUARIO, usuario.NICK_USUARIO, usuario.CONTRASEÑA_USUARIO)
        cursor.execute(sentencia, parameter)
        cursor.commit()
        if cursor.rowcount > 0:
            return buscar_usuario_nickname(usuario.NICK_USUARIO)
        return None
    except Exception as ex:
        raise ex
    finally:
        cursor.close()
        #cn.close()

def actualizar_usuario(usuario: UsuarioDB) -> Usuario:
    cursor = cn.cursor()
    try:
        sentencia = "{call dsp_ActualizarUsuario(?,?,?,?)}"
        parameter = (usuario.ID_USUARIO, usuario.NOMBRE_USUARIO, usuario.NICK_USUARIO, usuario.CONTRASEÑA_USUARIO)
        cursor.execute(sentencia, parameter)
        cursor.commit()
        if cursor.rowcount > 0:
            return buscar_usuario_nickname(usuario.NICK_USUARIO)
        return None
    except Exception as ex:
        raise ex
    finally:
        cursor.close()
        #cn.close()

def eliminar_usuario(idUsuario: int) -> bool:
    cursor = cn.cursor()
    try:
        sentencia = "{call dsp_EliminarUsuario(?)}"
        parameter = (idUsuario)
        cursor.execute(sentencia, parameter)
        cursor.commit()
        if cursor.rowcount > 0:
            return True
        return False
    except Exception as ex:
        raise ex
    finally:
        cursor.close()
        #cn.close()

