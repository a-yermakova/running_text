.PHONY: migrate makemigrations test run clean

start:
	docker-compose up

test:
	docker-compose run --rm it_solution python manage.py pytest .
