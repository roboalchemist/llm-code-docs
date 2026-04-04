# Source: https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/installing-the-openobserve-apm-tool-components.md

# Installing the OpenObserve APM tool components

Install the OpenObserve Application Performance Monitoring (APM) tool components so that you can perform infrastructure monitoring and log search on the Pentaho Data Mastering.

**Important:** Components for Pentaho Data Mastering must be installed in the following order:

1. OpenObserver APM tool components
2. Keycloak IAM server components
3. Pentaho Data Mastering server components

If you have intalled a component out of order, uninstall that component and then install the components in order.

Complete the following steps to install and configure the OpenObserve APM tool to work with Pentaho Data Mastering:

1. Open a file transfer tool, like the PuTTY client, and log into the server.
2. Run the following command to view the choices for installing, uninstalling, starting, and stopping components on the Pentaho Data Mastering server:

   ```
   cd /opt/mdm/     
   ./mdm.sh

   ```

   For example, the following image shows the choices that are shown when you run the `mdm.sh` command:

   ![](https://728502995-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fice38OqJsmUCytyCg7bk%2Fuploads%2Fgit-blob-f22cefa2b88bded9652cd10423c6572a4e3aaf30%2Finstalling_openobserve_tool_components.png?alt=media)
3. Enter the number for the `Installing Open Observe` choice.
4. Confirm that you want to proceed with the choice by typing `Yes` and pressing `Enter`.
5. Run the following command to verify that the OpenObserve (APM) tool components are up and running in the Docker container:

   ```
   $ sudo docker ps
   ```

   For example, the following image shows the running status of the OpenObserve (APM) tool components:

   ![](https://728502995-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fice38OqJsmUCytyCg7bk%2Fuploads%2Fgit-blob-745422608cbefc47653688daf115dd0fb13f904d%2Fopenobserve_components_running.png?alt=media)

After you have installed the OpenObserve (APM) tool components, see [Setting up the Keycloak IAM server](https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/setting-up-the-keycloak-iam-server).
