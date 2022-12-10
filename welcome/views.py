from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def  welcome_instructors(request):
    return Response('Welcome to my Products Project for devCodeCamp!')


