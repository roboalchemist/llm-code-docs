# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/using-the-dockmaker-command-line-tool-docker-deployment/docker-command-tool-property-and-registry-files-installation-article-cp/docker-command-tool-property-file-install/variable-resolution-order-docker-command-tool-properties.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/using-the-dockmaker-command-line-tool-docker-deployment/docker-command-tool-property-and-registry-files-installation-article-cp/docker-command-tool-property-file-install/variable-resolution-order-docker-command-tool-properties.md

# Variable resolution order

All variables in the file are resolved in the following specific order:

* Preset Variables based on command line entered.
* Derived Variables in the order they appear in the `DockMaker.properties` file. Derived Variables only have access to Preset Variables and any Derived Variables that appear earlier in the file.
* Mandatory variables and their dependencies just before applying that variable.

Other variables can be added as necessary to simplify the definition process. For example, `docker.download.host.prefix` was added to facilitate the hostname in the URLs.
