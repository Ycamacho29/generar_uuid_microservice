'''generar_uuid_adaptador.py'''

from dataclasses import asdict
from generador_uuid_microservice_app.aplicacion.casos_de_uso.generar_uuid_impl import GenerarUUIDImpl


class GenerarUUIDAdaptador:
    '''Clase que convierte los Objetos de tipo UUIDRepustaEntidad
    a tipo Json'''

    @staticmethod
    def generar_uuid_v4() -> dict:
        '''Metodo que convierte un Objeto UUIDRepustaEntidad
        a tipo Json'''

        uuid_entidad = GenerarUUIDImpl.generar_uuid_v4()
        return asdict(uuid_entidad)
