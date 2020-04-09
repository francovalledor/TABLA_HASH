from TDA_hash import TablaHash

class Cifrar:
    num_a_cod = TablaHash(20)
    cod_a_num = TablaHash(20)

    num_a_cod.insertar('1', 'abd')
    num_a_cod.insertar('2', 'def')
    num_a_cod.insertar('3', 'ghi')
    num_a_cod.insertar('4', 'jkl')
    num_a_cod.insertar('5', 'mnñ')
    num_a_cod.insertar('6', 'opq')
    num_a_cod.insertar('7', 'rst')
    num_a_cod.insertar('8', 'uvw')
    num_a_cod.insertar('9', 'xyz')
    num_a_cod.insertar('0', '#?&')


    for num, cod in num_a_cod.items():
        cod_a_num.insertar(cod, num)

    @classmethod
    def cifrar(cls, texto):
        fin_de_caracter = '%'
        cifrado = ''
        for caracter in texto:
            representacion_numerica = str(ord(caracter))

            for num in representacion_numerica:
                cifrado += cls.num_a_cod.buscar(num)
            
            cifrado += fin_de_caracter

        return cifrado

    @classmethod
    def descifrar(cls, texto_cifrado):

        def descifrar_caracter(char_cifrado):
            numeros = ''
            cantidad = len(char_cifrado)//3

            for i in range(0,cantidad):
                siguientes3 = char_cifrado[0:3]
                char_cifrado = char_cifrado[3:]
                numeros += cls.cod_a_num.buscar(siguientes3)


            caracter = chr(int(numeros))
            return caracter
        
        caracteres_cifrados = texto_cifrado.split('%')[:-1]
        msj_descifrado = ''
        for char_cifrado in caracteres_cifrados:
            msj_descifrado += descifrar_caracter(char_cifrado)
        
        return msj_descifrado

