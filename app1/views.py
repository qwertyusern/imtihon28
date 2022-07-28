from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class Suvlar(ModelViewSet):
    queryset = Suv.objects.all()
    s=SuvSer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticatedOrReadOnly]
class Mijozlar(ModelViewSet):
    queryset = Mijoz.objects.all()
    s=MijozSer

class BuyurtmaApi(APIView):
    def get(self,request):
        b=Buyurtma.objects.all()
        s=BuyurtmaSer(b,many=True)
        return Response(s.data)
    def post(self, request):
        m = request.data
        s=BuyurtmaSer(data=m)
        if s.is_valid():
            s.save()
        return Response(s.data)

class HaydovchilarApi(APIView):
    def get(self,request):
        h=Haydovchi.objects.all()
        s=HaydovchiSer(h,many=True)
        return Response(s.data)

class HaydovchiApi(APIView):
    def get(self,request,pk):
        h=Haydovchi.objects.get(id=pk)
        s=HaydovchiSer(h)
        return Response(s.data)

class AdminlarApi(APIView):
    def get(self,request):
        a=Admin.objects.all()
        s=AdminSer(a,many=True)
        return Response(s.data)

class AdminApi(APIView):
    def get(self,request,pk):
        a=Admin.objects.get(id=pk)
        s=AdminSer(a)
        return Response(s.data)