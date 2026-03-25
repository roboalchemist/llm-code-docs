# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/using-the-dockmaker-command-line-tool-docker-deployment/docker-command-tool-property-and-registry-files-installation-article-cp/docker-command-tool-registry-file-install.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/using-the-dockmaker-command-line-tool-docker-deployment/docker-command-tool-property-and-registry-files-installation-article-cp/docker-command-tool-registry-file-install.md

# Docker command tool registry file

The `containers/registry.yml` file contains information about what versions and combinations are supported by the command tool. The `databaseMap` section of the file defines what databases can be used to host the Pentaho Server repository database.

The following section of the file is an example of Postgres as the repository database:

```
postgres:
  databaseInstances:
    - versions: "9.6,13.5"
      edition:
      composeYml: docker-compose-postgres.yml
      dbInitFolder: db_init_postgres
      image: postgres:${DATABASE_VERSION}

```

Two versions of Postgres are supported, 9.6 or 13.5. The fully qualified database names available on the command line are `postgres/9.6` and `postgres/13.5`. The compose YML file that serves as a template for this configuration is `dock-compose-postgres.yml` and the directory containing the DDL to define the tables are in the `db_init_postgres` directory. The docker image that will be pulled down is defined in the `image` property and will be either `postgres:9.6` or `postgres:13.5`.

The `karFileRegistry` section of the registry file defines the various KAR files that can be installed. The `buildRegistry` section defines various fields that are conditional to the Pentaho version being chosen. Pentaho Server version 8.x supports `openjdk:8`, but Pentaho Server version 9.x supports `openjdk:8` or `openjdk:11`.
