def calcular_puntuacion(puntos, bonus):
    """
    Esta funcion calcula la puntuacion del juego segun las siguientes instrucciones:
    ---> Oro si puntos >= 100 y bonus == True.
    ---> Plata si puntos >= 50 y puntos < 100.
    ---> Bronce si puntos < 50 o bonus == False.

    Parametros:
    puntos == int: La cantidad de puntos obtenidos.
    bonus == bool: Indica si se ha recibido un bonus.

    Retorno:
    str: "Oro", "Plata" o "Bronce" según la puntuación.
    """
    if puntos >= 100 and bonus:
        return "Oro"
    elif puntos >= 50 and puntos < 100 and bonus:
        return "Plata"
    else: puntos < 50
    return "Bronce"
    