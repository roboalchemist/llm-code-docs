# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/using-dockmaker-with-service-packs.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/using-dockmaker-with-service-packs.md

# Using DockMaker with service packs

The DockMaker command line tool does not support the service pack (SP) update installers. You must use the full SP artifacts. To use these artifacts, first download them directly from the `DockMaker Full Artifacts` directory within each service pack release article. Then, copy them to the `artifactCache` directory or to another directory as defined by the **docker.server.artifactCache** property in the `Dockmaker.properties` file. The following shows example artifact file downloads that are available for the v10.2 release:

Server:

* `pentaho-server-ee-10.2.0.0-<build number>.zip`
* `paz-plugin-ee-10.2.0.0-<build number>` if **paz** is in the command line
* `pdd-plugin-ee-10.2.0.0-<build number>` if **pdd** is in the command line
* `pir-plugin-ee-10.2.0.0-<build number>` if **pir** is in the command line
* Any `.kar` files that you have specified in the command line, for example, `pentaho-hadoop-shims-ee-cdpdc71-kar-10.2.0.0-<build number>`

PDI client, Carte:

* `pdi-ee-client-10.2.0.0-<build number>`
* Hadoop add-ons for Pentaho 9.5 or greater
* Any `.kar` files specified in the command line, for example, `pentaho-hadoop-shims-ee-cdpdc71-kar-10.2.0.0-<build number>`
