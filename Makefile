web := leaf-web-1

connect_web:
	docker exec -ti $(web) bash

tests:
	docker exec -ti $(web) sh -c "pytest matrix/tests.py"

init:
	docker-compose build && docker-compose up
