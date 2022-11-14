docker stop postgres-django
docker rm postgres-django
docker image rm -f postgres-django-img
docker image build -t postgres-django-img .