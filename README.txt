STARTUP
###################

virtualenv .venv -p `which python3`

pip3 install -r requirements.txt

export FLASK_APP=webserver.py

flask run --host=0.0.0.0