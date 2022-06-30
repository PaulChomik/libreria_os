#https://docs.python.org/es/3/library/os.html#module-os
import os
os.mkdir('carpeta1')

'''
este codigo crea una carpeta.De existir la carpeta daria error
una forma de salvar el error es con el siguiente codigo:
'''
import errno
try:
    os.mkdir('carpeta2')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
'''
tambien podemos crear carpetas dentro de carpetas
'''
os.mkdir('carpeta1/carpeta1_1')
'''
esto puede dar error si es que la carpeta1 no existe
podemos arreglar esto con makedirs(),esta funcion crea todas las librerias
en la cadena si es que no existen y , si pasamos el parametro
exists=true, no crearà la carpeta en caso de existir
'''
os.makedirs('carpeta0/carpeta0_1/carpeta0_2',exist_ok=True)

'''
el comando open("ubicacion/archivo.extension","w")
crea un archivo y lo accede.
Este comando no da errores si el archivo ya existe, pero se debe
tener en cuenta que accede al archivo que ya existe y tiene el
mismo nombre
'''
file = open("/carpeta0/filename.txt", "w")
file.write("Primera línea \n")   #el \n solo indica que se finalizò la linea
file.write("Segunda línea")
file.close()
