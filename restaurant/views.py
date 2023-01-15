from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Menu,Booking
from .serializer import MenuSeralizer,BookingSeralizer
from rest_framework import status 
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework.response import Response

def sayHello(request):
    return HttpResponse("hola mundo")

def home(request):
    return render(request,'home.html',{})

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    serializer_class = MenuSeralizer
    queryset = Menu.objects.all()
    
    def get(self,request):
        serializer_data = MenuSeralizer(data=self.get_queryset(),many=True)
        serializer_data.is_valid()
        return Response(serializer_data.data)

    def post(self,request):
        data = MenuSeralizer(data={**request.data})
        data.is_valid(raise_exception = True)
        data.save()
        return Response(data.data,status=status.HTTP_201_CREATED)


class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    serializer_class = MenuSeralizer
    queryset = Menu.objects.all()

    def get(self,request,pk):
        try:
            queryset = Menu.objects.filter(pk=pk)
            data_serialized = MenuSeralizer(data=queryset,many=True)
            data_serialized.is_valid()
            return Response(data_serialized.data[0])
        except:
            return Response({'message':'item not found'},status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request,pk):
        queryset = Menu.objects.filter(pk=pk).first()
        
        if not queryset:
            return Response({'message':'item not found'},status=status.HTTP_404_NOT_FOUND)

        data_serialized = MenuSeralizer(instance=queryset,data={**request.data})
        data_serialized.is_valid(raise_exception = True)
        data_serialized.save()
        return Response(data_serialized.data)
        
    def delete(self,request,pk):
        queryset = Menu.objects.filter(pk=pk).first()
        
        if not queryset:
            return Response({'message':'item not found'},status=status.HTTP_404_NOT_FOUND)
        
        queryset.delete()

        return Response({'message':'item deleted'})

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSeralizer
    permission_classes = [IsAuthenticated]
