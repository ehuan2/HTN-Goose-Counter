
# tag with the latest build, use the appropriate dockerfile and start in right place
goose-counter-build:
	docker build \
		-t docker-workshop/goose-counter:latest \
		-f ./src/goose-counter/Dockerfile-goose-counter \
	./src/goose-counter/

frontend-build:
	docker build \
		-t docker-workshop/frontend:latest \
		-f ./src/frontend/Dockerfile-frontend \
	./src/frontend/

build: goose-counter-build frontend-build

run:
	docker-compose up