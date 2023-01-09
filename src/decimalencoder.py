# Comentario JLGF: Importación de las librerías necesarias en este .py
import decimal
import json


# This is a workaround for: http://bugs.python.org/issue16535
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):             #pylint: disable=E0202
                                        #pylint: enable=E0202
        if isinstance(obj, decimal.Decimal):
            # Comentario JLGF: Retorna int(obj) si se cumple la condición
            return int(obj)
        # Comentario JLGF: En caso contrario se retorna por defecto super(DecimalEncoder, self).default(obj)
        return super(DecimalEncoder, self).default(obj)
