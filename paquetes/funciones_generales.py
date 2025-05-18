from paquetes.calculos import (
    calcular_promedio_estudiantes,
    calcular_promedio_materias,
    calcular_promedio_maximo,
)
from paquetes.carga_datos import (
    cargar_lista_secuencial,
    cargar_matriz_secuencialmente,
    materias_por_nombre,
)
from paquetes.visualizacion import mostrar_materias


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
