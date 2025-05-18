## Imports ##
from paquetes.funciones_propias import (
    busqueda_alumno,
    calcular_promedio_estudiantes,
    calcular_promedio_materias,
    calcular_promedio_maximo,
    cargar_lista_secuencial,
    cargar_matriz_secuencialmente,
    inicializar_matriz,
    materias_por_nombre,
    mostrar_dato,
    mostrar_datos,
    mostrar_materia,
    mostrar_materias,
    ordenar,
    to_lower,
)
from paquetes.validates import validate_number

# matrices y listas pedidas
"""
notas_estudiantes = inicializar_matriz(5, 5, 0)
nombres_estudiantes = [""] * 5
edades_estudiantes = [-1] * 5
generos_estudiantes = [""] * 5
legajos_estudiantes = [-1] * 5
"""
nombres_estudiantes = [
    "Valentina Díaz",
    "Carlos Fernández",
    "Ana Gómez",
    "Zoe Herrera",
    "Martín Ibáñez",
    "Lucía Romero",
    "Bruno Sosa",
    "Ximena López",
    "Diego Pérez",
    "Hernán García",
    "Sofía Martínez",
    "Julieta Navarro",
    "Florencia Ocampo",
    "Pedro Quintana",
    "Ricardo Torres",
    "Ismael Vera",
    "Gabriel Urrutia",
    "Nicolás Domínguez",
    "Tomás Estrada",
    "Ulises Franco",
    "Wanda Giménez",
    "Cintia Rivas",
    "Emilia Sánchez",
    "Yamila Bustos",
    "Benjamin Álvarez",
    "Ramiro Castillo",
    "Ángela Moreno",
    "Kiara Núñez",
    "Oscar Acosta",
    "Lautaro Benedetti",
]
edades_estudiantes = [
    19,
    21,
    18,
    24,
    20,
    22,
    23,
    19,
    25,
    18,
    21,
    20,
    23,
    19,
    24,
    22,
    18,
    20,
    21,
    23,
    17,
    24,
    19,
    22,
    20,
    18,
    21,
    23,
    17,
    25,
]
generos_estudiantes = [
    "F",
    "M",
    "F",
    "X",
    "F",
    "M",
    "F",
    "M",
    "F",
    "M",
    "X",
    "M",
    "F",
    "M",
    "X",
    "M",
    "F",
    "F",
    "F",
    "M",
    "F",
    "M",
    "X",
    "M",
    "F",
    "M",
    "F",
    "M",
    "F",
    "X",
]
notas_estudiantes = [
    [9, 5, 8, 6, 9],
    [9, 6, 5, 7, 8],
    [9, 9, 6, 5, 7],
    [9, 7, 8, 5, 9],
    [9, 6, 5, 8, 6],
    [9, 7, 6, 9, 7],
    [9, 6, 7, 5, 8],
    [6, 9, 7, 8, 6],
    [7, 5, 6, 9, 8],
    [5, 6, 8, 7, 9],
    [6, 5, 7, 8, 6],
    [9, 6, 8, 5, 7],
    [8, 7, 9, 6, 5],
    [7, 6, 8, 7, 6],
    [6, 5, 7, 8, 9],
    [8, 9, 6, 7, 5],
    [7, 8, 5, 6, 4],
    [6, 7, 9, 8, 5],
    [5, 6, 8, 7, 9],
    [9, 7, 6, 5, 8],
    [6, 8, 7, 9, 5],
    [5, 7, 6, 8, 4],
    [8, 6, 5, 9, 7],
    [6, 5, 8, 7, 9],
    [7, 8, 6, 5, 9],
    [9, 7, 5, 6, 1],
    [6, 8, 9, 7, 5],
    [5, 6, 8, 9, 7],
    [7, 9, 6, 5, 8],
    [8, 7, 5, 6, 9],
]
legajos_estudiantes = [
    100001,
    100002,
    100003,
    100004,
    100005,
    100006,
    100007,
    100008,
    100009,
    100010,
    100011,
    100012,
    100013,
    100014,
    100015,
    100016,
    100017,
    100018,
    100019,
    100020,
    100021,
    100022,
    100023,
    100024,
    100025,
    100026,
    100027,
    100028,
    100029,
    100030,
]


# Funcion principal
def main() -> None:
    """
    Esta funcion se encarga de la funcionalidad principal de la aplicación.
    Args:
        NO RECIBE PARAMETROS FORMALES.
    Returns:
        NO HAY RETORNO EXISTENTE. SOLO EJECUCIÓN.
    """
    promedio_estudiantes = [0] * len(nombres_estudiantes)
    promedio_materias = [-1] * len(notas_estudiantes[0])
    # Creamos un bucle para primeramente validar que se elija la opcion 1 para cargar los datos o 2 para salir. luego si se cargan correctamente los datos apareceran las demas opciones anidadas.
    print("BIENVENIDO A LA APP DE ESTUDIANTES!!!!")
    datos_cargados = False
    while True:
        # mensaje de bienvenida y muestra de las opciones disponibles
        print(
            "n1.Cargar datos alumnos\n2.Mostrar datos alumnos\n3.Calcular promedio alumnos\n4.Ordenar los promedios y datos de forma descendente\n5.Mostrar materias con mayor promedio general\n6.Buscar y mostrar todos los datos de un alumno\n7.salir del programa\n"
        )
        opciones = input("Elija una opción para continuar: ")
        validacion = validate_number(opciones)
        if validacion == True and opciones >= "1" and opciones <= "7":
            if datos_cargados == False and opciones != "1" and opciones != "7":
                print("\nDebes cargar los datos antes de ingresar a otra opcion!!")
                continue
            match opciones:
                case "1":
                    # cargar_matriz_secuencialmente(notas_estudiantes)
                    cargar_lista_secuencial(
                        nombres_estudiantes,
                        edades_estudiantes,
                        generos_estudiantes,
                        legajos_estudiantes,
                        len(nombres_estudiantes),
                    )
                    datos_cargados = True
                    print("Los datos fueron cargados exitosamente.")
                case "2":
                    mostrar_datos(
                        nombres_estudiantes,
                        edades_estudiantes,
                        generos_estudiantes,
                        legajos_estudiantes,
                        notas_estudiantes,
                        promedio_estudiantes,
                        len(nombres_estudiantes),
                    )
                case "3":
                    promedio_estudiantes_retorno = calcular_promedio_estudiantes(
                        notas_estudiantes,
                        len(notas_estudiantes[0]),
                        len(notas_estudiantes),
                    )
                    promedio_estudiantes = promedio_estudiantes_retorno
                case "4":
                    ordenar(
                        nombres_estudiantes,
                        edades_estudiantes,
                        generos_estudiantes,
                        legajos_estudiantes,
                        notas_estudiantes,
                        promedio_estudiantes,
                    )
                    print("Los elementos han sido ordenado existosamente!!!")
                case "5":
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
                case "6":
                    busqueda_alumno(
                        legajos_estudiantes,
                        nombres_estudiantes,
                        edades_estudiantes,
                        generos_estudiantes,
                        notas_estudiantes,
                        promedio_estudiantes,
                    )
                case "7":
                    break
        else:
            print(
                "LAS OPCIONES VALIDAS SON:\n1.Cargar datos alumnos\n2.Mostrar datos alumnos\n3.Calcular promedio alumnos\n4.Ordenar los promedios y datos de forma descendente\n5.Mostrar materias con mayor promedio general\n6.Buscar y mostrar todos los datos de un alumno\n7.salir del programa!!"
            )


main()  # -> EJECUCIÓN DEL PROGRAMA.
