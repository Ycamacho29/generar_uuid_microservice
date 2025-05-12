'''uuid_respuesta_entidad.py'''

from dataclasses import dataclass


@dataclass
class UUIDRepustaEntidad:
    '''Clase que Almacena los Datos de Salida para Enviar como respuesta del endpoing'''

    uuid: str
    version: str
