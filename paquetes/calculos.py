def calcular_promedio_materias(notas: list, cantidad_alumnos: int) -> list:
    """
    Esta funcion recibe la matriz de notas de los estudiantes y saca el promedio general de las materias.
    calcula cada nota de una materia, calcula el promedio y lo guarda en una lista.
    Args:
        notas (list): Recibe la matriz de las notas de cada estudiante.
        cantidad_notas (int): recibe la cantidad total de notas que tiene cada alumno (son 5).
        tamaño_lista (int): recibe el tamaño para crear la lista donde se guardan los promedios.
    Returns:
        list: Devuelve una lista nueva con cada promedio calculado.
    """
    promedios_general_materias = [0] * len(notas[0])
    columna = 0
    fila = 0
    while columna < 5:
        variable_suma = 0
        for i in range(len(notas)):
            variable_suma += notas[i][columna]
            if i == 29:
                columna += 1
        promedio = (variable_suma / cantidad_alumnos) * 10 // 1
        promedio = promedio / 10
        promedios_general_materias[fila] = promedio
        fila += 1
    return promedios_general_materias


def calcular_promedio_maximo(lista: list) -> list:
    """
    Recibe una lista de numeros enteros y calcula cual es el numero maximo y si se repite.

    Args:
        lista_enteros (list): Recibe una lista definida con elementos ya ingresados.
    Returns:
        list: Devuelve las posiciones donde se encuentra el nro o los nros maximos
    """

    numero_maximo = lista[0]
    for index in range(len(lista)):
        numero = lista[index]
        if numero > numero_maximo:
            numero_maximo = numero

    contador = 0
    for i in range(len(lista)):
        if lista[i] == numero_maximo:
            numero_maximo = lista[i]
            contador += 1

    return numero_maximo


def calcular_promedio_estudiantes(
    notas: list, cantidad_notas: int, tamaño_lista: int
) -> list:
    """
    Esta funcion recibe la matriz de notas de los estudiantes y lo divide por la cantidad de notas totales de cada estudiantes para sacar el promedio general de cada uno y guardarlo en una nueva lista.
    Args:
        notas (list): Recibe la matriz de las notas de cada estudiante.
        cantidad_notas (int): recibe la cantidad total de notas que tiene cada alumno (son 5).
        tamaño_lista (int): recibe el tamaño para crear la lista donde se guardan los promedios.
    Returns:
        list: Devuelve una lista nueva con cada promedio calculado.
    """
    lista_promedios = [-1] * tamaño_lista
    for i in range(len(notas)):
        notas_sumadas = 0
        for j in range(len(notas[i])):
            variable_temporal = notas[i][j]
            notas_sumadas += variable_temporal
            promedio = notas_sumadas / cantidad_notas
            lista_promedios[i] = promedio

    return lista_promedios


def ordenar(
    lista_nombres: list,
    lista_edades: list,
    lista_generos: list,
    lista_legajos: list,
    lista_notas: list,
    lista_promedios: list,
    primer_modo=1,
    segundo_modo=1,
) -> list:
    """
    Esta funcion recibe 3 listas y el modo de como ordenar las listas(1= ascendente, 2=descendente).
        lista_nombres (list): Recibe la lista de nombres por parametro.
        lista_edades (list): Recibe la lista de edades por parametro.
        lista_generos (list): Recibe la lista de generos por parametro.
        lista_legajos (list): Recibe la lista de legajos por parametro.
        lista_notas (list): Recibe la lista de notas por parametro.
        lista_promedios (list): Recibe la lista de promedios por parametro.
        modo (int): por defecto es 1 pero su valor puede cambiar -> (1=ASCENDENTE, 2=DESCENDENTE).
    Returns:
        list: Retorna la lista o listas ordenada de manera ascendente o descendente.
    """

    for i in range(0, len(lista_nombres) - 1, 1):

        for j in range(i + 1, len(lista_nombres), 1):

            if (lista_promedios[i] > lista_promedios[j] and primer_modo == 1) or (
                lista_promedios[i] < lista_promedios[j] and primer_modo == 2
            ):

                edad_auxiliar = lista_edades[i]
                lista_edades[i] = lista_edades[j]
                lista_edades[j] = edad_auxiliar

                nombre_auxiliar = lista_nombres[i]
                lista_nombres[i] = lista_nombres[j]
                lista_nombres[j] = nombre_auxiliar

                genero_auxiliar = lista_generos[i]
                lista_generos[i] = lista_generos[j]
                lista_generos[j] = genero_auxiliar

                legajo_auxiliar = lista_legajos[i]
                lista_legajos[i] = lista_legajos[j]
                lista_legajos[j] = legajo_auxiliar

                notas_auxiliar = lista_notas[i]
                lista_notas[i] = lista_notas[j]
                lista_notas[j] = notas_auxiliar

                promedio_auxiliar = lista_promedios[i]
                lista_promedios[i] = lista_promedios[j]
                lista_promedios[j] = promedio_auxiliar
            # 2 criterio
            elif lista_promedios[i] == lista_promedios[j]:
                if (lista_nombres[i] > lista_nombres[j] and segundo_modo == 1) or (
                    lista_nombres[i] < lista_nombres[j] and segundo_modo == 2
                ):
                    edad_auxiliar = lista_edades[i]
                    lista_edades[i] = lista_edades[j]
                    lista_edades[j] = edad_auxiliar

                    nombre_auxiliar = lista_nombres[i]
                    lista_nombres[i] = lista_nombres[j]
                    lista_nombres[j] = nombre_auxiliar

                    genero_auxiliar = lista_generos[i]
                    lista_generos[i] = lista_generos[j]
                    lista_generos[j] = genero_auxiliar

                    legajo_auxiliar = lista_legajos[i]
                    lista_legajos[i] = lista_legajos[j]
                    lista_legajos[j] = legajo_auxiliar

                    notas_auxiliar = lista_notas[i]
                    lista_notas[i] = lista_notas[j]
                    lista_notas[j] = notas_auxiliar
