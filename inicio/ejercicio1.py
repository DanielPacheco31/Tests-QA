
def validar_usuario(nombre):
    """
    Esta funcion verifica si un nombre de usuario es valido segun los siguientes instrucciones:
    - La longitud del nombre debe estar entre 5 y 15 caracteres.
    - No debe contener espacios.
    - Solo debe contener letras (mayúsculas/minúsculas) y números.

    Parametro:
    nombre (str): Para validar el nombre de usuario.

    Retorno:
    bool: True si el nombre de usuario es valido, False si no lo es.
    """
    if len(nombre) < 5 or len(nombre) > 15:
        """
        Verifica si la longitud del nombre de usuario es menor que 5 o mayor que 15 caracteres.
        Si es así, el nombre de usuario no es válido.
        """
        return False
    if " " in nombre:
        """
        Verifica si el nombre de usuario contiene espacios.
        Si contiene espacios, el nombre de usuario no es válido.
        """
        return False
    for c in nombre:
        """
        Recorre cada carácter en el nombre de usuario para verificar si es alfanumérico.
        Si encuentra algún carácter que no sea alfanumérico, el nombre de usuario no es válido.
        """
        if not c.isalnum():
            return False
        """
        Si todas las verificaciones anteriores pasan, el nombre de usuario es válido.
        """
    return True