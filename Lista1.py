#lista es un tipo de datos abstracto mutable 

print("Ejemplo lista")
mi_lista=["Cadena de texto",15,2.8,"otro dato",25,25,25]

print("Datos lista :",mi_lista)

print("Imprimir : ",mi_lista[2])
print("Imprimir : ",mi_lista.count(25))
print("Imprimir : ",mi_lista.index(2.8))
mi_lista.append('Elemento ')

print("Datos Nueva lista :",mi_lista)
