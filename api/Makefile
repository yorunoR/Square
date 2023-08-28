test:
	poetry run python manage.py test

run:
	poetry run python manage.py runserver 3000

fmt:
	poetry run black . --preview

lint:
	poetry run ruff check .

lint-fix:
	poetry run ruff check . --fix

shell:
	poetry run python manage.py shell_plus

migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

superuser:
	poetry run python manage.py createsuperuser
