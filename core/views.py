from django.shortcuts import render
from rest_framework import viewsets, filters
from .serializers import CarCategorySerializer, CarListSerializer
from .models import CarCategory, CarList
from django_filters.rest_framework import DjangoFilterBackend


def index(request):
    cars = CarList.objects.all()
    data = [{'name': car.name, 'image': car.image.url, 'description': car.description, 'category': car.carcategories.name} for car in cars]
    context = {'data': data}
    return render(request, "index.html", context)


class CarCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CarCategorySerializer
    queryset = CarCategory.objects.all()
    

class CarListViewSet(viewsets.ModelViewSet):
    serializer_class = CarListSerializer
    queryset = CarList.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["id","name","carcategories","description"]
    search_fields = ["name","carcategories__name"]
    ordering_fields = "__all__"
    
    
