import json
#from pprint import pprint

def Deporte(data, deporte_u):

    total_personas_deporte=[]

    for key, valores in (data.items()):
            if deporte_u in valores["deportes"]:
                nombre=(str(valores["nombres"] + "  " + str(valores["apellidos"])))
                total_personas_deporte.append(nombre)
    print("Los que practican " + str(deporte_u) + " son: " + str(total_personas_deporte))

def Edad(data, edad_inicial, edad_final):
   
    total_personas_edad=[]

    for key, valores in (data.items()):
        if valores["edad"]>edad_inicial and valores["edad"]<edad_final:
            nombre=(str(valores["nombres"] + "  " + str(valores["apellidos"])))
            total_personas_edad.append(nombre)
    print("Las personas que están en el rango de edad entre " + str(edad_inicial) + " y " + str(edad_final) + " años, son: " + str(total_personas_edad))     

if __name__ == "__main__":

    with open("Punto3_Reto13.json", 'r') as file:
        data = json.load(file)
    
    #pprint(data)
    
    deporte=str(input("Ingrese el deporte: "))   
    deporte_u=deporte.capitalize() 

    Deporte(data, deporte_u)

    print("Ingrese el rango de edades")
    edad_inicial=int(input())   
    edad_final=int(input()) 
    
    Edad(data, edad_inicial, edad_final)