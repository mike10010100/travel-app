from setuptools import setup
setup(
	name='travel_app',
	packages=['travel_app'],
	include_package_data=True,
	install_requires=[
	'flask',
	'zappa',
	'Flask-SQLAlchemy',
	'googlemaps',
	'psycopg2'
	],
)