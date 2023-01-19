# Comentario JLGF: Importación de las librerías necesarias
# en este caso solo es necesario todoList.py
# que contiene la funcion delete_item
import todoList

# Comentario JLGF: Definición de función delete


def delete(event, context):
    # Comentario JLGF: Se invoca a la funcion todoList.delete_item
    # definida en todoList.py, para borrar un item concreto
    todoList.delete_item(event['pathParameters']['id'])

    # create a response
    # Comentario JLGF: Se define la respuesta que será
    # devuelta a continuación con el return
    response = {
        "statusCode": 200
    }
    # Comentario JLGF: Se retorna una respuesta 200
    # que es equivalente a que el proceso a ido correctamente
    return response
