## Imports ##
from paquetes.funciones_generales import *
from paquetes.validates import validate_number
from paquetes.visualizacion import *
from paquetes.calculos import *
from paquetes.funciones_propias import busqueda_alumno


# Funcion principal
def main() -> None:
    """
    Esta funcion se encarga inicializar variables, listas o matrices, realizar el menu de opciones con su validación correspondiente 
    y el llamado a cada funcion para la ejecucion de cada caso del menu. 
    Args:
        NO RECIBE PARAMETROS FORMALES.
    Returns:
        None: NO HAY RETORNO EXISTENTE.
    """
    # matrices y listas pedidas -> ESTAS LISTAS SE INICIALIZAN PARA PROBAR LA CARGA DE DATOS. (El punto 1 del parcial)
    """
    notas_estudiantes = inicializar_matriz(5, 5, 0)
    nombres_estudiantes = [""] * 5
    edades_estudiantes = [-1] * 5
    generos_estudiantes = [""] * 5
    legajos_estudiantes = [-1] * 5
    """
    # VARIABLES, LISTAS
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
    promedio_estudiantes = [-1] * len(notas_estudiantes)
    # VARIABLES CON MENSAJES PARA MEJOR OPTIMIZACIÓN
    menu = "\n1.Cargar datos alumnos\n2.Mostrar datos alumnos\n3.Calcular promedio alumnos\n4.Ordenar los promedios y datos de forma descendente\n5.Mostrar materias con mayor promedio general\n6.Buscar y mostrar todos los datos de un alumno\n7.salir del programa"
    mensaje_de_despedida = "Decidiste salir del programa!!"
    mensaje_bienvenida = "BIENVENIDO A LA APP DE ALUMNOS!!"

    print(mensaje_bienvenida)
    datos_cargados = False
    while True:
        # mensaje de bienvenida y muestra de las opciones disponibles
        print(f"{menu}")
        opciones = input("Elija una opción para continuar: ")
        validacion = validate_number(opciones)
        if validacion == True:
            opciones = int(opciones)
            if opciones >= 1 and opciones <= 7:
                if datos_cargados == False and opciones != 1 and opciones != 7:
                    print("\nDebes cargar los datos antes de ingresar a otra opcion!!")
                    continue
            match opciones:
                case 1:
                    """carga_de_datos(
                        nombres_estudiantes,
                        edades_estudiantes,
                        generos_estudiantes,
                        legajos_estudiantes,
                        notas_estudiantes,
                    )"""
                    datos_cargados = True
                case 2:
                    mostrar_datos(
                        nombres_estudiantes,
                        edades_estudiantes,
                        generos_estudiantes,
                        legajos_estudiantes,
                        notas_estudiantes,
                        promedio_estudiantes,
                        len(nombres_estudiantes),
                    )
                case 3:
                    promedio_estudiantes = calculo_promedios(notas_estudiantes)
                case 4:
                    ordenar(
                        nombres_estudiantes,
                        edades_estudiantes,
                        generos_estudiantes,
                        legajos_estudiantes,
                        notas_estudiantes,
                        promedio_estudiantes,
                    )
                case 5:
                    mostrar_materias_con_mejor_promedio(notas_estudiantes)
                case 6:
                    busqueda_alumno(
                        legajos_estudiantes,
                        nombres_estudiantes,
                        edades_estudiantes,
                        generos_estudiantes,
                        notas_estudiantes,
                        promedio_estudiantes,
                    )
                case 7:
                    print(mensaje_de_despedida)
                    break
        else:
            print(f"ERROR, Ingrese una opción entre 1 y 7")


main()  # -> EJECUCIÓN DEL PROGRAMA.
