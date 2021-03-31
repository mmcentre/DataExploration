SUPERSET
========

To launch Superset with a new postgres instance, follow the steps below.

1. Edit `./superset/postresql/init/db-init.sql` and `./superset/superset-config.py` (line 22, edit `SQLALCHEMY_DATABASE_URI` parameter) and supply the desired credentials for the DB user. Be default they are set to superset/superset. 

2. Launch superset and dependencies, provide the Mapbox API Key value:

        # export MAPBOX_API_KEY=SomeMapBoxApiKey
        # docker-compose up -d

3. Initialize Superset, supply your username and password:

        # docker-compose exec superset superset db upgrade
        # docker-compose exec superset \
            superset fab create-admin \
               --username admin \
               --firstname John \
               --lastname Doe \
               --email jdoe@example.com \
               --password password

        # docker-compose exec superset superset init

4. Login to Superset UI as [http://localhost:8088](http://localhost:8088)

To launch Superset with an existing postgres DB, follow the steps below:

1. Create the DB and user for Superset on the existing DB server:

        CREATE DATABASE superset;
        CREATE USER superset WITH PASSWORD 'superset';
        GRANT ALL PRIVILEGES ON DATABASE "superset" to superset;

2. Edit `./superset/superset-config.py` (line 22, edit `SQLALCHEMY_DATABASE_URI` parameter) and supply the desired credentials for the DB user.

3. Launch superset and dependencies, provide the Mapbox API Key value:

        # export MAPBOX_API_KEY=SomeMapBoxApiKey
        # docker-compose -f docker-compose-no-postgres.yml up -d

4. Initialize Superset, supply your username and password: 

        # docker-compose -f docker-compose-no-postgres.yml exec superset superset db upgrade
        # docker-compose -f docker-compose-no-postgres.yml exec superset \
            superset fab create-admin \
              --username admin \
              --firstname John \
              --lastname Doe \
              --email jdoe@example.com \
              --password password

        # docker-compose -f docker-compose-no-postgres.yml exec superset superset init

5. Login to Superset UI as http://localhost:8088

To launch Superset with an existing postgres DB, running locally on the same VM with Superset containers, follow the same steps, but use the docker-compose-no-postgres-same-host.yml instead:

	# docker-compose -f docker-compose-no-postgres-same-host.yml up -d
