
# tag with the latest build, use the appropriate dockerfile and start in right place
goose-counter-build:
	docker build \
		-t ehuan2/htngc-goose-counter:latest \
		-f ./src/goose-counter/Dockerfile-goose-counter \
	./src/goose-counter/

frontend-build:
	docker build \
		-t ehuan2/htngc-frontend:latest \
		-f ./src/frontend/Dockerfile-frontend \
	./src/frontend/

nickname-generator-build:
	docker build \
		-t ehuan2/htngc-nickname-generator:latest \
		-f ./src/nickname-generator/Dockerfile-nickname-generator \
	./src/nickname-generator/

build: goose-counter-build frontend-build nickname-generator-build

run:
	docker-compose up

push:
	docker push ehuan2/htngc-goose-counter:latest
	docker push ehuan2/htngc-frontend:latest
	docker push ehuan2/htngc-nickname-generator:latest