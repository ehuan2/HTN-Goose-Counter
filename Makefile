
# tag with the latest build, use the appropriate dockerfile and start in right place
goose-counter-build:
	docker build \
		-t docker-workshop/goose-counter:latest \
		-f ./src/goose-counter/Dockerfile-goose-counter \
	./src/goose-counter/

run:
	docker-compose up