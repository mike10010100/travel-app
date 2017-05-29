from .travel_app import app
from flask import request
from geopy.geocoders import Nominatim

@app.route('/')
def index():
	geolocator = Nominatim()
	location = geolocator.geocode(request.args.get('location1'))
	return location.address