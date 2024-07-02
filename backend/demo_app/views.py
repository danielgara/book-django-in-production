from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_world(request, *args, **kwargs):
  return Response(data={'msg':'hello world'})
