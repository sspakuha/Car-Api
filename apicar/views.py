# views.py
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from .service import get_data
from .models import Car, Rating
from .serializers import CarSerializer, PopularSerializer


@api_view(['GET', 'POST'])
def cars(request):
	if request.method == 'GET':
		objects = Car.objects.all()
		serializer = CarSerializer(objects, many=True)
		return JsonResponse(serializer.data, safe=False)

	if request.method == 'POST':
		data = request.data

		if not 'make' in data or not 'model' in data or data['make'].strip() == "" or data['model'].strip() == "":
			return HttpResponse("POST Error. Wrong parameters. Try { 'make': '', 'model': '' } ")

		make = data['make'].capitalize()
		model = data['model'].capitalize()

		# CHECK, IF THE CAR IS ALREADY IN THE DATABASE
		if Car.objects.filter(make=make, model=model): 
			return HttpResponse("POST Error. Car already is in the database.")

		# GET REQUEST TO EXTERNAL API
		exists = get_data(make, model)

		if exists:
			obj = Car.objects.create(make=make, model=model)
			return HttpResponse('{"success": True}')
		else:
			return HttpResponse("Error. Car is not found in the external API database.")


@api_view(['DELETE'])
def delete(request, id):
	instance = Car.objects.filter(id=id)
	if instance:
		instance.delete()
		return HttpResponse('{"success": True}')
	else:
		return HttpResponse("Error. Car id is not found in the external API database.")


@api_view(['POST'])
def rate(request):
	data = request.data

	if not 'car_id' in data or not 'rating' in data or not type(data['rating']) in [int, float] or not type(data['car_id']) == int or data['rating'] > 5 or data['rating'] < 0:
		return HttpResponse("POST Error. Wrong parameters. Try { 'car_id': [], 'rating': [0.0-5.0] } ")
	
	car = Car.objects.filter(id=data['car_id'])

	if not car:
		return HttpResponse('POST Error. No car with id {}.'.format(data['car_id']))
	
	obj = Rating.objects.create(car_id=car[0], rate=data['rating'])

	return HttpResponse('{"success": True}')


@api_view(['GET'])
def popular(request):
	objects = Car.objects.all()
	serializer = PopularSerializer(objects, many=True)

	return JsonResponse(sorted(serializer.data, key=lambda i: i['rates_number'], reverse=True), safe=False)
	# return JsonResponse(serializer.data, safe=False)
