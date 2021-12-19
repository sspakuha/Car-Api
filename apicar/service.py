import requests
import json


def get_data(make, model):
	url = f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make.lower()}?format=json'
	r = requests.get(url)
	data = r.json()
	# Checks if response contains the string
	if data["Results"] == None:
		return False
	
	exists = False

	for i in range(len(data["Results"])):
		car = data["Results"][i];

		if car["Model_Name"].lower() == model.lower():
			exists = True;
			break
		
	return exists