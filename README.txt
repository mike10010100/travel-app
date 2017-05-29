STARTUP
###################

virtualenv .venv -p python3

pip3 install -e .

export FLASK_APP=travel_app && export FLASK_DEBUG=true

flask run --host=0.0.0.0