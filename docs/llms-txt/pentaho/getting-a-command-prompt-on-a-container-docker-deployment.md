# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/starting-or-stopping-your-docker-container-docker-deployment/getting-a-command-prompt-on-a-container-docker-deployment.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/starting-or-stopping-your-docker-container-docker-deployment/getting-a-command-prompt-on-a-container-docker-deployment.md

# Getting a command prompt on a container

On Linux, if you need a command prompt for a running container, such as a Pentaho Server or Carte container, you can use the `docker exec` command with the *containerID* listed via the `docker container ls` command, as shown in the following example:

`docker exec -it *containerId* bash`

To get into a stopped PDI container after a command has been executed, use the docker compose command with the bash argument, as shown in the following example:

`docker compose run pdi bash`

The `pdi` reference already is defined in your `docker-compose.yaml` file.
