.PHONY: migrate makemigrations test run clean

start:
	poetry run python manage.py runserver

test:
	poetry run pytest .
