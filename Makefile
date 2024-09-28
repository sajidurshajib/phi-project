start:
	python institute/manage.py runserver
	
runserver:
	python institute/manage.py runserver

makemigrations:
	python institute/manage.py makemigrations

makemigrations:
	python institute/manage.py migrate

startapp:
	django-admin startapp $(appname) institute

removeapp:
	sudo rm -r institute/$(appname)