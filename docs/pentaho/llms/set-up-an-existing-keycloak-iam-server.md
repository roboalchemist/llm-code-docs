# Source: https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/setting-up-the-keycloak-iam-server/set-up-an-existing-keycloak-iam-server.md

# Set up an existing Keycloak IAM server

Set up an existing Keycloak IAM server to use with Pentaho Data Mastering if you do not want to install the default Keycloak IAM server.

Complete the following steps to configure the Docker container to use an existing Keycloak IAM server:

1. Open a file transfer tool, like the PuTTY client, and log into the server.
2. Run the following command with the environmental variables specified for the Keycloak server IP and Keycloak server secret:

   ```
   $ sudo truncate -s 0 /opt/mdm/conf/.keycloak.env > /dev/null

   $ echo "KEYCLOAK_REALM=mdm" |sudo tee -a /opt/mdm/conf/.keycloak.env> /dev/null
   $ echo "KEYCLOAK_ID=mdm" |sudo tee -a /opt/mdm/conf/.keycloak.env > /dev/null
   $ echo "KEYCLOAK_HOST=http://<Keycloak_server_ip>:8080   " |sudo tee -a /opt/mdm/conf/.keycloak.env > /dev/null
   $ echo "KEYCLOAK_SECRET= <Keycloak_server_secret> " |sudo tee -a /opt/mdm/conf/.keycloak.env > /dev/null
   ```

After you have set up the Keycloak IAM server, see [Installing the Pentaho Data Mastering server](https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/setting-up-the-keycloak-iam-server/broken-reference).
