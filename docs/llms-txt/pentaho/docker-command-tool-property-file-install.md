# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/using-the-dockmaker-command-line-tool-docker-deployment/docker-command-tool-property-and-registry-files-installation-article-cp/docker-command-tool-property-file-install.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/using-the-dockmaker-command-line-tool-docker-deployment/docker-command-tool-property-and-registry-files-installation-article-cp/docker-command-tool-property-file-install.md

# Docker command tool property file

The `DockMaker.properties` file contains configuration settings for the `DockMaker` command line tool, particularly the download and storage of artifacts.

The artifact cache directory is defined by the following code:

`docker.server.artifactCache=./artifactCache`

Although the default is to use the `artifactCache` directory in main directory for `DockMaker`, you can set cache to a secure location on your filesystem.

The rest of the file contains information on how to build a URL for the artifact to download. For example, the `docker.download.host.prefix` property defines the host URI of all Pentaho artifact downloads. The `docker.server.curlCommand` property defines the syntax for the `curl` command. For instance, you may want to change this property to a `wget` command per some installations.
