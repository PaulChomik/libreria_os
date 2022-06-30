import os

'''
en esta pagina hay un tutorial bastante completo de como funciona
la libreria os:
https://www.tutorialspoint.com/python/python_files_io.htm
'''
archivo=open("archiv.txt","w")
archivo.write("Primera línea \n")   #el \n solo indica que se finalizò la linea
archivo.write("Segunda línea")
archivo.close()

'''
buffer=espacio de memoria donde se almacenan datos
de manera temporal
la funcion open(nombre,modo_acceso,guardado_buffer)
tiene 3 parametros
nombre=contiene el nombre y la extension
modo_acceso=hay varios modos de acceso ,pero el por defectyo
es "r"(read)
      r=read,solamente leer      |rb=read binary leer el archivo en formato bianrio
      r+ lectura y escritura, el |rb+ leer y escribir en formato binario, el cursor
      cursor esta en la primer   |esta en el inicio del archivo
      linea o inicio del archivo |
      -----------------------------------------------------------------------------
      w=write solo escritura, si el archivo no existe crea uno nuevo
      wb=write binary escribir el archivo desde su formato binario
      w+ abrir el archivo par aleer y escribir
      a =append (anexar al final) abr euna rchivo para escribirlo, lo que
      se escriba sera anexado al final
      ab=append binary
      a+= es para anexar y leer simultaneamente

almacenamiento_buffering=si toma valor 0 no se esta usando meoria para almacenar temporal-
mente informacion de esa variable, valores mayores a 1 indican que esa memoria se destina
al almacenamiento de la variable o archivo,si es negativo se le asigna un almacenamiento
por defecto

------ATRIBUTOS DEL OBJETO file-----
Variada informacion se puede consultar mientras el archivo este abierto con open()
,pero si el archivo esta "cerrado"(close()) ese archivo no puede consultarse
archivo.open() abre el archivo
archivo.close() lo cierrra
archivo.mode() nose dice si el archivo esta abierto o cerrado
archivo.nombre() nos da el nombre del archivo
file.softspace()  nos da un "espacio explicito" requerido con impresion(no se que significa eso)
'''
archivo=open("archiv.txt","w")
print("nombre del archivo"+archivo.name)
print("el archivo está cerrado?=",archivo.closed)
print("modo de abertura:"+archivo.mode)
#print("softspace flag:",archivo.softspace) #da errores

archivo.close()
