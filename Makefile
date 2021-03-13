PORT ?= 8080

install:
	poetry install

app-dry:
	export DEBUG=true; poetry run python app.py

app:
	poetry run gunicorn app:server --bind="0.0.0.0:${PORT}"
