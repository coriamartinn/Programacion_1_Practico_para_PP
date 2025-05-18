from paquetes.validates import validar_legajo_alumno, validate_cadena, validate_number


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


def cargar_lista_secuencial(
    nombres: list, edades: list, generos: list, legajos: list, tamano: int
) -> None:
    print(
        "Ingresaste al sistema para cargar Nombre, Edad, Genero y legajo del estudiante."
    )
    for i in range(tamano):
        while True:
            nombres[i] = input("Nombre y Apellido: ")
            validacion = validate_cadena(nombres[i])
            if validacion == True:
                break
            print("ERROR, no es un nombre válido!!")

        while True:
            edades[i] = input("Edad: ")
            validacion_edad = validate_number(edades[i])
            if validacion_edad == True and edades[i] > "17":
                edades[i] = int(edades[i])
                break
            print("ERROR, no es una edad valida!!")

        while True:
            generos[i] = input("Genero: ")
            generos[i] = to_upper(generos[i])
            if generos[i] == "F" or generos[i] == "M" or generos[i] == "X":
                break 
            print("ERROR, no es Genero valido!! (F=FEMENINO, M=MASCULINO, X=BINARIO)")

        while True:
            legajos[i] = input("Legajo: ")
            validacion_legajos = validate_number(legajos[i])
            if validacion_legajos == True:
                legajos[i] = int(legajos[i])
                if legajos[i] >= 1000 and legajos[i] <= 9999:
                    break
            print("ERROR, no es un legajo valido!!")


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
    lista_a: list,
    lista_b: list,
    lista_c: list,
    lista_d: list,
    lista_e: list,
    lista_f: list,
    primer_modo=1,
    segundo_modo=1,
) -> list:
    """
    Esta funcion recibe 3 listas y el modo de como ordenar las listas(1= ascendente, 2=descendente).
        lista_a (list): Recibe una lista por parametro.
        lista_b (list): Recibe una lista por parametro.
        lista_c (list): Recibe una lista por parametro.
        lista_d (list): Recibe una lista por parametro.
        lista_e (list): Recibe una lista por parametro.
        lista_f (list): Recibe una lista por parametro.
        modo (int): por defecto es 1 pero su valor puede cambiar -> (1=ASCENDENTE, 2=DESCENDENTE).
    Returns:
        list: Retorna la lista o listas ordenada de manera ascendente o descendente.
    """

    for i in range(0, len(lista_a) - 1, 1):

        for j in range(i + 1, len(lista_a), 1):

            if (lista_f[i] > lista_f[j] and primer_modo == 1) or (
                lista_f[i] < lista_f[j] and primer_modo == 2
            ):

                edad_auxiliar = lista_b[i]
                lista_b[i] = lista_b[j]
                lista_b[j] = edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = nombre_auxiliar

                genero_auxiliar = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = genero_auxiliar

                legajo_auxiliar = lista_d[i]
                lista_d[i] = lista_d[j]
                lista_d[j] = legajo_auxiliar

                notas_auxiliar = lista_e[i]
                lista_e[i] = lista_e[j]
                lista_e[j] = notas_auxiliar

                promedio_auxiliar = lista_f[i]
                lista_f[i] = lista_f[j]
                lista_f[j] = promedio_auxiliar
            # 2 criterio
            elif lista_f[i] == lista_f[j]:
                if (lista_a[i] > lista_a[j] and segundo_modo == 1) or (
                    lista_a[i] < lista_a[j] and segundo_modo == 2
                ):
                    edad_auxiliar = lista_b[i]
                    lista_b[i] = lista_b[j]
                    lista_b[j] = edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i] = lista_a[j]
                    lista_a[j] = nombre_auxiliar

                    genero_auxiliar = lista_c[i]
                    lista_c[i] = lista_c[j]
                    lista_c[j] = genero_auxiliar

                    legajo_auxiliar = lista_d[i]
                    lista_d[i] = lista_d[j]
                    lista_d[j] = legajo_auxiliar

                    notas_auxiliar = lista_e[i]
                    lista_e[i] = lista_e[j]
                    lista_e[j] = notas_auxiliar


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
            if i == 29:
                columna += 1
        promedio = f"Materia_{fila+1}"
        materias_mejor_promedio[fila] = promedio
        fila += 1
    return materias_mejor_promedio


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
    if promedio_materias == [0] * 30:
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
        if indice == None:
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
