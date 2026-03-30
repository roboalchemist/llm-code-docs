# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-your-linux-environment-for-a-manual-installation/download-and-unpack-installation-files/step-4-unpack-the-operations-mart-ddl-files-reuse.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-your-windows-environment-for-a-manual-installation/download-and-unpack-installation-files/step-4-unpack-the-operations-mart-ddl-files-reuse.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/prepare-your-linux-environment-for-an-archive-install/download-and-unpack-installation-files/step-4-unpack-the-operations-mart-ddl-files-reuse.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/prepare-your-windows-environment-for-an-archive-install/download-and-unpack-installation-files/step-4-unpack-the-operations-mart-ddl-files-reuse.md

# Step 4: (Optional) Unpack the Operations Mart DDL files

The Pentaho Operations Mart distribution file is a package file and needs to be unpacked.

1. Unzip the Pentaho Operations Mart distribution file to a folder.

   The packaged installation file is in the folder.
2. Run the `install.bat` file to unpack the installation file.

   The IZPak window appears.
3. Read the license agreement in the IZPack window. Select the **I accept the terms of this license agreement** check box, and then click **Next.**
4. In the **Select the installation path** text box, browse to and save the file in the `pentaho\server\pentaho-server\data` directory, then click **Next.**

   A warning message appears informing you that the directory already exists.
5. Click **Yes**.

   Any existing files in the directory will be retained.
6. Click **Quit** when the installation progress is complete.
7. Unzip the `pentaho-operations-mart-ddl-9.3.0.zip` file.
8. Move the directory for your database into `pentaho\server\pentaho-server\data\<database name>` and delete the others.

   The appropriate database names are shown in the following table:

   | If your Pentaho Repository is on: | Copy this directory into `pentaho\server\pentaho-server\data\` |
   | --------------------------------- | -------------------------------------------------------------- |
   | PostgreSQL                        | `postgresql`                                                   |
   | MySQL                             | `mysql5`                                                       |
   | Oracle                            | `oracle10g`                                                    |
   | MS SQL Server                     | `sqlserver`                                                    |
9. Complete the steps for installing Data Integration Operations Mart in the **Administer Pentaho Data Integration and Analytics** document before installing your database.
