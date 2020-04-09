from TDA import TablaHash

VALIDOS = "1234567890qwertyuiopasdfghjklñzxcvbnmQ"
OTROS="WERTYUIOPASDFGHJKLÑZXCVBNM-_!#$%&/()=?¡¿"


tabla = TablaHash()


for letra in VALIDOS:
    tabla.insertar(letra, ord(letra))

for letra in OTROS:
    tabla.insertar(letra, ord(letra))

print(f"len {len(VALIDOS)}")

for letra in VALIDOS:
    print(f"{letra}: {tabla.buscar(letra)}")
