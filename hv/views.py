from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HVSerializer
from . models import HV

@api_view(['GET', 'POST'])
def hv_lists(request):
    # if request.method == 'GET':
        hv = HV.objects.all()
        serializer = HVSerializer(hv, many =True)
        return Response(serializer.data)