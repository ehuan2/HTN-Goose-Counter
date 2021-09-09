
# tag with the latest build, use the appropriate dockerfile and start in right place

# ** general tagging guidelines **
# <external-repo>/<image-name>:<version-number>

goose-counter-build:
	# todo: add this in

frontend-build:
	docker build \
		-t ehuan2/htngc-frontend:latest \
		-f ./src/frontend/Dockerfile-frontend \
	./src/frontend/

nickname-generator-build:
	# todo: add this in

build: goose-counter-build frontend-build nickname-generator-build

run:
	# todo: add this in

push:
	docker push ehuan2/htngc-goose-counter:latest
	docker push ehuan2/htngc-frontend:latest
	docker push ehuan2/htngc-nickname-generator:latest