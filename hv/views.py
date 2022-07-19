from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import HVSerializer
from . models import HV

@api_view(['GET', 'POST'])
def hv_lists(request):
    if request.method == 'GET':
        hv = HV.objects.all()
        serializer = HVSerializer(hv, many =True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HVSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)   
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        