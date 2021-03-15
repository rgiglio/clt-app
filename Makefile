install:
	pip3 install -r requirements.txt

app-dry:
	export DEBUG=true; python3 app.py

app:
	gunicorn --workers 4 app:server