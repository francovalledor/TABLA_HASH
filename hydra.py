from TDA_hash import TablaHash

diccionario = TablaHash()

def get_complemento(caracter):
    complemento = ord(caracter)
    complemento += 47 if ( ord(caracter) <= 78 ) else -47
    return chr(complemento)


def cifrar_caracter(caracter):
    salida = ''
    complemento = get_complemento(caracter)

    cuatro_digitos_str = str(ord(caracter) * 37)

    def convertir_digito(digito: str):
        digito = int(digito)
        convertido = digito * digito + ord(complemento)
        return chr(convertido)

    for digito in cuatro_digitos_str:
        salida += convertir_digito(digito)

    salida += complemento

    return salida


def descifrar_caracter(caracter_cifrado: str):
    descifrado = diccionario.obtener(caracter_cifrado)

    if not descifrado:
        for i in range(32, 126):
            c = chr(i)
            if cifrar_caracter(c) == caracter_cifrado:
                diccionario.insertar(caracter_cifrado, c)
                descifrado = c
                break
            
    return descifrado


def descifrar_texto(texto):
    texto_descifrado = ''
    
    while len(texto) >= 5:
        siguiente_caracter = texto[:5]
        texto = texto[5:]
        descifrado = descifrar_caracter(siguiente_caracter)
        if descifrado:
            texto_descifrado += descifrado

    return texto_descifrado


def descifrar_texto2(texto):

    for i in range(32, 126):
        c = chr(i)
        while cifrar_caracter(c) in texto:
            texto = texto.replace(cifrar_caracter(c), c)

    return texto


def leer_archivo(archivo, codificacion):

    with open(archivo, encoding=codificacion) as arch:
        contenido = arch.read()

    return contenido