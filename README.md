# Reto número 13 repo
### Fecha:  17-11-2023
  
**1.** Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.
* No hay explicación porque fue voluntario :)
* Mirar archivo Reto_13.ipynb
```pseudocode
diccionario={"nombre": "María Alejandra", "carrera": "Ing Industrial", "mascota": "sí"}
valores=list(diccionario.values())
valores.sort()
print(valores)

diccionario2={"nombre": 5, "carrera": 1, "mascota": 3}
valores2=list(diccionario2.values())
valores2.sort()
print(valores2)
```

**2.** Desarrollar una función que reciba dos diccionarios como parámetros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.
* No hay explicación porque fue voluntario :)
* Mirar archivo Reto_13.ipynb
```pseudocode
diccionario1={"nombre": "María Alejandra", "carrera": "Ing Industrial", "mascota": "sí"}
diccionario2={"nombre": "Matías", "color": "Magenta", "comida": "pasta"}
dicc3={}

for key, valor in diccionario1.items():
  dicc3[key] = valor

for key, valor in diccionario2.items():
  if key not in dicc3:
    dicc3[key] = valor

print(dicc3)
```

**3.** Dado el JSON:
```pseudocode
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "D��az Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["F�utbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
```

Cree un programa que lea de un archivo con dicho JSON y: Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario, Imprima los nombres completos (nombre y apellidos) de las personas que estén en un rango de edades dado por el usuario.

* No hay explicación porque fue voluntario :)
* Mirar archivo Punto_3.py y Punto3_Reto13.json
  
```pseudocode
import json
#from pprint import pprint                                                                      # Opcional si se quiere imprimir el contenido del archivo json

def Deporte(data, deporte_u):                                                                   # Función para el deporte

    total_personas_deporte=[]                                                                   # Lista de personas que lo practican

    for key, valores in (data.items()):                                                         # Con tuplas se va mirando cada llave y su valor
            if deporte_u in valores["deportes"]:                                                # Se mira si el deporte está en la lista de deportes
                nombre=(str(valores["nombres"] + "  " + str(valores["apellidos"])))             # Se añade el valor de la key de nombre y apellido
                total_personas_deporte.append(nombre)                                           # Se añade el nombre completo a lista general
    print("Los que practican " + str(deporte_u) + " son: " + str(total_personas_deporte))       # Se imprimen los nombres

def Edad(data, edad_inicial, edad_final):                                                       # Función para la edad
   
    total_personas_edad=[]                                                                      # Lista de personas entran en el rango

    for key, valores in (data.items()):                                                         # Con tuplas se va mirando cada llave y su valor
        if valores["edad"]>edad_inicial and valores["edad"]<edad_final:                         # Se mira si la edad está dentro del rango 
            nombre=(str(valores["nombres"] + "  " + str(valores["apellidos"])))                 # Se añade el valor de la key de nombre y apellido
            total_personas_edad.append(nombre)                                                  # Se añade el nombre completo a lista general
    print("Las personas que están en el rango de edad entre " + str(edad_inicial) + " y " + str(edad_final) + " años, son: " + str(total_personas_edad))     

if __name__ == "__main__":

    with open("Punto3_Reto13.json", 'r') as file:                                               # Se abre al archivo tipo json 
        data = json.load(file)
    
    #pprint(data)                                                                               # Opcional para imprimir el contenido del archivo json
    
    deporte=str(input("Ingrese el deporte: "))                                                  # Ingresar el deporte
    deporte_u=deporte.capitalize()                                                              # Nos aseguramos de que esté la primera en mayuscula ya que así está en todo el archivo establecido

    Deporte(data, deporte_u)                                                                    # Se llama la función de deporte

    print("Ingrese el rango de edades")                                                         # Para ingresar el rango de edades                        
    edad_inicial=int(input())                           
    edad_final=int(input()) 
    
    Edad(data, edad_inicial, edad_final)                                                        # Se llama la función de edades
```

**4.** El siguiente código contiene un JSON con el pronostivo detallado del clima para 8 días:
```pseudocode
import json

# Cargar archivo
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
data = json.loads(jsonString)
```

Revise los campos: 'alertAlertas', 'alertPrecip', 'alertTmpMax', 'alertTmpMin', 'alertVelViento'. Para cada uno identifique si se presentan alertas ({0: x} indica que el día 0 habra un fenomeno de la alerta en cuestión, {1:"-"} indica que no habrá ningun fenomeno climatico). En caso que se presente una alerta obtenga la fecha del campo 'dt' (aquí pueden revisar como se convierte de UTC a fecha), así como los parametros relevantes del evento (e.g. si es un fenomeno de lluvias, busqye el nivel de lluvia, si es vientos, la velocidad del viuento). Al final deberá imprimir las fechas de alerta, el tipo de alerta y las variables asociadas.


