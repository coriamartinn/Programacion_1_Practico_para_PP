from paquetes.calculos import (
    calcular_notas_repetidas,
    calcular_promedio_estudiantes,
    calcular_promedio_materias,
    calcular_promedio_maximo,
    ordenar,
)
from paquetes.carga_datos import (
    cargar_lista_secuencial,
    cargar_matriz_secuencialmente,
    materias_por_nombre,
)
from paquetes.funciones_propias import to_lower
from paquetes.validates import validar_legajo_alumno, validar_materia_existente
from paquetes.visualizacion import (
    mostrar_dato,
    mostrar_materias,
    mostrar_materias_y_notas_repetidas
)


def mostrar_materias_con_mejor_promedio(notas_estudiantes: list) -> None:
    """
    Esta funcion se encarga de encapsular toda la logica para obtener la o las materias con mejor promedio.
    Args:
        notas_estudiantes: Recibe las notas de los estudiantes.
    Returns:
        None: No existe ningun retorno.
    """
    materias = materias_por_nombre(notas_estudiantes)
    promedio_materias = calcular_promedio_materias(
        notas_estudiantes, len(notas_estudiantes)
    )
    promedio_maximo = calcular_promedio_maximo(promedio_materias)
    mostrar_materias(
        materias,
        promedio_materias,
        promedio_maximo,
        len(notas_estudiantes[0]),
    )


def carga_de_datos(
    nombres_estudiantes: list,
    edades_estudiantes: list,
    generos_estudiantes: list,
    legajos_estudiantes: list,
    notas_estudiantes: list,
) -> None:
    """
    Esta funcion se encarga de encapsular toda la logica para realizar la carga de los datos de cada alumno secuencialmente.
    Args:
        notas_estudiantes: Recibe las notas de los estudiantes.
    Returns:
        None: No existe ningun retorno.
    """

    cargar_matriz_secuencialmente(notas_estudiantes)
    cargar_lista_secuencial(
        nombres_estudiantes,
        edades_estudiantes,
        generos_estudiantes,
        legajos_estudiantes,
        len(nombres_estudiantes),
    )
    print("Los datos fueron cargados exitosamente.")


def calculo_promedios(notas_estudiantes: list) -> list:
    """
    Esta funcion se encarga de mantener la logica de los promedios encapsulado y tener mejor order en el programa.
    Args:
        notas_estdiantes (list): Recibe las notas de los estudiantes.
    Returns:
        list: Retorna la lista con los promedios de cada estudiante.
    """
    promedio_estudiantes_retorno = calcular_promedio_estudiantes(
        notas_estudiantes,
        len(notas_estudiantes[0]),
        len(notas_estudiantes),
    )
    return promedio_estudiantes_retorno


def ordenamiento(
    nombres_estudiantes: list,
    edades_estudiantes: list,
    generos_estudiantes: list,
    legajos_estudiantes: list,
    notas_estudiantes: list,
    promedio_estudiantes: list,
):
    """
    Funcion general para mantener una unica logica en el case 4
    Args:
    Returns:
    """
    if -1 in promedio_estudiantes:
        print("No se puede ordenar porque aun no existen los promedios.")
    else:
        ordenar(
            nombres_estudiantes,
            edades_estudiantes,
            generos_estudiantes,
            legajos_estudiantes,
            notas_estudiantes,
            promedio_estudiantes,
        )


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


def buscar_y_mostrar_notas_repetidas(notas_estudiantes: list) -> None:
    """
    Esta funcion se encarga de matener ordenado los llamados de las funciones necesarias
    """
    lista_notas_repetidas = calcular_notas_repetidas(notas_estudiantes)
    print(lista_notas_repetidas)
    materias = materias_por_nombre(notas_estudiantes)
    print(materias)
    while True:
            materia = input("Ingrese la materia que quiere encontrar (materia_1, materia_2, materia_3, materia_4, materia_5): ")
            indice = validar_materia_existente(materias, materia)
            if indice == -1:
                print("ERROR, La materia que intentas buscar no existe.")
            else:
                mostrar_materias_y_notas_repetidas(materias, lista_notas_repetidas, materia, len(lista_notas_repetidas))
            continuar = input("Desea continuar?: s/n: ")
            continuar = to_lower(continuar)
            if continuar == "n":
                break
