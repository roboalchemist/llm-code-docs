# Source: https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/downloading-files-and-drivers/downloading-files-for-offline-installation.md

# Downloading files for offline installation

If you do not plan to use the internet while installing Pentaho Data Mastering, you must first download installation image files from HCP Anywhere.

Complete the following steps to download the Pentaho Data Mastering installation image files from HCP Anywhere:

If you are installing Pentaho Data Mastering without connecting to the internet, you must have a download link and access code to access HCP Anywhere, which is provided to you by Hitachi Vantara. If you were not provided with a download link and access code, contact support to request a download link and access code.

1. Open a file transfer tool, like the PuTTY client, and log into your server.
2. Log into HCP Anywhere using the download link and access code provided to you and download the files and drivers needed for the installation process.
3. Load the Pentaho Data Mastering installation image file by running the following command with the image file name specified:

   ```
   $ sudo docker load -i <image_file_name>.tar.gz
   ```

   The Pentaho Data Mastering installation image file is loaded into the Docker runtime so that you can use the Docker runtime to install Pentaho Data Mastering from the image file.
4. Verify that the Pentaho Data Mastering installation image file is loaded into the Docker runtime by running the following command:

   ```
   $ sudo docker images
   ```

   For example, the following image shows the output that is produced when you run the `$ sudo docker images` command.

   ![](https://728502995-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fice38OqJsmUCytyCg7bk%2Fuploads%2Fgit-blob-2361861f2f107f99344dff4a4bb5bd6361a3205e%2Fenv_setup_offline_inst.png?alt=media)

After you have downloaded files and drivers for the installation, see [Installing configuration pre-requisites](https://docs.pentaho.com/pentaho-data-mastering/installing-pentaho-data-mastering/installing-configuration-pre-requisites).
