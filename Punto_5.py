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