# local developemnt
build:
	cd server && docker-compose build
start:
	cd server && docker-compose up -d
stop:
	cd server && docker-compose down
