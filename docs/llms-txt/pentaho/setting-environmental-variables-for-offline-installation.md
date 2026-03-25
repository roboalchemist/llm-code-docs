# Source: https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/setting-environmental-variables/setting-environmental-variables-for-offline-installation.md

# Setting environmental variables for offline installation

If you are installing Pentaho Data Mastering without connecting to the internet, you must set environmental variables in the Docker container for the installation image files that you downloaded from HCP Anywhere.

**Important:** Do not specify values for the following fields because these values are filled automatically from the installation image files that you downloaded from HCP Anywhere:

* JFROG\_USER
* JFROG\_TOKEN
* MDM\_IMAGE\_PREFIX
* OBS\_IMAGE\_PREFIX

Complete the following steps to set the environmental variables for offline installation:

1. Open a file transfer tool, like the PuTTY client, and log into your server.
2. Run the following command with the environmental variables specified as the image file names for the corresponding installation files that you downloaded from HCP Anywhere:

   ```
   $ sudo truncate -s 0 /opt/mdm/conf/.env > /dev/null

   $ echo "SERVER_IP=<XX.XX.XX.XXX>    " |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "JFROG_USER=" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "JFROG_TOKEN=" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "MDM_IMAGE_PREFIX=" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "MDM_DB_TAG=<image_file_name>" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "MDM_BE_TAG=<image_file_name>" |sudo tee -a /opt/mdmconf/.env > /dev/null
   $ echo "MDM_POSTGRES_TAG=<image_file_name>" |sudo tee -a /opt/mdm/conf/.env > /dev/null

   $ echo "OBS_IMAGE_PREFIX=" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "OBS_OPENOBSERVE_TAG=<image_file_name>" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "OBS_NODEEXP_TAG=<image_file_name>" |sudo tee -a /opt/mdm/conf/.env > /dev/null
   $ echo "OBS_OTEL_TAG=<image_file_name>" |sudo tee -a /opt/mdm/conf/.env > /dev/null

   ```

   For example, the following image shows the command with the following environmental variables specified:

   * `**MDM\_DB\_TAG**=v1.3.0.20230825`
   * `**MDM\_BE\_TAG**=v1.3.0.20230825`
   * `**MDM\_POSTGRES\_TAG**=v1.3.0.20230808`
   * `**OBS\_OPENOBSERVE\_TAG**=0.0.3-b499cf1`
   * `**OBS\_NODEEXP\_TAG**=v1.0.1`
   * `**OBS\_OTEL\_TAG**=1.0.0-66-925434` ![](https://728502995-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fice38OqJsmUCytyCg7bk%2Fuploads%2Fgit-blob-98dfe350e28617c0a6d7c608f55e5960c6ff752d%2Fsetting_env_var_for_offline_installation.png?alt=media)
3. (Optional) Update the shared memory size of Postgres by running following commands with the new size value specified in gigabytes (For example: 2g):

   ```
   $ sudo truncate -s 0 /opt/mdm/conf/.infra.env > /dev/null

   $ echo PG_SHM_SIZE="<new_memory_size>” | sudo tee -a /opt/mdm/conf/.infra.env > /dev/null
   ```

   **Note:** The default shared memory size of Postgres is 1g (1 gigabyte).

After you have set the environmental variables in the Docker container, see [Installing the OpenObserve APM tool components](https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/installing-the-openobserve-apm-tool-components).
