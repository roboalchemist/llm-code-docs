# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/before-you-begin-docker-deployment.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/before-you-begin-docker-deployment.md

# Before you begin

Before you start creating and deploying your Docker containers of Pentaho products, make sure you have the following items ready:

* Installation artifacts (ZIP files) of the Pentaho 10.2 products you are deploying through Docker containers. See [Pentaho installation](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp) for instructions about downloading installation artifacts of Pentaho products.
* An installed and stable Docker instance. This instance must have `docker-compose` installed to support the `docker-compose.yml`. If you are on a Windows operating system, you must have WSL2 installed and active.
* A user account with <https://hub.docker.com/>. The account login must be configured using the `docker login` command so that Docker can access registered database containers.
* The `curl` command line tool must be installed on the host operating system.
* To download Oracle databases, you must have login credentials to Oracle’s container repository.
* Java 8 or 11 must be installed on the host machine.

## Audience

IT administrators who know where the data is stored, how to connect to it, details about the computing environment, and how to use the command line to issue commands for Microsoft Windows or Linux.

## Login credentials

You must be logged on to an account that has privileges to perform the tasks in these sections. Additionally, Linux users must use `sudo` privileges or Docker roles for some tasks.
