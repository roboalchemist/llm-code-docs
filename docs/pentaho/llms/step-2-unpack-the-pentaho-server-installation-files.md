# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-your-linux-environment-for-a-manual-installation/download-and-unpack-installation-files/step-2-unpack-the-pentaho-server-installation-files.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-your-windows-environment-for-a-manual-installation/download-and-unpack-installation-files/step-2-unpack-the-pentaho-server-installation-files.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-your-windows-environment-for-a-manual-installation/download-and-unpack-installation-files/step-2-unpack-the-pentaho-server-installation-files.md

# Step 2: Unpack the Pentaho Server installation files

You must unpack the Pentaho Server installation file and move the contents to the correct directories for a manual installation.

Complete the following steps to unpack the installation file and move the contents to the correct directories.

1. Locate the `pentaho-server-manual-ee-10.2.0.0-<build number>.zip` file that you downloaded in [Step 1: Download files](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-your-windows-environment-for-a-manual-installation/download-and-unpack-installation-files/step-1-download-files-reuse).
2. Unpack the `pentaho-server-manual-ee-10.2.0.0-<build number>.zip` file and move the contents into the `\pentaho\server\pentaho-server` directory.
3. In the `\pentaho-server` directory, navigate to the `\pentaho-server-manual-ee` directory.
4. Unpack the following ZIP files and place the contents of the files in the appropriate directories.

   The following table lists the files to unpack and the directories where the contents from the file must be moved.

   | File to unpack                  | Directory where you move the file contents |
   | ------------------------------- | ------------------------------------------ |
   | `license-installer.zip`         | `pentaho\server`                           |
   | `jdbc-distribution-utility.zip` | `pentaho\server`                           |
   | `pentaho-data.zip`              | `pentaho\server\pentaho-server`            |
   | `pentaho-solutions.zip`         | `pentaho\server\pentaho-server`            |
5. Copy the `.war` and `.html` files to the following directories on your web application server.​

   The following table lists the files to copy and the directories where the files must be copied.

   | File                              | Directories that you copy the file into                                 |
   | --------------------------------- | ----------------------------------------------------------------------- |
   | `pentaho.war`                     | `pentaho\server\pentaho-server\<tomcat installation directory>\webapps` |
   | `pentaho-style.war`               | `pentaho\server\pentaho-server\<tomcat installation directory>\webapps` |
   | `PentahoServer_OSS_Licenses.html` | `pentaho\server\pentaho-server`                                         |
