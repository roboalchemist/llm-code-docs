# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/starting-or-stopping-your-docker-container-docker-deployment/starting-or-stopping-a-pentaho-server-container-docker-deployment.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/starting-or-stopping-your-docker-container-docker-deployment/starting-or-stopping-a-pentaho-server-container-docker-deployment.md

# Starting or stopping a Pentaho Server container

You start the Pentaho Server container when you specify the `-X` parameter to the `DockMaker` command. If you do not specify the `-X` parameter, the `generatedFiles` folder is created, but you must use the `docker build` and `docker compose` commands to generate the `docker-compose.yml` file. The `docker-compose.yml` file is a standard docker compose file that starts both thePentaho Server and repository database containers from their associated images. The data in the repository database is stored on a docker volume. You can sign into the server by entering `http://localhost:8081/pentaho/Login` into a browser. The default port number is 8081. You can change it with the `-p` parameter to the `DockMaker` command.

Once the Pentaho Server containers are built, use the `docker compose` command with the `up` parameter to start the containers, as shown in the following example:

`docker compose -f generatedFiles/docker-compose/yml up`

Use `docker compose` with the `stop` parameter to stop the containers, as shown in the following example:

`docker compose -f generatedFiles/docker-compose/yml stop`

Use `docker compose` with the `down` parameter to stop and delete the Pentaho Server container yet keep the database volume intact, as shown in the following example:

`docker compose -f generatedFiles/docker-compose/yml down`

Use `docker compose` with the `down` and `-v` parameters to stop and delete both Pentaho Server and repository database containers with all associated volumes, as shown in the following example:

`docker compose -f generatedFiles/docker-compose/yml down -v`

You can also use the `DockMakerDown.bat` (Windows) or `DockMakerDown.sh` (Linux) script files to stop and delete both Pentaho Server and repository database containers with all associated volumes.
