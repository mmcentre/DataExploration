SUPERSET
========

launching Superset with a new postgres instance
-----------------------------------------------

If postgres is not installed on your machine or if you would like 
to install a separate instance, follow the steps below:

1. Edit `./superset/postresql/init/db-init.sql` and `./superset/superset-config.py` (line 33, edit `SQLALCHEMY_DATABASE_URI` parameter) and supply the desired credentials for the DB user. Be default they are set to superset/superset. 

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

Launching Superset with an existing postgres DB
-----------------------------------------------
If you are on Mac or Windows, you have to follow the instructions for 
PostgreSQL running on a separate host.

If you are on Linux and PostgreSQL si already running on your machine,
follow these steps:

1. Create the DB and user for Superset on the existing DB server:

        CREATE DATABASE superset;
        CREATE USER superset WITH PASSWORD 'secret1';
        GRANT ALL PRIVILEGES ON DATABASE "superset" to superset;

2. Edit `./superset/superset-config.py` (line 33, edit `SQLALCHEMY_DATABASE_URI` parameter) and supply the desired credentials for the DB user.

3. Launch superset and dependencies, provide the Mapbox API Key value:

        # export MAPBOX_API_KEY=SomeMapBoxApiKey
        # docker-compose -f docker-compose-no-postgres-same-host.yml up -d

4. Initialize Superset, supply your username and password: 

        # docker-compose -f docker-compose-no-postgres-same-host.yml exec superset superset db upgrade
        # docker-compose -f docker-compose-no-postgres-same-host.yml exec superset \
            superset fab create-admin \
              --username admin \
              --firstname John \
              --lastname Doe \
              --email jdoe@example.com \
              --password password

        # docker-compose -f docker-compose-no-postgres-same-host.yml exec superset superset init

5. Login to Superset UI as http://localhost:8088

Launch Superset with an existing postgres DB running on a separate host
--------------------------------------------------------------------------
If you are on Mac, Windows or you PostgreSQL is running on a separate host,
follow the steps above, but use the docker-compose-no-postgres.yml instead:

1. Update Postgres configuration to accept connections from your host. 
   You might need to edit two files: pg_hba.conf and postgresql.conf. In 
   pg_hba.conf you might need to add a line:
   
         host    all             all             172.0.0.0/8             md5

   In postgresql.conf you might need to add a line like:

         listen_addresses = '*'		# what IP address(es) to listen on;

2. Edit line 31 of docker-compose-no-postgres.yml:
   
         POSTGRES_HOST: host.docker.internal

   The setting above works on Mac for PostgreSQL running on the host. 
   Change it to match your database server.

	# docker-compose -f docker-compose-no-postgres.yml up -d
