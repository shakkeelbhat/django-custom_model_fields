from rest_framework import viewsets
from home.serializer import RestaurantSerializer
from home.models import Restaurant
# Create your views here.
class RestaurantViewset(viewsets.ModelViewSet):
	
	serializer_class = RestaurantSerializer
	queryset = Restaurant.objects.all()
