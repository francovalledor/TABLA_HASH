from TDA_hash import TablaHash, TablaHashCerrada
from lista import Lista
# # EJ1
# diccionario = TablaHash(28)
# # 1.a
# diccionario['arroba'] = 'En las direcciones de e-mail, es el símbolo que separa el nombre del usuario del nombre de su proveedor de correo electrónico. Por ejemplo: pepe@hotmail.com'
# # 1.b
# try:
#     significado = diccionario.buscar('arroba')
#     print(significado)
# except KeyError:
#     print('La clave no existe')

# # 1.c
# del diccionario['arroba']

# # 1.d La tabla tiene de tamanio el numero primo mas cercano pero mayor a 28

# # EJ2
# class Telefono:
#     def __init__(self, telefono, apellido, nombre, direccion):
#         NUMEROS = '0123456789'
#         self.telefono = ''
#         for letra in telefono:
#             if letra in NUMEROS:
#                 self.telefono += letra

#         self.apellido = apellido
#         self.nombre = nombre
#         self.direccion = direccion

# telefonos = TablaHash(100)

# listado_telefonos = Lista()
# listado_telefonos.append(Telefono('(11) 4209-2111', 'VALLEDOR',  'ALBERTO', 'D Elia Cnel 2747 Pb Tp'))
# listado_telefonos.append(Telefono('(11) 4240-8045', 'VALLEDOR',  'ALBERTO', 'Yrigoyen Presidente Hipolito 5383 2 D'))
# listado_telefonos.append(Telefono('(11) 4642-3780', 'VALLEDOR',  'ALVAREZ EMILIO', 'Montiel Selva De 1297 Pa'))
# listado_telefonos.append(Telefono('(11) 4240-6496', 'VALLEDOR',  ' AMABLE C DE', 'Gardel Carlos 729 Pb Fdo'))
# listado_telefonos.append(Telefono('(11) 4568-8287', 'VALLEDOR',  'AMADOR', 'Navarro Julian 4832 1 C'))
# listado_telefonos.append(Telefono('(11) 4262-8453', 'VALLEDOR',  'ANGELICA V', 'Humberto Primo 3051 '))
# listado_telefonos.append(Telefono('(11) 4712-1531', 'VALLEDOR',  'AURORA N', 'Newton Isaac 1015'))
# listado_telefonos.append(Telefono('(11) 4441-7206', 'VALLEDOR',  'BEATRIZ', 'Cisneros 1394'))
# listado_telefonos.append(Telefono('(11) 4952-6564', 'VALLEDOR',  'CECILIA I', 'Junin Bat De 55 5 12'))
# listado_telefonos.append(Telefono('(11) 4253-6945', 'VALLEDOR',  'CLAUDIA P', 'Larrea 1852'))

# for num in listado_telefonos:
#     telefonos.insertar(num.telefono, num)


# # #EJ3
# class Materia:
#     def __init__(self, codigo: str, nombre: str, horas: int, anual: bool=False):
#         if type(codigo) not in (str, int):
#             raise TypeError('"codigo" debe ser un valor hasheable (int o str)')

#         if type(nombre) != str:
#             raise TypeError('"nombre" debe ser "str"')

#         if type(horas) != int:
#             raise TypeError('"horas" debe ser un valor entero "int"')

#         if type(anual) != bool:
#             raise TypeError('"anual" debe ser "bool"')

#         self.codigo = codigo.upper().strip()
#         self.nombre = nombre.upper().strip()
#         self.horas = horas
#         self.anual = anual
#         self.docentes = []

#     def __str__(self):
#         modalidad = 'anual' if self.anual else 'cuatrimestral'
#         texto = f"({self.codigo.upper()}) {self.nombre.title()}"
#         texto += f" - {modalidad.title()} - {self.horas} horas."
#         texto += f"\nDocentes:"
#         for docente in self.docentes:
#             texto += f"\n\t-{docente}"
#         return texto


# class Docente:
#     def __init__(self, nombre: str, DNI: str):
#         if (type(nombre) != str) or (type(DNI) != str):
#             raise TypeError('"nombre" y "DNI" deben ser "str"')
#         else:
#             for caracter in DNI:
#                 if caracter not in ('0123456789'):
#                     raise ValueError('Caracteres permitidos para "DNI": 0 1 2 3 4 5 6 7 8 9')
        
#         self.nombre = nombre.upper().strip()
#         self.DNI = DNI

#     def __repr__(self):
#         return f"Docente({self.nombre}, {self.DNI})"

#     def __str__(self):
#         return self.nombre.title()


# programacion = Materia('34102', 'fundamentos de programación', 10, True)
# lourdes = Docente('PRALONG', '32745379')
# rossana = Docente('ROSSANA SOSA ZITTO', '18786460')
# programacion.docentes.append(lourdes)
# programacion.docentes.append(rossana)

# syo = Materia('34101', 'Sistemas y Organizaciones', 10, True)
# claudia = Docente('Claudia Alvarez', '20369755')
# patricia = Docente('PATRICIA RAQUEL CRISTALDO', '24970060')
# syo.docentes.append(claudia)
# syo.docentes.append(patricia)