* Explicación FALTA
* Mirar archivo Punto_4.py
```pseudocode
import json
#from pprint import pprint                                                                           # Por si quiere imprimirse el json                                                        
from datetime import datetime                                                                        # Para cambiar la fecha

def alertAlertas(data):                                                                              # Función para la primera alerta
     for key, valores in data["alertAlertas"].items():                                               # Toma los valores de ahí
        if valores == "X":                                                                           # Cuando si hay alerta para el fenómeno
            print("¡ALERTA POR ALERTAS!")
            print("Tipo de alerta: alertAlertas " + str(valores))                                    # Tipo de alerta

            for key_fecha, valores_fecha in data['dt'].items():                                      # Para mirar la fecha de la alerta
                if key_fecha==key:                                                                   # Cuando sea la misma llave para coincidir alerta con el día
                    fecha_rara=data['dt'].get(key)                                                   # Para extraer el valor de esa key
                    fecha_normal=datetime.utcfromtimestamp(fecha_rara).strftime('%Y-%m-%d %H:%M:%S') # Cambiar la fecha al estilo normal
                    print("Fecha de la alerta " + str(fecha_normal))

def alertPrecip(data):                                                                               # Los mismos comentarios que la primera función, lo único que cambia son las variables según el tipo de alerta        
     for key, valores in data["alertPrecip"].items():
        if valores == "X":                                                                          
            print("¡ALERTA POR PRECIPITACIONES!")
            print("Tipo de alerta: alertPrecip " + str(valores))

            for key_fecha, valores_fecha in data['dt'].items():
                if key_fecha==key:
                    fecha_rara=data['dt'].get(key)
                    fecha_normal=datetime.utcfromtimestamp(fecha_rara).strftime('%Y-%m-%d %H:%M:%S')
                    print("Fecha de la alerta " + str(fecha_normal))

            for key2, valores2 in data['description'].items():
                if key2==key:
                    nivel_lluvia=data['description'].get(key)
                    print("Hay " + str(nivel_lluvia))
            
            for key3, valores3 in data['dew_point'].items():
                if key3==key:
                    rocio=data['dew_point'].get(key)
                    print("El punto de rocío es:  " + str(rocio))

            for key4, valores4 in data['humidity'].items():
                if key4==key:
                    humedad=data['humidity'].get(key)
                    print("El nivel de humedad es:  " + str(humedad))

def alertTmpMax(data):                                                                               # Los mismos comentarios que la primera función, lo único que cambia son las variables según el tipo de alerta
     for key, valores in data["alertTmpMax"].items():
        if valores == "X":                                                                          
            print("¡ALERTA POR TEMPERATURA MÁXIMA!")
            print("Tipo de alerta: alertTmpMax " + str(valores))

            for key_fecha, valores_fecha in data['dt'].items():
                if key_fecha==key:
                    fecha_rara=data['dt'].get(key)
                    fecha_normal=datetime.utcfromtimestamp(fecha_rara).strftime('%Y-%m-%d %H:%M:%S')
                    print("Fecha de la alerta " + str(fecha_normal))

            for key2, valores2 in data['tmpMax'].items():
                if key2==key:
                    temp_max=data['tmpMax'].get(key)
                    print("La temperatura máxima es " + str(temp_max))
            
            for key3, valores3 in data['temp.day'].items():
                if key3==key:
                    temeratura_dia=data['temp.day'].get(key)
                    print("La temperatura durante el día es:  " + str(temeratura_dia))

            for key4, valores4 in data['temp.eve'].items():
                if key4==key:
                    temperatura_tarde=data['temp.eve'].get(key)
                    print("La temperatura durante la tarde es:  " + str(temperatura_tarde))
            
            for key5, valores5 in data['temp.morn'].items():
                if key5==key:
                    temperatura_mañana=data['temp.morn'].get(key)
                    print("La temperatura por la mañana es:  " + str(temperatura_mañana))
            
            for key6, valores6 in data['temp.night'].items():
                if key6==key:
                    temperatura_noche=data['temp.night'].get(key)
                    print("La temperatura por la noche es:  " + str(temperatura_noche))

def alertTmpMin(data):                                                                               # Los mismos comentarios que la primera función, lo único que cambia son las variables según el tipo de alerta
     for key, valores in data["alertTmpMin"].items():
        if valores == "X":                                                   
            print("¡ALERTA POR TEMPERATURA MINIMA!")
            print("Tipo de alerta: alertTmpMin " + str(valores))

            for key_fecha, valores_fecha in data['dt'].items():
                if key_fecha==key:
                    fecha_rara=data['dt'].get(key)
                    fecha_normal=datetime.utcfromtimestamp(fecha_rara).strftime('%Y-%m-%d %H:%M:%S')
                    print("Fecha de la alerta " + str(fecha_normal))

            for key2, valores2 in data['tmpMin'].items():
                if key2==key:
                    temp_min=data['tmpMin'].get(key)
                    print("La temperatura minima es " + str(temp_min))
            
            for key3, valores3 in data['temp.day'].items():
                if key3==key:
                    temeratura_dia=data['temp.day'].get(key)
                    print("La temperatura durante el día es:  " + str(temeratura_dia))

            for key4, valores4 in data['temp.eve'].items():
                if key4==key:
                    temperatura_tarde=data['temp.eve'].get(key)
                    print("La temperatura durante la tarde es:  " + str(temperatura_tarde))
            
            for key5, valores5 in data['temp.morn'].items():
                if key5==key:
                    temperatura_mañana=data['temp.morn'].get(key)
                    print("La temperatura por la mañana es:  " + str(temperatura_mañana))
            
            for key6, valores6 in data['temp.night'].items():
                if key6==key:
                    temperatura_noche=data['temp.night'].get(key)
                    print("La temperatura por la noche es:  " + str(temperatura_noche))

def alertVelViento(data):                                                                            # Los mismos comentarios que la primera función, lo único que cambia son las variables según el tipo de alerta
     for key, valores in data["alertVelViento"].items():
        if valores == "X":                                                                        
            print("¡ALERTA POR VELOCIDAD DEL VIENTO!")
            print("Tipo de alerta: alertVelViento " + str(valores))

            for key_fecha, valores_fecha in data['dt'].items():
                if key_fecha==key:
                    fecha_rara=data['dt'].get(key)
                    fecha_normal=datetime.utcfromtimestamp(fecha_rara).strftime('%Y-%m-%d %H:%M:%S')
                    print("Fecha de la alerta " + str(fecha_normal))

            for key2, valores2 in data['dirViento'].items():
                if key2==key:
                    dirr_viento=data['dirViento'].get(key)
                    print("La dirección del viento es " + str(dirr_viento))
            
            for key3, valores3 in data[ 'velViento'].items():
                if key3==key:
                    vel_viento=data[ 'velViento'].get(key)
                    print("La velocidad del viento es:  " + str(vel_viento))

if __name__ == "__main__":

    # Cargar archivo
    jsonString = '''
    {\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
    '''
    data = json.loads(jsonString)

    #pprint(data)

    alertAlertas(data)
    print("----------------------------------------------------------------")
    alertPrecip(data)
    print("----------------------------------------------------------------")
    alertTmpMax(data)
    print("----------------------------------------------------------------")
    alertTmpMin(data)
    print("----------------------------------------------------------------")
    alertVelViento(data)
```

