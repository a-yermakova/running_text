# running_text

Тестовое задание на стажировку в компании "АйТи-Солюшн"

## Запуск проекта

1. Собрать и запустить Docker-контейнеры: \
```make build``` \
```make start```
2. Применить миграции: \
```docker-compose run web poetry run python manage.py makemigratioms``` \
```docker-compose run web poetry run python manage.py migrate```
3. Перейдите по URL:
http://127.0.0.1:8081/runtext?text=Пример , \
где вместо "Пример" впишите желаемое сообщение

### Запуск тестов:
```make test```