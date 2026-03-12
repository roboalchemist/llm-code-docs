# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/using-the-dockmaker-command-line-tool-docker-deployment/docker-command-tool-property-and-registry-files-installation-article-cp/docker-command-tool-property-file-install/mandatory-variables-docker-command-tool-properties.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/using-the-dockmaker-command-line-tool-docker-deployment/docker-command-tool-property-and-registry-files-installation-article-cp/docker-command-tool-property-file-install/mandatory-variables-docker-command-tool-properties.md

# Mandatory variables

All other properties in the file are variables with a value. Some of these properties are required by the application to properly download artifacts.

The following variables are mandatory:

* **`docker.pdi.pdiArtifactFileName`**

  The file name associated with the PDI artifact
* **`docker.pdi.pdiArtifactUrl`**

  The complete URL used in the `curl` command to download the PDI artifact
* **`docker.server.serverArtifactFileName`**

  The file name associated with the Pentaho Server artifact
* **`docker.server.serverArtifactUrl`**

  The complete URL used in the `curl` command to download the Pentaho Server artifact
* **`docker.server.serverPluginFileName`**

  The file name associated with a `${pluginId}` (`paz`, `pad`, `pir`, and `hdp`)
* **`docker.server.serverPluginUrl`**

  The complete URL used in the `curl` command to download a `${pluginId}`
* **`docker.server.serverPatchFileName`**

  The file name associated with the patch artifact
* **`docker.server.serverPatchUrl`**

  The complete URL used in the `curl` command to download the patch
* **`docker.server.karFileName`**

  The file name associated with the a `${karId}`
* **`docker.server.karUrl`**

  The complete URL used in the `curl` command to download a KAR file
* **`docker.server.curlCommand`**

  The syntax of the `curl` command where `${url}` contains one of the URLs listed above, `${outputFolder}` contains the destination folder for the artifact, and `${filename}` contains the file name associated with the URL
