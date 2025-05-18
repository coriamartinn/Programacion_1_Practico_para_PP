from paquetes.validates import validar_legajo_alumno
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


def busqueda_alumno(
    legajos_estudiantes: list,
    nombres_estudiantes: list,
    edades_estudiantes: list,
    generos_estudiantes: list,
    notas_estudiantes: list,
    promedio_estudiantes: list,
) -> None:
    """
    Esta funcion realiza la busqueda de alumnos por legajo. Pide AL usuario su legajo, si existe muestra los datos de ese.
    Si no existe -> indica que no existe en el sistema y le pregunta si quiere seguir buscando S/N.
    Args:
    legajos_estudiantes (list):Recibe la lista de legajos guardada en el sistema.
    nombres_estudiantes (list):Recibe la lista de nombres guardada en el sistema.
    edades_estudiantes (list):Recibe la lista de edades guardada en el sistema.
    generos_estudiantes (list):Recibe la lista de generos guardada en el sistema.
    notas_estudiantes (list):Recibe la lista de notas guardada en el sistema.
    promedio_estudiantes (list):Recibe la lista de promedios guardada en el sistema.
    Returns:
        None: No tiene retorno, llama a la funcion mostrar_dato() si el legajo ingresado existe en el sistema.
    """

    while True:
        legajo = int(input("Ingrese el numero de Legajo: "))
        indice = validar_legajo_alumno(legajos_estudiantes, legajo)
        if indice == -1:
            print("ERROR, el legajo que buscas no existe en el sistema.")
        else:
            mostrar_dato(
                nombres_estudiantes,
                edades_estudiantes,
                generos_estudiantes,
                legajos_estudiantes,
                notas_estudiantes,
                promedio_estudiantes,
                indice,
            )
        continuar = input("Desea continuar?: s/n: ")
        continuar = to_lower(continuar)
        if continuar == "n":
            break
