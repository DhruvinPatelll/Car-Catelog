from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CarCategoryViewSet, CarListViewSet
from . import views


urlpatterns = [
    path("", views.index, name="index" ),
]

router = DefaultRouter()
router.register("api/carcategories", views.CarCategoryViewSet, basename="carcategories")
router.register("api/car-list", views.CarListViewSet, basename="car_list")

urlpatterns += router.urls