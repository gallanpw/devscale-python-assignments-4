format:
	uv run ruff check --fix --unsafe-fixes

lint:
	uv run ruff check

dev:
	uv run uvicorn app.main:app --reload

celery:
	uv run celery -A app.celery_app worker --loglevel=info

redis-cli ping:
	docker exec -it redis-local redis-cli ping

redis-cli flushall:
	docker exec -it redis-local redis-cli flushall