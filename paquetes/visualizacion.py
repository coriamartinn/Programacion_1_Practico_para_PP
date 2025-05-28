def mostrar_dato(
    nombres: list,
    edades: list,
    generos: list,
    legajos: list,
    notas: list,
    promedio: list,
    indice: int,
) -> None:
    """
    Esta funcion Recibe los datos de los usuarios y los muestra 1 por 1 -> ordenados de Nombre, Edades, Genero, Legajo, Notas y promedio.
    Args:
        nombres (int): Recibe la lista de nombres de los alumnos.
        edades (int): Recibe la lista de edades de los alumnos.
        generos (int): Recibe la lista de generos de los alumnos.
        legajos (int): Recibe la lista de legajos de los alumnos.
        notas (list): Recibe la matriz con cada alumno y sus respectivas notas.
        promedio (list): recibe la lista de los promedios de los alumnos, si no los promedios no fueron calculados muestra -> NO CALCULADO.
        indice (int): recibe un indice, para poder ingresar a cada elemento de cada lista.
    Returns:
        None: No existe retorno -> Muestra por pantalla.
    """
    if promedio == [0] * len(nombres):
        if len(nombres[indice]) >= 16:
            print(
                f"{nombres[indice]}\t{edades[indice]}\t{generos[indice]}\t{legajos[indice]}\t{notas[indice]}\t No calculado"
            )
        else:
            print(
                f"{nombres[indice]}\t\t{edades[indice]}\t{generos[indice]}\t{legajos[indice]}\t{notas[indice]}\t No calculado"
            )
    else:
        if len(nombres[indice]) >= 16:
            print(
                f"{nombres[indice]}\t{edades[indice]}\t{generos[indice]}\t{legajos[indice]}\t{notas[indice]}\t\t{promedio[indice]}"
            )
        else:
            print(
                f"{nombres[indice]}\t\t{edades[indice]}\t{generos[indice]}\t{legajos[indice]}\t{notas[indice]}\t\t{promedio[indice]}"
            )


def mostrar_datos(
    nombres: list,
    edades: list,
    generos: list,
    legajos: list,
    notas: list,
    promedio: list,
    tamanio: int,
) -> None:
    """
    Esta funcion Recibe los datos de los usuarios y los muestra 1 por 1 -> ordenados de Nombre, Edades, Genero, Legajo, Notas y promedio.
    Args:
        nombres (int): Recibe la lista de nombres de los alumnos.
        edades (int): Recibe la lista de edades de los alumnos.
        generos (int): Recibe la lista de generos de los alumnos.
        legajos (int): Recibe la lista de legajos de los alumnos.
        notas (list): Recibe la matriz con cada alumno y sus respectivas notas.
        promedio (list): recibe la lista de los promedios de los alumnos, si no los promedios no fueron calculados muestra -> NO CALCULADO.
        tamanio (int): recibe la longitud de las listas para poder iterar de forma correcta en el bucle.
    Returns:
        None: No existe retorno -> muestra por pantalla el titulo de cada dato e itera por el tamaño de la lista y
        llama a mostrar_dato() para imprimirlos por pantalla.
    """
    print("NOMBRES Y APELLIDO\tEDAD\tGENERO\tLEGAJO\tNOTAS\t\t PROMEDIO GENERAL")
    for i in range(tamanio):
        mostrar_dato(nombres, edades, generos, legajos, notas, promedio, i)


def mostrar_materia(materias: list, promedio_materias: list, indice: int) -> None:
    """
    Esta funcion Recibe las materias existentes, el promedio de cada una de esas materias y los muestra 1 por 1 por pantalla
    -> ordenados de Materias, promedio -> si no esta calculado indica -> NO CALCULADO
    Args:
        materias (list): Recibe la lista de materias de los alumnos.
        promedio_materias (list): Recibe la lista de los promedios de esas materias.
        indice (int): recibe el indice para entrar a cada dato de esas listas.
    Returns:
        None: No existe retorno -> muestra por pantalla cada dato que se pide anteriormente por parametro formal.
    """
    if promedio_materias == [0] * len(materias):
        if len(materias[indice]) >= 16:
            print(f"\t{materias[indice]}\t No calculado")
        else:
            print(f"\t{materias[indice]}\t No calculado")
    else:
        if len(materias[indice]) >= 16:
            print(f"\t{materias[indice]}\t\t{promedio_materias[indice]}")
        else:
            print(f"\t{materias[indice]}\t\t{promedio_materias[indice]}")


def mostrar_materias(
    materias: list, promedio: list, promedio_maximo: list, tamano: int
) -> None:
    """
    Esta funcion Recibe los datos de los usuarios y los muestra 1 por 1 -> ordenados de Nombre, Edades, Genero, Legajo, Notas y promedio.
    Args:
        materias (list): Recibe la lista con las materias existentes.
        promedio (list): Recibe la lista con los promedios de cada materia existentes.
        promedio_maximo (int): Recibe cual es la mayor nota dentro de las materias existentes.
        tamanio (int): recibe la longitud de las listas para poder iterar de forma correcta en el bucle.
    Returns:
        None: No existe retorno -> muestra por pantalla el titulo de cada dato e itera por el tamaño de la lista y
        llama a mostrar_dato() para imprimirlos por pantalla. OBSERVACION -> (La función va a mostrar solamente la/s materia/s que tengan mejor promedio)
    """
    print("MATERIAS\t\tPROMEDIO GENERAL")
    for i in range(tamano):
        if promedio[i] == promedio_maximo:
            mostrar_materia(materias, promedio, i)


def mostrar_materia_repetida(lista_numeros_repetidos: list, indice: int) -> None:
    """
    Esta funcion Recibe las materias existentes, el promedio de cada una de esas materias y los muestra 1 por 1 por pantalla
    -> ordenados de Materias, promedio -> si no esta calculado indica -> NO CALCULADO
    Args:
        materias (list): Recibe la lista de materias de los alumnos.
        promedio_materias (list): Recibe la lista de los promedios de esas materias.
        indice (int): recibe el indice para entrar a cada dato de esas listas.
    Returns:
        None: No existe retorno -> muestra por pantalla cada dato que se pide anteriormente por parametro formal.
    """
    print(f"se repite: {lista_numeros_repetidos[indice]} la nota {indice+1}")


def mostrar_materias_y_notas_repetidas(
    materias: list, lista_numeros_repetidos: list, materia, tamano: int
) -> None:
    """
    Esta funcion Recibe los datos de los usuarios y los muestra 1 por 1 -> ordenados de Nombre, Edades, Genero, Legajo, Notas y promedio.
    Args:
        materias (list): Recibe la lista con las materias existentes.
        promedio (list): Recibe la lista con los promedios de cada materia existentes.
        promedio_maximo (int): Recibe cual es la mayor nota dentro de las materias existentes.
        tamanio (int): recibe la longitud de las listas para poder iterar de forma correcta en el bucle.
    Returns:
        None: No existe retorno -> muestra por pantalla el titulo de cada dato e itera por el tamaño de la lista y
        llama a mostrar_dato() para imprimirlos por pantalla. OBSERVACION -> (La función va a mostrar solamente la/s materia/s que tengan mejor promedio)
    """
    print(f"{materia}")
    for i in range(tamano):
        mostrar_materia_repetida(lista_numeros_repetidos, i)
