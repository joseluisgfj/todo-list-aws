# Comentario JLGF: Importación de las librerías necesarias en este .py
import json
import decimalencoder
import todoList

# Comentario JLGF: Definición de función 'list'
def list(event, context):
    # fetch all todos from the database
    result = todoList.get_items()
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result, cls=decimalencoder.DecimalEncoder)
    }
    # Comentario JLGF:json.dumps, Este método permite convertir un objeto python en un objeto JSON serializado.
    # Comentario JLGF: Se retorna una respuesta 200, y se completa el body con el listado de items
    return response
