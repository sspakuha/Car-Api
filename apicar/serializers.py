from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Car, Rating

from django.db.models import Avg


class RatingSerializer(ModelSerializer):

	avg_rate = SerializerMethodField()

	class Meta:

		model = Rating
		fields = ["rate"]
	

class CarSerializer(ModelSerializer):
	avg_rating = SerializerMethodField()

	class Meta:

		model = Car
		fields = ['id', 'make', 'model', 'avg_rating']
	
	def get_avg_rating (self, obj):		
		obj.avg_rating = Rating.objects.filter(car_id=obj.id).aggregate(Avg('rate'))

		if not obj.avg_rating["rate__avg"] == None:
			return obj.avg_rating["rate__avg"]
		else:
			return 0


class PopularSerializer(ModelSerializer):
	rates_number = SerializerMethodField()

	class Meta:
		model = Car
		fields = ['id', 'make', 'model', 'rates_number']
		# ordering = [-1]
	
	def get_rates_number (self, obj):
		obj.rates_number = Rating.objects.filter(car_id=obj.id).count()
		return obj.rates_number