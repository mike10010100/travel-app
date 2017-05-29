STARTUP
###################

	virtualenv .venv -p python3 && source .venv/bin/activate

...or if you have zsh, virtualenvwrapper, and the associated zsh plugin, just cd out of and back into the folder. You'll automatically activate!

Then:

	pip3 install -e .

	export FLASK_APP=travel_app && export FLASK_DEBUG=true

	flask run --host=0.0.0.0