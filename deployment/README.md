SUPERSET
========

Launching Superset 
------------------

To change database user/password, edit [.env](docker/.env) lines 22-23
and create file docker/pythonpath_dev/superset_config_local using
[superset_config_local.example](docker/pythonpath_dev/superset_config_local.example)
as an example. Additionally, edit lines 84-86 of
[docker-init.sh](docker/docker-init.sh).

To change Superset admin password edit line 40 of 
[docker-init.sh](docker/docker-init.sh). 
You will be able to create additional users via Superset UI.

      # export MAPBOX_API_KEY=SomeMapBoxApiKey
      cd deployment
      docker-compose pull
      docker-compose up    # interactively, to see log output
      # docker-compose up -d ## to start in background
      

Login to Superset UI as [http://localhost:8088](http://localhost:8088)

Exercise datasource will be using database `student`. To connect to it
from your host use parameters from lines 32-39 of 
[connection.py](../exercises/connection.py)

        "host": "localhost",
        "database": "student",
        "user": "student",
        "password": "secret2",
        "port": 8432
    

To connect to the database from Superset 
(which is running inside a docker container),
use:

        "host": "db",
        "database": "student",
        "user": "student",
        "password": "secret2",
        "port": 5432

The difference is in host and port. To use a different port 
on your localhost edit line 40 in
[](docker-compose.yml)

    ports:
      - 8432:5432
        
