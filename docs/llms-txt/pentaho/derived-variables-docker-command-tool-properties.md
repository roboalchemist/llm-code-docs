# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/using-the-dockmaker-command-line-tool-docker-deployment/docker-command-tool-property-and-registry-files-installation-article-cp/docker-command-tool-property-file-install/derived-variables-docker-command-tool-properties.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/docker-container-deployment-of-pentaho-installation-cp/docker-container-deployment-process-docker-deployment/using-the-dockmaker-command-line-tool-docker-deployment/docker-command-tool-property-and-registry-files-installation-article-cp/docker-command-tool-property-file-install/derived-variables-docker-command-tool-properties.md

# Derived variables

Derived variables have values based on a true or false condition. All properties names for these derived variables start with `docker.server.var` followed by a number to make each line unique, followed by the name of variable being set, followed by the value to set it to. The value of this property contains a JavaScript representation of the condition for setting this variable. All derived variables are usually supplied as the last section in the file but can appear anywhere.

Consider the following lines of code:

```
# set fileDistNumber to the distNumber, or blank if the distNumber="latest"
docker.server.var.0.fileDistNumber.="${distNumber}" === "latest" 
docker.server.var.1.fileDistNumber.-${distNumber}="${distNumber}" != "latest"

```

The first line is a comment describing the lines that follow. Second line sets a derived variable named `fileDistNumber` to an empty string, but only if `distNumber` equals `latest`. The third line sets the same `fileDistNumber` variable to `${distNumber}`, but only if the `distNumber` does not equal `lastest`.
