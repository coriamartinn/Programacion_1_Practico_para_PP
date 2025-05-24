from paquetes.funciones_propias import to_upper
from paquetes.validates import validate_cadena, validate_number


def cargar_nombre() -> str:
    """
    Esta funcion se utiliza para cargar el Nombre y el Apellido de los alumnos.
    Args:
        No recibe parametros formales.
    Returns:
        str: Retorna el nombre ingresado.
    """
    while True:
        nombre = input("Nombre y Apellido: ")
        validacion = validate_cadena(nombre)
        if validacion == True:
            break
        print("ERROR, no es un nombre válido!!")

    return nombre


def cargar_edad() -> int:
    """
    Esta funcion se utiliza para cargar las edades de los alumnos.
    Args:
        No recibe parametros formales.
    Returns:
        int: Retorna la edad ingresada.
    """
    while True:
        edades = input("Edad: ")
        validacion_edad = validate_number(edades)
        if validacion_edad == True:
            edades = int(edades)
            if edades > 17:
                break
        print("ERROR, no es una edad valida!!")

    return edades


def cargar_genero() -> str:
    """
    Esta funcion se utiliza para cargar los generos de los alumnos.
    Args:
        No recibe parametros formales.
    Returns:
        str: Retorna el genero ingresado.
    """
    while True:
        genero = input("Genero: ")
        genero = to_upper(genero)
        if genero == "F" or genero == "M" or genero == "X":
            break
        print("ERROR, no es Genero valido!! (F=FEMENINO, M=MASCULINO, X=BINARIO)")

    return genero


def cargar_legajos() -> int:
    """
    Esta funcion se utiliza para cargar los legajos de los alumnos.
    Args:
        No recibe parametros formales.
    Returns:
        int: Retorna el legajo ingresado.
    """
    while True:
        legajos = input("Legajo: ")
        validacion_legajos = validate_number(legajos)
        if validacion_legajos == True:
            legajos = int(legajos)
            if legajos >= 10000 and legajos <= 99999:
                break
        print("ERROR, no es un legajo valido!!")

    return legajos


def cargar_lista_secuencial(
    nombres: list, edades: list, generos: list, legajos: list, tamanio: int
) -> None:
    print(
        "Ingresaste al sistema para cargar Nombre, Edad, Genero y legajo del estudiante."
    )
    for i in range(tamanio):
        nombres[i] = cargar_nombre()
        edades[i] = cargar_edad()
        generos[i] = cargar_genero()
        legajos[i] = cargar_legajos()


def cargar_matriz_secuencialmente(matriz: list) -> list:
    """
    Esta funcion carga secuencialmente los datos de una matriz
    Args:
        matriz (list): Recibe una matriz ya inicializada como parametro.
    Returns:
        list: Devuelve la matriz con los datos ya cargados.
    """

    print("Ingresaste al sistema para cargar las notas.")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            while True:
                dato = input(f"Fila {i}: Columna {j}: ")
                if dato == "":
                    print(
                        "ERROR, el dato no puede estar vacio!!, las notas deben ser del 1 al 10."
                    )
                else:
                    validacion = validate_number(dato)
                    if validacion == True:
                        dato = int(dato)
                    else:
                        print(
                            "ERROR, el dato no es valido!!, las notas deben ser del 1 al 10."
                        )
                        continue
                    if dato < 1 or dato > 10:
                        print(
                            "ERROR, el dato no es valido!!, las notas deben ser del 1 al 10."
                        )
                    else:
                        matriz[i][j] = dato
                        break


def materias_por_nombre(notas: list) -> list:
    """
    Esta funcion busca en la matriz de las notas, cuales son por promedio las notas mas altas para luego guardarla en una lista y llamar para mostrar esas con mejor promedio.
    Args:
        notas (list): matriz cada alumno y su respectivas notas.
    Returns:
        list: Retorna una lista nueva con las materias con mejor promedio.
    """
    materias_mejor_promedio = [""] * len(notas[0])
    columna = 0
    fila = 0
    while columna < 5:
        variable_suma = 0
        for i in range(len(notas)):
            variable_suma += notas[i][columna]
        promedio = f"materia_{fila+1}"
        materias_mejor_promedio[fila] = promedio
        fila += 1
        columna += 1
    return materias_mejor_promedio
