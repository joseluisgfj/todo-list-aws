# Comentario JLGF: Importación de las librerías necesarias en este py
import json
import decimalencoder
import todoList

# Comentario JLGF: Definición de función get
def get(event, context):
    # create a response
    # Comentario JLGF: Se invoca a la funcion todoList.get_item
    # definida en todoList.py, para obtener un item concreto
    item = todoList.get_item(event['pathParameters']['id'])
    # Comentario JLGF: Si existe un item se define una respuesta correcta
    # statusCode 200, y se codifica dicho item en la variable body
    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item, cls=decimalencoder.DecimalEncoder)
            # Comentario JLGF:json.dumps, Este método permite convertir
            # un objeto python en un objeto JSON serializado.
        }
    # Comentario JLGF: Si no existe un item, se devuelve
    # un codigo de error 404, y la variable body se deja vacia
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    # Comentario JLGF: Se retorna la respuesta concreta
    # en función de la existencia de item
    return response
