# Comentario JLGF: Importación de las librerías necesarias en este py
import json
import logging
import todoList

# Comentario JLGF: Definición de función create


def create(event, context):
    # Comentario JLGF: Se obtiene el texto introducido en el programa
    data = json.loads(event['body'])
    # Comentario JLGF: Si no se introdujo texto en el programa
    # se escribe un error en el log y se lanza una excepción
    if 'text' not in data:
        # Comentario JLGF: Con la función logging.error
        # se escribe en el log un error
        logging.error("Validation failed")
        # Comentario JLGF:Se lanza una excepción con raise, y entre comillas
        # se escribe la Información de la excepción
        raise Exception("Couldn't create the todo item.")
    # Comentario JLGF: Si se introdujo información valida en el campo
    # se procede a intrucirla en el programa mediante
    # la funcion todoList.put_item
    item = todoList.put_item(data['text'])
    # create a response
    # Comentario JLGF: Se retorna una respuesta 200
    # que es equivalente a que el proceso a ido correctamente
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
        # Comentario JLGF:json.dumps, Este método permite convertir
        # un objeto python en un objeto JSON serializado
    }
    # Comentario JLGF: Se retorna una respuesta 200
    return response
