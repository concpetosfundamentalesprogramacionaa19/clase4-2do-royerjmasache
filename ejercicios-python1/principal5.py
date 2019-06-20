"""
	@royerjmasache
"""
diccionario = {"nombre": "Royer", "apellido": "Masache"}
diccionario2 = {"nombre": "René", "apellido": "Elizalde"}
lista = [diccionario, diccionario2]
for l in lista:
	midiccionario = l
	print("Mi nombre es: %s y mi apellido es: %s" % (midiccionario["nombre"], midiccionario["apellido"]))
	