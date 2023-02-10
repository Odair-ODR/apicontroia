from fastapi import APIRouter, HTTPException, Depends, status
from dataBase.models.usuario import Usuario, UsuarioDB
from controlers import usuario as user_controller
from routers import login

# Instancias
router = APIRouter(prefix="/usuarios",
                   tags=["usuarios"], responses={404: {"datail": "Not found"}})


@router.get("/", response_model=list[Usuario], status_code=status.HTTP_200_OK)
async def usuarios(_ = Depends(login.usuario_logueado)):
    return user_controller.listarUsurios()


# Busqueda por path => http://127.0.0.1:8000/usuarios/id/1
@router.get("/id/{idUsuario}")
async def usuarioXId(idUsuario: int, _ = Depends(login.usuario_logueado)):
    return obtener_usuario_id(idUsuario)


# Busqueda por query => http://127.0.0.1:8000/usuarios/id/?idUsu=1
@router.get("/id/")
async def usuarioXId(idUsu: int, _ = Depends(login.usuario_logueado)):
    return obtener_usuario_id(idUsu)


def obtener_usuario_id(idUsuario: int):
    usuario = None
    try:
        usuario = user_controller.buscar_usuario_id(idUsuario)
        if usuario == None:
            raise
        return usuario
    except Exception as ex:
        if usuario == None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="El usuario no existe")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(ex))

# response_model = Usuario,
@router.post("/create", status_code=status.HTTP_201_CREATED)
async def crear_usuario(usuario: UsuarioDB, _ = Depends(login.usuario_logueado)):
    try:
        if type(user_controller.buscar_usuario_nickname(usuario.NICK_USUARIO)) == Usuario:
            return not_found_exception("El usuario ya existe")
            
        usuario_inserted = user_controller.insertar_usuario(usuario)
        if type(usuario_inserted) != Usuario:
            return not_found_exception("No se pudo insertar el usuario")
        print(type(usuario_inserted))
        return usuario_inserted
    except Exception as ex:
        raise not_found_exception(str(ex))


@router.put("/update", status_code=status.HTTP_200_OK)
async def actualizar_usuario(usuario: UsuarioDB, _ = Depends(login.usuario_logueado)):
    try:
        if type(user_controller.buscar_usuario_nickname(usuario.NICK_USUARIO)) == Usuario:
            return not_found_exception("El nombre de usuario ya existe")

        usuario_updated = user_controller.actualizar_usuario(usuario)
        if type(usuario_updated) != Usuario:
            return not_found_exception("No se pudo actualizar el usuario")

        return usuario_updated
    except Exception as ex:
        raise not_found_exception(str(ex))


@router.delete("/delete/{idUsuario}", status_code=status.HTTP_200_OK)
async def eliminar_usuario(idUsuario: int, _ = Depends(login.usuario_logueado)):
    try:
        usuario = user_controller.buscar_usuario_id(idUsuario)
        if type(usuario) != Usuario:
            return not_found_exception("El usuario no existe")

        usuario_deleted = user_controller.eliminar_usuario(idUsuario)
        if not usuario_deleted:
            return not_found_exception("No se pudo actualizar el usuario")
            
        return usuario
    except Exception as ex:
        raise not_found_exception(str(ex))


def not_found_exception(message: str):
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message)

