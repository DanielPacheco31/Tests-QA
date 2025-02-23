import re

def validar_telefono(telefono):
    """
    Esta funcion valida numeros de telefonos que tenga el formato solicitado +XX-XXX-XXX-XXXX.

    Parametro:
    telefono string: Numero de telefono a verificar.

    Retorno:
    bool: True si el numero de telefono es valido, False si no lo es.
    """
    patron = r'^\+\d{2}-\d{3}-\d{3}-\d{4}$'
    return re.match(patron, telefono) is not None