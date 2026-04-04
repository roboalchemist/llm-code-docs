# Source: https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/setting-environmental-variables/setting-environmental-variables-for-online-installation.md

# Setting environmental variables for online installation

If you are installing Pentaho Data Mastering while connected to the internet, you must set environmental variables in the Docker container for the installation image files that are located on the JFrog Artifactory repository.

Complete the following steps to set the environmental variables for online installation:

1. Open a file transfer tool, like the PuTTY client, and log into the server.
2. Run the following command with the environmental variables specified for your JFrog Artifactory ID, JFrog Artifactory access token, and the image file names for the most up-to-date installation image files that are posted on the JFrog Artifactory repository:

   ```
   $ sudo truncate -s 0 /opt/mdm/conf/.env > /dev/null

   $ echo "SERVER_IP=<XX.XX.XX.XXX>" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "JFROG_USER=<JFrog_Artifactory_ID>" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "JFROG_TOKEN=<JFrog_Artifactory_token    >" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "MDM_IMAGE_PREFIX=hitachi.jfrog.io/docker/mdm/" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "MDM_DB_TAG=< image_file_name >" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "MDM_BE_TAG=<image_file_name>" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "MDM_POSTGRES_TAG=<image_file_name>" |sudo tee -a /opt/mdm/conf/.env > /dev/null

   $ echo "OBS_IMAGE_PREFIX=hitachi.jfrog.io/docker/" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "OBS_OPENOBSERVE_TAG=<image_file_name>" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "OBS_NODEEXP_TAG=< image_file_name >" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "OBS_OTEL_TAG=< image_file_name >" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   ```

   **Note:** For the JFrog Artifactory token, you can use either a Bearer Token or an access token.
3. (Optional) Update the shared memory size of Postgres by running following commands with the new size value specified in gigabytes (example: 2g):

   ```
   $ sudo truncate -s 0 /opt/mdm/conf/.infra.env > /dev/null

   $ echo PG_SHM_SIZE="<new_size_value>” | sudo tee -a /opt/mdm/conf/.infra.env > /dev/null
   ```

   **Note:**

   The default shared memory size of Postgres is 1g (1GB).

After you have set the environmental variables in the Docker container, see [Installing the OpenObserve APM tool components](https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/installing-the-openobserve-apm-tool-components).
