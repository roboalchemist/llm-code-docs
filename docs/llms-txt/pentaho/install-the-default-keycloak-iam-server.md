# Source: https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/setting-up-the-keycloak-iam-server/install-the-default-keycloak-iam-server.md

# Install the default Keycloak IAM server

Install the default Keycloak IAM server if you do not have an existing Keycloak IAM server that you want to use with Pentaho Data Mastering.

Complete the following steps to install the default Keycloak IAM server:

1. Open a file transfer tool, like the PuTTY client, and log into the server.
2. Run the following command to view the choices for installing, uninstalling, starting, and stopping components on the Pentaho Data Mastering server:

   ```
   cd /opt/mdm/     
   ./mdm.sh
   ```

   For example, the following image shows the choices that are shown when you run the `mdm.sh` command:

   ![](https://728502995-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fice38OqJsmUCytyCg7bk%2Fuploads%2Fgit-blob-eb376e06fb31cc0c688808cfc86b1884a949a0a3%2Fkeycloak_server_provided_by_hv.png?alt=media)
3. Enter the number for the `Installing keycloak` choice.
4. Confirm that you want to proceed with the choice by typing `Yes` and pressing `Enter`.
5. Run the following command to verify that the Keycloak IAM server log service is up and running in the Docker container:

   ```
   $ sudo docker logs -f mdm-keycloak
   ```

After you have set up the Keycloak IAM server, see [Installing the Pentaho Data Mastering server](https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/setting-up-the-keycloak-iam-server/broken-reference).
