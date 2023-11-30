# running_text

Тестовое задание на стажировку в компании "АйТи-Солюшн"

## Запуск проекта

1. Собрать Docker-контейнер: \
```make build```
2. Применить миграции: \
```docker-compose run web poetry run python manage.py makemigrations``` \
```docker-compose run web poetry run python manage.py migrate```
3. Запустить Docker-контейнер: \
```make start```
4. Перейдите по URL:
http://127.0.0.1:8081/runtext?text=Пример , \
где вместо "Пример" впишите желаемое сообщение

### Запуск тестов:
```make test```