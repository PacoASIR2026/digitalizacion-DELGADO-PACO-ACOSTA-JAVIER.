"""
Crea un diccionario pokemon que contenga como claves: nombre, tipo y niviel con
valores Pikachu, Eléctrico y 25. Luego comprueba si Charmander se encuentra entre sus valores.
Comprueba si hay uncampo llamado tipo y si es así muestra su valor.
"""

pokemon = {"Nombre": "Pikachu", "Tipo":"Eléctrico", "Nivel": "25"}

if "Charmander" in pokemon.values():
    print ("El pokemon se encuentra entre los valores.")
else:
    print ("El pokemon no se encuentra entre los valores.")
if "Tipo" in pokemon:
    print("El pokemon es de tipo:", pokemon["Tipo"])
