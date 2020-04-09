from random import choice
from TDA_hash import TablaHash

class Crypt:
    def __init__(self, longitud=8, caracteres_validos=None, inicio=32, fin=125):
        self.INICIO = inicio
        self.FIN = fin
        self.LONGITUD_CLAVE = longitud
        self.CANT_CLAVES = 1 + self.FIN - self.INICIO
        # Caracteres validos para generar claves
        self.VALIDOS = "1234567890qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM-_!#$%&/()=?¡¿"
        if caracteres_validos:
            self.VALIDOS = caracteres_validos
        
        claves = set()  # uso un conjunto para evitar repeticiones

        while not (len(claves) == self.CANT_CLAVES):
            claves.add(self._generar_clave())

        #Ahora que tengo la cantidad de claves que necesito 
        #creo 2 diccionarios inversos

        i = self.INICIO
        self._caracter_a_clave = TablaHash(self.CANT_CLAVES*2)
        self._clave_a_caracter = TablaHash(self.CANT_CLAVES*2)

        for clave in claves:
            self._caracter_a_clave.insertar(chr(i), clave)
            self._clave_a_caracter.insertar(clave, chr(i))
            i += 1

    def _generar_clave(self):
        """Devuelve una clave generada de forma aleatoria"""
        cadena = ""

        for i in range(0, self.LONGITUD_CLAVE):
            cadena += choice(self.VALIDOS)
        
        return cadena

    def encriptar(self, texto):
        """Encripta un texto"""
        encriptado = ""

        for caracter in texto:
            encriptado += self._caracter_a_clave.buscar(caracter)

        return encriptado

    def desencriptar(self, texto):
        """Desencripta un texto"""
        if len(texto) % self.LONGITUD_CLAVE != 0:
            raise ValueError('Cantidad de caracteres inválido')

        desencriptado = ""
        
        lista = []
        for caracter in texto:
            lista.append(caracter)

        while len(lista) >= self.LONGITUD_CLAVE:
            siguiente_clave = ""
            
            for i in range(0, self.LONGITUD_CLAVE):
                siguiente_clave += lista.pop(0)
            
            try:
                desencriptado += self._clave_a_caracter.buscar(siguiente_clave)
            except KeyError:
                raise ValueError('Imposible desencriptar ese mensaje')

        return desencriptado

    def compartir_claves(self):
        claves = []
        caracteres = []

        for clave, caracter in self._clave_a_caracter.items():
            claves.append(clave)
            caracteres.append(caracter)

        return [caracteres, claves]

    def importar(self, par):
        """
        Crea una instancia de la clase a partir de un par [caracteres, claves]
        """
        # ##VERIFICACIONES
        # Par debe ser una lista de tamaño 2
        if (type(par) != list) or (len(par) != 2):
            raise AttributeError('par debe ser [caracteres, claves]')

        # Ambas listas deben tener el mismo tamaño
        if len(par[0]) != len(par[1]):
            raise AttributeError('Las listas deben tener el mismo tamaño')
        
        caracteres = par[0]
        claves = par[1]

        # La longitud de cada clave debe ser la misma
        longitud = len(claves[0])

        for clave in claves:
            if len(clave) != longitud:
                raise AttributeError('Los tamaños de las claves difieren')

        # caracteres: todos deben ser de tipo str
        for caracter in caracteres:
            if type(caracter) != str:
                raise AttributeError('Caracteres deben ser "str"')

        self.LONGITUD_CLAVE = len(claves[0])
        self.CANT_CLAVES = len(claves)

        self._caracter_a_clave = TablaHash(self.CANT_CLAVES*2)
        self._clave_a_caracter = TablaHash(self.CANT_CLAVES*2)

        for i in range(0, self.CANT_CLAVES):
            self._caracter_a_clave.insertar(caracteres[i], claves[i])
            self._clave_a_caracter.insertar(claves[i], caracteres[i])
            i += 1