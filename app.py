#Importamos lo que vamos a necesitar de flask
from flask import Flask, render_template, abort
# Importamos la libreria os del sistema para utilizar environ
import os 
# La aplicación nos va permitir mostrar la información del fichero books.json
# Por tanto, importamos json para leer el fichero 
import json 
# Leemos el fichero y lo añadimos a una variable 
with open ("books.json") as fichero:
    info = json.load(fichero)

# Definimos la ruta principal de la página de incio 

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html", lista_libros=info)







