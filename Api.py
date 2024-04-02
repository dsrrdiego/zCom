import requests
import json
from clases import *
urlCrear = 'http://127.0.0.1:8000/ficha/crear/' 
urlObtener = 'http://127.0.0.1:8000/ficha/obtener/' 

def crearFicha(ficha):
    
    #data = {'numero': numero, 'color': color}
    data=json.dumps(ficha, default=ficha.serializar)
    #print (data)

    try:
        response = requests.post(urlCrear, data, headers={'Content-Type': 'application/json'})
        if response.status_code == 201:
            ficha_data = response.json()
            print("Ficha creada con éxito:", ficha_data)
        else:
            print("Error al crear la ficha:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)

def obtenerFicha():
    
    try:
        response = requests.get(urlObtener)
        if response.status_code == 200:
            fichas = response.json()
            return fichas
            #for ficha in fichas:
            #    print("ficha",ficha)

        else:
            print("Error al obtener la ficha:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)

if __name__ == "__main__":
    ficha=JugadorAzul(101,101,11,1,1,True,1,1,1,True,"Pepe1",1)
    ficha2=JugadorRojo(102,102,12,2,2,True,2,2,2,True,"Pepe2",2)
    crearFicha(ficha)
    crearFicha(ficha2)
    
    print (obtenerFicha())
