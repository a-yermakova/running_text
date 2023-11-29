.PHONY: migrate makemigrations test run clean

build:
	docker-compose build

start:
	docker-compose up

test:
	docker-compose run web poetry run pytest .
