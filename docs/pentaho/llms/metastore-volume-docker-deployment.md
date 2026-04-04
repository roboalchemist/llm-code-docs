# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/using-your-docker-containers-with-clusters-docker-deployment/shared-volumes-docker-deployment/metastore-volume-docker-deployment.md

# Metastore volume

You generate this volume by specifying the `-M` or `–metastore` parameter when using the `DockMaker` command. Specifying the parameter helps to create a bi-directional bind on a `metastore` directory. It binds the directory defined by the parameter with the `/home/pentaho` directory on the container.
