.PHONY: help create update delete
.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

deploy: ## deploys the application
	gcloud app deploy

browse: ## open browser
	gcloud app browse

logs: ## show logs
	gcloud app logs tail -s default

describe: ## displays data about the app
	gcloud app describe

list: ## list app engine instances
	gcloud app instances list

build: ## build the docker container
	docker build -t actors-ws .

run: build ## run the webservice
	docker run -d -p 8080:8080 --name actors-ws actors-ws

kill: ## kill the webservice
	docker kill actors-ws

run-local: ## run the webservice locally
	pipenv run python main.py
