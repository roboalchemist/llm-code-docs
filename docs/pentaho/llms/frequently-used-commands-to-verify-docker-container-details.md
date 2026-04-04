# Source: https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/frequently-used-commands-to-verify-docker-container-details.md

# Frequently used commands to verify Docker container details

Use the following commands to verify the Docker container details:

| Command                              | Description                                                                                                                                            |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| $ sudo docker ps                     | Command to list all running containers on the Docker host.                                                                                             |
| $ sudo docker ps -a                  | Command to list all containers on the Docker host, regardless of their state, including running containers, stopped containers, and exited containers. |
| $ sudo docker logs -f \<containerID> | Command to stream the logs for the container with the specified ID.                                                                                    |
