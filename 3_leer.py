import os

archivo=open("archivo.txt","w+")
archivo.write("hola esta es una linea \n y esta es otra linea \n")
print(archivo.read())

#consultar la posicion del cursor en el archivo
posicion=archivo.tell()
print("posicion:",posicion)
#posicionar el cursor al inicio del archivo
posicion=archivo.seek(0,0)
print("posicion:",posicion)

'''
RENOMBRAR:
para renombrar un archivo usamos el metodo
rename("nombreActual","nombreNuevo")
'''
os.rename("archivo.txt","pokemon.txt")

'''
BORRAR:
se puede borrar con el metodo os.remove("nombre")
'''
poke=open("pokemon2.txt","w")
os.remove("pokemon2.txt")
