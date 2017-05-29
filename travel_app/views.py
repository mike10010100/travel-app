from .travel_app import app

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/hello')
def hello():
	return 'Howdy there!'