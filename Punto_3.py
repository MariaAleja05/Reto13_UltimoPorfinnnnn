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