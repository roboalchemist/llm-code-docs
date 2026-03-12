# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/using-the-dockmaker-command-line-tool-docker-deployment/docker-command-tool-property-and-registry-files-installation-article-cp/docker-command-tool-property-file-install/preset-variables-docker-command-tool-properties.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/using-the-dockmaker-command-line-tool-docker-deployment/docker-command-tool-property-and-registry-files-installation-article-cp/docker-command-tool-property-file-install/preset-variables-docker-command-tool-properties.md

# Preset variables

A set of variables are automatically available and can be used within the properties file to create other variables. The following variables are preset:

* **`Version`**

  The version of the base server zip (`10.2.0.0` for example)
* **`distNumber`**

  The build number of base server zip (`343` for example)
* **`patchVersion`**

  The version of the patch file (`10.2.0` for example), if supplied
* **`patchDistNumber`**

  The build number of the patch file (`828` for example)
* **`edition`**

  EE
* **`pluginId`**

  Three character plugin ID (`paz`, `pdd`, `pir`, or `hdp` for example) being processed.
* **`karId`**

  The unique ID for a KAR file. (For example, the KAR file used on the command line)
* **`PORT`**

  The port number from the command line
* **`USER`**

  The user from the command line
* **`PASSWORD`**

  The password from the command line
