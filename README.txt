STARTUP
###################

virtualenv .venv -p `which python3`

pip3 install -r requirements.txt OR pip3 install -e

export FLASK_APP=travel_app && export FLASK_DEBUG=true

flask run --host=0.0.0.0