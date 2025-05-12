'''generar_uuid_impl.py'''

import uuid

from generador_uuid_microservice_app.dominio.casos_de_uso.generar_uuid import GenerarUUID
from generador_uuid_microservice_app.dominio.entidades.uuid_respuesta_entidad import UUIDRepustaEntidad


class GenerarUUIDImpl(GenerarUUID):
    '''Implementacion de la Clase Abstracta GenerarUUID'''

    @classmethod
    def generar_uuid_v4(cls) -> UUIDRepustaEntidad:
        '''Metodo para Generar un UUID version 4'''
        valor_uuid = str(uuid.uuid4())
        return UUIDRepustaEntidad(valor_uuid, 'v4')
