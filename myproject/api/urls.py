from home.views import RestaurantViewset
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'restaurant',RestaurantViewset,basename='restaurant')


urlpatterns = [
    path('', include(router.urls)),
]