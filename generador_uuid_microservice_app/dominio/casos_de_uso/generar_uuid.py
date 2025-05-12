'''generar_uuid.py'''

from abc import ABC, abstractmethod


class GenerarUUID(ABC):
    '''Clase Abstracta que define que metodos hay que implementar para
    generar los uuid'''

    @classmethod
    @abstractmethod
    def generar_uuid_v1(cls):
        '''Metodo para Generar un UUID version 1'''

    @classmethod
    @abstractmethod
    def generar_uuid_v3(cls):
        '''Metodo para Generar un UUID version 3'''

    @classmethod
    @abstractmethod
    def generar_uuid_v4(cls):
        '''Metodo para Generar un UUID version 4'''

    @classmethod
    @abstractmethod
    def generar_uuid_v5(cls):
        '''Metodo para Generar un UUID version 5'''