**5.** A través de un programa conectese a al menos 3 API's , obtenga el JSON, imprimalo y extraiga los pares de llave : valor.
* Explicación FALTA
* Mirar archivo Reto_13.py
```pseudocode
import json
import requests

api1 = 'https://api.agify.io?name='                               # Predict the age of a person based on their name.
api2 = 'https://api.genderize.io?name='                           # Predict the gender of a person based on their name.
api3 = 'https://api.nationalize.io?name='                         # Predict the nationality of a person based on their name.

def EdadyNombre(nombre):
  print(api1)
  api_1 = requests.get(api1+str(nombre))
  print(api_1.status_code)

  return json.loads(api_1.content)

def GeneroyNombre(nombre):
  print(api2)
  api_2 = requests.get(api2+str(nombre))
  print(api_2.status_code)

  return json.loads(api_2.content)

def NacionalidadyNombre(nombre):
  print(api3)
  api_3 = requests.get(api3+str(nombre))
  print(api_3.status_code)

  return json.loads(api_3.content)

if __name__ == "__main__":

  nombre=str(input("Ingrese el nombre: "))   
  respuesta1 = EdadyNombre(nombre)
  respuesta2 = GeneroyNombre(nombre)
  respuesta3 = NacionalidadyNombre(nombre)

  unir_resultados_apis={}
  unir_resultados_apis.update(respuesta1)
  unir_resultados_apis.update(respuesta2)
  unir_resultados_apis.update(respuesta3)

  for key1, value1 in unir_resultados_apis.items():
    print(str(key1) + " --> " + str(value1))
```

