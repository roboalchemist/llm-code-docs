# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/using-your-docker-containers-with-clusters-docker-deployment/shared-volumes-docker-deployment/database-volume-docker-deployment.md

# Database volume

The database volume is only created when you start a Pentaho Server container. This volume contains all the database tables associated with the server repository, quartz scheduler, and log tables. When the database container is started for the first time, the container runs the DDL provided in `generatedFiles`, which then defines and populates the tables needed.
