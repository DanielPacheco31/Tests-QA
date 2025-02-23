import re

def validar_email(email):
    """
    Esta funcion valida un email segun las siguientes instrucciones:
    ---> Formato usuario@dominio.extension.
    ---> usuario: Solo letras, numeros, ., _, y `.
    ---> dominio: Letras, numeros, y guiones.
    ---> extension: 2 a 4 letras.

    Parameto:
    email "str": para validar el correo.

    Returns:
    bool: True si el email es valido, False si no lo es.

    re: pertenece a la blioteca estandar de python e incluye el patron utilizado.
    """
    patron = r'^[a-zA-Z0-9._`]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}$'
    return re.match(patron, email) is not None