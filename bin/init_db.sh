docker cp ./init.sql postgres-docker:/
docker exec -it postgres-docker /bin/bash -c "psql -U docker -f ./init.sql"