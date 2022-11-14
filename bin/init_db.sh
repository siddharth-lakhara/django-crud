docker cp ./init.sql postgres-django:/
docker exec -it postgres-django /bin/bash -c "psql postgresql://django_user:django_user_pass@localhost:5432 -f ./init.sql"