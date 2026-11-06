pokemon = {"Nombre": "Pikachu", "Tipo":"Eléctrico", "Nivel": "25"}

if "Charmander" in pokemon.values():
    print ("El pokemon se encuentra entre los valores.")
else:
    print ("El pokemon no se encuentra entre los valores.")
if "Tipo" in pokemon:
    print("El pokemon es de tipo:", pokemon["Tipo"])
