from paquetes.validates import validar_legajo_alumno, validate_number
from paquetes.visualizacion import mostrar_dato


def inicializar_matriz(
    cantidad_filas: int, cantidad_columnas: int, valor_inicial=-1
) -> list:
    """
    Esta funcion crea la matriz necesaria segun los parametros pasados
    Args:
        cantidad_filas (int): recibe un numero entero para saber cuantas filas tendra la matriz.
        cantidad_columnas (int): recibe un numero entero para saber cuantas columnas tendra la matriz.
    Returns:
        list: Devuelve la matriz con los valores pasados por parametro.
    """

    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]

    return matriz


def to_lower(cadena: str) -> str:
    """
    Esta funcion recibe una cadena de caracteres y la vuelve toda en caracteres minusculas.
    Args:
        cadena (str): Recibe una cadena de caracteres.
    Returns:
        str: Retorna la cadena pasada a minuscula
    """
    palabra_minusculas = ""
    caracter = ""
    for i in range(len(cadena)):
        if ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90:
            caracter = chr(ord(cadena[i]) + 32)
        else:
            caracter = cadena[i]
        palabra_minusculas += caracter
    return palabra_minusculas


def to_upper(cadena: str) -> str:
    """
    Esta funcion recibe una cadena de caracteres y la vuelve toda en caracteres MAYUSCULAS.
    Args:
        cadena (str): Recibe una cadena de caracteres.
    Returns:
        str: Retorna la cadena pasada a MAYUSCULAS.
    """
    palabra_minusculas = ""
    caracter = ""
    for i in range(len(cadena)):
        if ord(cadena[i]) >= 97 and ord(cadena[i]) <= 122:
            caracter = chr(ord(cadena[i]) - 32)
        else:
            caracter = cadena[i]
        palabra_minusculas += caracter
    return palabra_minusculas


def opcion_menu(menu: str) -> int:
    """
    Esta funcion va a retornar la opcion validada para ingresar en el case correspondiente del match
    Args:
        opcion (str): Recibe la opcion tipo cadena para validar
    Returns:
        int: Retorna la opcion elegida parseada a int.
    """
    print(menu)
    opcion = input(f"Ingrese una opcion: ")
    validacion = validate_number(opcion)
    if validacion == True:
        opcion = int(opcion)

    return opcion
