from math import sqrt, trunc
from lista import Lista


class TablaHash:
    def __init__(self, tamanio):
        self.tamanio = self.menor_primo(tamanio)
        self.tabla = []
        for i in range(0, self.tamanio):
            self.tabla.append(Lista())

    def insertar(self, clave, valor):
        pass
        

    def eliminar(self, clave):
        pass

    def buscar(self, clave):
        pass

    def hash(self, clave):
        pass

    @staticmethod
    def menor_primo(self, tamanio):
        def es_primo(numero):
            if numero <= 1:
                b_es_primo = False
            elif numero == 2:
                b_es_primo = True
            elif numero % 2 == 0:
                b_es_primo = False
            else:
                b_es_primo = True

                limite = trunc(sqrt(numero))
                for cociente in range(3, limite + 1, 2):
                    if (numero % cociente == 0):
                        b_es_primo = False
            return b_es_primo
        
        while True:
            if es_primo(tamanio):
                return tamanio
            else:
                tamanio += 1

        