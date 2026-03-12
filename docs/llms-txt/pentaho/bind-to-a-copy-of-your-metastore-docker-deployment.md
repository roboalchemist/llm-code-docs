# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/using-your-docker-containers-with-clusters-docker-deployment/shared-volumes-docker-deployment/metastore-volume-docker-deployment/bind-to-a-copy-of-your-metastore-docker-deployment.md

# Bind to a copy of your metastore

Because linking directly to your own metastore may break the container contract, you can copy your metastore and bind to that copy. Perform the following steps to bind to a copy of your metastore:

1. Create an arbitrary directory on your host file system to serve as the shared folder.

   For example, you can use `d:\metastore` on Windows.
2. Copy the `.kettle` and `.pentaho` directories from your home directory to shared folder, the `d:/metastore` directory for this example.
3. Copy any other files you need for processing your use case.

   In our example, the `d:/metastore` directory will then be bound to the `/home/pentaho` directory for the container.
4. Use the `DockMaker` command with `-M` parameter specified.

   For example, `-M d:/metastore`.