# computacion = Materia('34107', 'Fundamentos de Computación', 10)
# ben = Docente('BEN RAUL SAAD CORREA', '18741660')
# luis = Docente('LUIS RICARDO GRAZIANI', '14399984')
# computacion.docentes.append(ben)
# computacion.docentes.append(luis)


# materias = TablaHashCerrada(20)
# for materia in (programacion, syo, computacion):
#     materias[materia.codigo] = materia

# print(materias['34107'])


# #EJ4
# #Aclaración: el factor de carga para el rehashing es 0.8,
# #se podría cambiar modificando ese parámetro en el TDA

# from starwarsdata import personajes

# tabla = TablaHashCerrada(20)
# for i in range(0,11):
#     tabla.insertar(personajes[i].name.upper(), personajes[i])

# for clave, personaje in tabla.items():
#     print(f"key:'{clave}', nombre:'{personaje.name.title()}''")


# #EJ5
# class Contacto:
#     def __init__(self, nombre: str, apellido: str, correo: str):
#         for campo in (nombre, apellido, correo):
#             if type(campo) != str:
#                 raise TypeError('Los parametros "nombre", "apellido" y "correo" deben ser "str"')

#         self.nombre = nombre.strip().upper()
#         self.apellido = apellido.strip().upper()
#         self.correo = correo.strip()

#     def __str__(self):
#         return f"{self.nombre.title()} {self.apellido.title()} - {self.correo}"

# lista = []

# lista.append(Contacto('Hector Varela', 'Menéndez', 'oliverfelipe@exposito-aguila.com'))
# lista.append(Contacto('Pilar', 'Armas Luna', 'catalina41@yahoo.com'))
# lista.append(Contacto('Ismael', 'Falcón Pacheco', 'koller@haro.com'))
# lista.append(Contacto('Mónica Magdalena', 'Plana Pina', 'lourdesbarranco@hotmail.com'))
# lista.append(Contacto('Juan José', 'Pazos Oliver', 'palaciosbelen@hotmail.com'))
# lista.append(Contacto('Emilio', 'Rius Balaguer', 'fonsecafrancisco-javier@ferreras.org'))
# lista.append(Contacto('Martin', 'Blanca Antón', 'jorgefolch@diez.com'))
# lista.append(Contacto('Vicente', 'Villar Tomas', 'moralestrinidad@gmail.com'))
# lista.append(Contacto('Carlos', 'de Chaparro', 'nataliaalberdi@gmail.com'))
# lista.append(Contacto('Mario', 'de Company', 'benaventcarmen@hotmail.com'))
# lista.append(Contacto('Carmen', 'de Perez', 'joanhervas@gmail.com'))
# lista.append(Contacto('Juan Francisco', 'Camino Mir', 'mariaescobar@hotmail.com'))
# lista.append(Contacto('Manuela', 'Bas', 'ifarre@hotmail.com'))
# lista.append(Contacto('Miguel', 'Hernández Alfaro', 'wbermudez@real-pastor.com'))
# lista.append(Contacto('Sebastian', 'Castells-Pérez', 'cabanillasirene@tejera-fuente.biz'))
# lista.append(Contacto('Francisco Jose', 'Lillo Toro', 'sofia36@hotmail.com'))
# lista.append(Contacto('Lourdes', 'del Marquez', 'tllanos@gmail.com'))
# lista.append(Contacto('Emilio', 'Mayol Guillen', 'guitartconcepcion@pelaez.com'))
# lista.append(Contacto('Eduardo', 'del Hervás', 'cesarhuguet@lucas.com'))
# lista.append(Contacto('Anna', 'Duque Vilar', 'davidgiron@mayoral.com'))

# tabla = TablaHashCerrada()

# for persona in lista:
#     clave = f"{persona.nombre} {persona.apellido}"
#     tabla.insertar(clave, persona)

# print(tabla['Juan Francisco Camino Mir'.upper()])



# # EJ8
# from crypt import Crypt

# mensaje = "Este es un mensaje secreto."
# print('\n\nMENSAJE SIN ENCRIPTAR:')
# print(mensaje)

# # Creando una instancia
# cry = Crypt()
# mensaje_encriptado = cry.encriptar(mensaje)
# print('\n\nMENSAJE ENCRIPTADO:')
# print(mensaje_encriptado)

# print('\n\nMENSAJE DESENCRIPTADO:')
# print(cry.desencriptar(mensaje_encriptado))

# # Intentando desencriptar con otra instancia de Crypt
# print('\n\nIntentando desencriptar con otra instancia de Crypt:')
# cry2 = Crypt()
# try:
#     print(cry2.desencriptar(mensaje_encriptado)) #ValueError
# except ValueError:
#     print('No fue posible desencriptar el mensaje')

# # Compartiendo las claves
# claves = cry.compartir_claves()

# # Importando las claves
# cry2.importar(claves)

# # Intentando desencriptar con otra instancia de Crypt
# # Intento nro 2
# print('\n\nSegundo intento:')
# try:
#     print(cry2.desencriptar(mensaje_encriptado)) #Exito!
# except ValueError:
#     print('No fue posible desencriptar el mensaje')

