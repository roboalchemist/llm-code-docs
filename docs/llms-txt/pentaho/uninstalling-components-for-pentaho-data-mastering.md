# Source: https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/uninstalling-components-for-pentaho-data-mastering.md

# Uninstalling components for Pentaho Data Mastering

Uninstall any of the following components by running a command and choosing the corresponding uninstall option: Pentaho Data Mastering components, the OpenObserve APM tool components, or the default Keycloak IAM server.

1. Open a file transfer tool, like the PuTTY client, and log into the server.
2. Run the following command to view the choices for installing, uninstalling, starting, and stopping tools on the Pentaho Data Mastering server:

   ```
   cd /opt/mdm/     
   ./mdm.sh
   ```
3. Enter the number that corresponds to the component that you want to uninstall.
4. Confirm that you want to proceed with the choice by typing `Yes` and pressing **Enter**.

   ![](https://728502995-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fice38OqJsmUCytyCg7bk%2Fuploads%2Fgit-blob-572491db2014af7df281ed3519bbe3019c021987%2Funinstall_mdm.png?alt=media)
5. Run the following command to verify that the components you uninstalled are no longer running in the Docker container:

   ```
   $ sudo docker ps
   ```
