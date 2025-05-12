'''routers.py'''

from ninja import NinjaAPI

from generador_uuid_microservice_app.infraestructura.adaptador.generar_uuid_adaptador import GenerarUUIDAdaptador

api = NinjaAPI()


@api.get("/generar_uuid_v4")
def generar_uuid_v4(request):
    '''Genera un UUID version 4'''
    return GenerarUUIDAdaptador.generar_uuid_v4()
