from rest_framework.response import Response
from rest_framework.decorators import api_view
from demo_app_version import custom_versions
from rest_framework.views import APIView

class DemoView(APIView):
  versioning_class = custom_versions.DemoViewVersion
  def get(self, request, *args, **kwargs):
    version = request.version
    return Response(data={'msg': f' You have hit {version}'})

class AnotherView(APIView):
  versioning_class = custom_versions.AnotherViewVersion
  def get(self, request, *args, **kwargs):
    version = request.version
    if version == 'v1':
      # perform v1 related tasks
      return Response(data={'msg': 'v1 logic'})
    elif version == 'v2':
      # perform v2 related tasks
      return Response(data={'msg': 'v2 logic'})

@api_view(['GET'])
def hello_world(request, *args, **kwargs):
  version = request.version
  return Response(data={
    'msg': f'You have hit {version} of demo-api'
  })

