from inicio import ejercicio1, ejercicio2, ejercicio3,ejercicio4

"""....................Aqui empieza el ejercicio 1............................................."""

def test_validar_usuario():
    """
    Esta funcion realiza varias pruebas para verificar que la func validar_usuario()
    funcione correctamente.

    Las pruebas incluyen casos validos ey casos invalidos:
    ---> Casos False:
        1. Nombre muy corto.
        2. Caracter especial (_) no permitido.
        3. Convinacion de numeros y letras con mas de 15 caracteres.
        4. Usuario numerico con mas de 15 caracteres.
        5. Caracter especial (!) no permitido.
        6. Contiene espacio no permitido.
    """
    #casos False
    assert ejercicio1.validar_usuario("Ana") == False
    assert ejercicio1.validar_usuario("Juan_Perez") == False
    assert ejercicio1.validar_usuario("ABC23456789012345") == False 
    assert ejercicio1.validar_usuario("1234567890123456") == False 
    assert ejercicio1.validar_usuario("UsuarioNombre!") == False
    assert ejercicio1.validar_usuario("Usuario Nombre") == False 

    """
    ---> Casos True:
        1. Nombre de usuario numerico con minimo 5 caracteres.
        2. Nombre de usuario con letras con minimo 5 caracteres.
        3. Nombre de usuario convinando letras miniscula y numeros de 6 caracteres.
        4. Nombre de usuario con letras y numeros no excede los 15 caracteres.
    """
    #casos True
    assert ejercicio1.validar_usuario("12345") == True
    assert ejercicio1.validar_usuario("ABCDE") == True
    assert ejercicio1.validar_usuario("a1b2c3") == True 
    assert ejercicio1.validar_usuario("UsuarioValido12") == True

    """
    Estas pruebas de realizaron siguiendo las siguientes instrucciones:
        ---> La longitud del nombre debe estar entre 5 y 15 caracteres.
        ---> No debe contener espacios.
        ---> Solo debe contener letras (mayúsculas/minúsculas) y números.
    """

"""....................Aqui empieza el ejercicio 2............................................."""

def test_calcular_puntuacion():
    """
    Esta funcion realiza varias pruebas para verificar que la func calcular_puntuacion()
    funcione correctamente.

    Las pruebas incluyen:
    ---> Casos donde se debe retornar "Oro".
    ---> Casos donde se debe retornar "Plata".
    ---> Casos donde se debe retornar "Bronce".
    """
    # Casos Oro
    assert ejercicio2.calcular_puntuacion(100, True) == "Oro"
    assert ejercicio2.calcular_puntuacion(120, True) == "Oro"

    # Casos Plata
    assert ejercicio2.calcular_puntuacion(50, True) == "Plata"
    assert ejercicio2.calcular_puntuacion(80, True) == "Plata"
    assert ejercicio2.calcular_puntuacion(75, True) == "Plata"

    # Casos Bronce
    assert ejercicio2.calcular_puntuacion(15, False) == "Bronce"
    assert ejercicio2.calcular_puntuacion(20, False) == "Bronce"
    assert ejercicio2.calcular_puntuacion(30, False) == "Bronce"
    assert ejercicio2.calcular_puntuacion(2, True) == "Bronce"
    assert ejercicio2.calcular_puntuacion(25, False) == "Bronce"

"""....................Aqui empieza el ejercicio 3............................................."""


def test_validar_email():
    """
    Esta funcion realiza pruebas para verificar que la funcion validar_email(email)
    se ejecute correctamenre.

    Las pruebas incluyen:
    ---> Casos True:
        Correos con todas sus caracteristicas: usuario@dominio.extencion e incluso un - en el dominio.

    ---> Casos False:
        1.Correo con falta de extencion
        2.Caracter # no permitido
        3.Extencion incorrecta
        4.Doble punto en el dominio
        5.Sin extencion
        6.Extencion incompleta
        7.Sin usuario
        8.Sin dominio

    """
    # Casos True
    assert ejercicio3.validar_email("danielpacsota93@gmail.com") == True
    assert ejercicio3.validar_email("usuario@dominio-.com") == True
    
    # Casos False
    assert ejercicio3.validar_email("maria@dominio") == False 
    assert ejercicio3.validar_email("pedro#2024@mail.org") == False
    assert ejercicio3.validar_email("user@dominio.extended") == False
    assert ejercicio3.validar_email("user@domain..com") == False
    assert ejercicio3.validar_email("user@domain") == False
    assert ejercicio3.validar_email("usuario@dominio.c") == False 
    assert ejercicio3.validar_email("@dominio.com") == False
    assert ejercicio3.validar_email("usuario@.com") == False

"""....................Aqui empieza el ejercicio 4............................................."""

def test_validar_telefono():
    """
    Esta funcion realiza pruebas para verificar que la funcion validar_telefono()
    se ejecute correctamente.

    Las pruebas incluyen:
    ---> Casos True:
        Un numero que cumple con el formato solicitado.

    ---> Casos False:
        1.Falta el signo +
        2.Codigo del pais con mas de 2 numeros
        3.Codigo de area con mss de 3 numeros
        4.Primer segmento con mas de 3 numeros
        5.Segundo segmento con mas de 4 numeros
        6.Codigo de area con menos de 3 numeros
        7.Primer segmento con menos de 3 numeros
        8.Segundo segmento con menos de 4 numeros
        9.Letras el codigo del pais

    """
    # Caso True
    assert ejercicio4.validar_telefono("+12-345-678-9012") == True
    
    # Casos False
    assert ejercicio4.validar_telefono("12-345-678-9012") == False
    assert ejercicio4.validar_telefono("+123-456-789-0123") == False
    assert ejercicio4.validar_telefono("+12-3456-789-0123") == False
    assert ejercicio4.validar_telefono("+12-345-6789-0123") == False
    assert ejercicio4.validar_telefono("+12-345-678-01234") == False
    assert ejercicio4.validar_telefono("+12-34-678-9012") == False
    assert ejercicio4.validar_telefono("+12-345-67-9012") == False
    assert ejercicio4.validar_telefono("+12-345-678-912") == False 

    