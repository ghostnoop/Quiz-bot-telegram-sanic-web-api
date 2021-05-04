from sanic.response import json
from .services import service_back_call, service_after_quiz


def setup_routes(app):

    @app.post('/afterquiz')
    async def after_quiz_create(request):
        response = await service_after_quiz(request.json)
        if response is True:
            return json({'message': "OK"}, status=201)
        else:
            return json({'message': response}, status=400)

    @app.post('/backcall')
    async def back_call_create(request):
        response = await service_back_call(request.json)
        if response is True:
            return json({'message': "OK"}, status=201)
        else:
            return json({'message': response}, status=400)
