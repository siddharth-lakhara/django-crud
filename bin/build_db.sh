docker stop postgres-docker
docker rm postgres-docker
docker image rm -f postgres-img
docker image build -t postgres-img .