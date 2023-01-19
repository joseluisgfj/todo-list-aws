# Comentario JLGF: Importación de las librerías necesarias en este .py
import json
import logging
import decimalencoder
import todoList

# Comentario JLGF: Definición de función 'update'
def update(event, context):
    data = json.loads(event['body'])
    # Comentario JLGF: Se realiza una comprobación
    # antes de actualizar la Base de Datos
    # si no se cumple no llega a actualizarse
    # generando una escritura en el log y una excepción en el programa
    if 'text' not in data or 'checked' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")
        # Comentario JLGF:No es necesario el return debido
        # a la excepción además no se estaba retornando nada
        return
    # update the todo in the database
    # Comentario JLGF: Si se pasa la comprobación previa
    # se invoca a la función todoList.update_item para actualizar la BBDD
    result = todoList.update_item(
        event['pathParameters']['id'],
        data['text'], data['checked'])
    # create a response
    # Comentario JLGF: Se genera la información que será retornada
    # por la función return a continuación
    response = {
        "statusCode": 200,
        "body": json.dumps(result, cls=decimalencoder.DecimalEncoder)
    }
    # Comentario JLGF: Se retorna una respuesta 200
    # y se completa el body con la información actualizada en la BBDD
    return response
