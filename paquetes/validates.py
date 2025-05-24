def validate_number(cadena: str) -> bool:
    """
    Recibe una cadena de numeros y verifica que sea un numero INT o FLOAT .
    -> Recibe una cadena tipo STR porque la validacion se lleva a cabo con la plantilla de codigo ASCI.
    ARGS:
    cadena (str): Cadena ingresada en el sistema,
    RETURNS:
       bool: Devuelve True si es valido, False si no es valido.
    """
    flag = True
    for caracter in cadena:
        if ord(caracter) < 48 or ord(caracter) > 57:
            flag = False
            break

    return flag


def validate_cadena(cadena: str) -> bool:
    """
    Esta funcion valida que una cadena de caracteres recibida por parametro tenga caracteres validos,
    -> un nombre no puede tener caracteres especiales como #@ o caracteres tipo INT.
    (en codigo ASCI seria: 65 a 90 (letras mayusculas) y 97 a 122 (letras minusculas))
    Args:
        cadena (str): Recibe una cadena de caracteres ingresada por el usuario.
    Returns:
        bool: Retorna True si la cadena ingresada tiene los caracteres permitidos,
        Retorna False si encuentra un caracter que no esta permitido dentro de la cadena.
    """

    validate_caracters = True
    cadena = cadena.lower()
    contador_espacios = 0
    for caracter in cadena:
        if ord(caracter) == 32:
            contador_espacios += 1
        if (
            (ord(caracter) < 97 or ord(caracter) > 122)
            and (ord(caracter) < 97 or ord(caracter) > 122)
            and contador_espacios != 1
        ):
            validate_caracters = False
            break

    return validate_caracters


def validar_legajo_alumno(legajos: list, legajo: int) -> int:
    """
    Esta funcion recibe la lista de legajos de los alumnos, y busca el legajo recibido por parametro.
    -> si existe tal LEGAJO guarda la posicion en la variable indice.
    Args:
        legajos (list): Recibe la lista de legajos.
        legajo (int): Recibe el legajo del alumno que quieren buscar.
    Returns:
        int: Retorna indice = None (VALOR POR DEFECTO) si el legajo es inexistente, Retorna indice = i -> posicion del legajo que existe.
    """

    indice = -1
    for i in range(len(legajos)):
        if legajos[i] == legajo:
            indice = i
            break
    return indice


def validar_materia_existente(materias: list, materia: int) -> int:
    """
    Esta funcion recibe la lista de legajos de los alumnos, y busca el legajo recibido por parametro.
    -> si existe tal LEGAJO guarda la posicion en la variable indice.
    Args:
        legajos (list): Recibe la lista de legajos.
        legajo (int): Recibe el legajo del alumno que quieren buscar.
    Returns:
        int: Retorna indice = None (VALOR POR DEFECTO) si el legajo es inexistente, Retorna indice = i -> posicion del legajo que existe.
    """

    indice = -1
    for i in range(len(materias)):
        if materias[i] == materia:
            indice = i
            break
    return indice
