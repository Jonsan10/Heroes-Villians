from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import HVSerializer
from . models import HV

@api_view(['GET', 'POST'])
def hv_lists(request):
    if request.method == 'GET':

        supers_name = request.query_params.get('super_type')
        print(supers_name)

        hv = HV.objects.all()
        if supers_name:
            hv = hv.filter(super_type=supers_name)


        serializer = HVSerializer(hv, many =True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HVSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)   
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT' 'DELETE'])
def hv_detail(request, pk):
    hv = get_object_or_404(HV, pk=pk)
    if request.method == 'GET':
        serializer = HVSerializer(hv);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = HVSerializer(hv, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        hv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

