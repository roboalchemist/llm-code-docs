# Source: https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/downloading-files-and-drivers/downloading-files-for-online-installation.md

# Downloading files for online installation

If you want to install Pentaho Data Mastering while connected to the internet, you must download installation files and drivers from the JFrog Artifactory repository.

Complete the following steps to download installation files and drivers from the JFrog Artifactory repository:

1. In a file transfer tool, like the PuTTY client, connect to the computer that you plan to use as your Pentaho Data Mastering server.
2. Download the latest version of the `mdm-install` image file to your server by running the following command with your JFrog Artifactory user ID, Bearer Token, and image file name specified:

   ```
   $ curl -u<JFrog Artifactory ID>:<Bearer Token> -L -O https://one.hitachivantara.com/artifactory/pntmdm-generic-dev/mdm-install/mdm-install-< image_file_name>.tar.gz

   ```
3. Extract the contents of the `mdm-install` image file by running the following command with the image file name specified:

   ```
   $ sudo tar xzf mdm-install-< image_file_name>.tar.gz -C /opt/
   ```
4. Copy the JDBC drivers to your server by taking one of the following actions:
   * For Development and QA environments, extract the contents of the `mdm-jdbc-drivers` compressed file by running the following command with the image file name specified:

     ```
     $ sudo tar xzf  mdm-jdbc-drivers-<image_file_name>.tar.gz -C /opt/mdm/db_drivers/
     ```
   * For customer environments, use a file archive utility to extract the contents of the `mdm-jdbc-drivers` compressed file and then copy the drivers to the following location on the server: `opt/mdm/db_drivers/location`.

     **Note:** In customer environments, static files are stored in the same location as the JDBC drivers, `opt/mdm/db_drivers/location`.

After you have downloaded files and drivers for the installation, see [Installing configuration pre-requisites](https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/installing-configuration-pre-requisites).
