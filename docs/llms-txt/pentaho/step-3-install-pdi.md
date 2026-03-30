# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/install-the-pdi-tools-and-plugins/step-3-install-pdi.md

# Step 3: Install PDI

Move the PDI files that you previously unpacked to the appropriate directories so that you can install PDI.

Perform the following steps to move the PDI files into the appropriate directory.

1. Create a directory for installing the design tools that has permissions to read, write, and execute commands.

   For example, you can create the `Pentaho/design-tools` directory on your workstation.

   **Note:** For publishing reports, models, and schemas created with the design tools, it is a best practice to install the design tools in a directory on a workstation or server that is on the same network as the Pentaho Server.
2. In your operating system, verify that you have the appropriate permissions to read, write, and execute commands in the directories that you created.
3. Move the PDI files to the `pentaho/design-tools` directory.

   The design tool, utilities, and plugins appear in the following directory:

   ```
   pentaho/design-tools/data-integration (Spoon, Kitchen, Pan, Carte)
   ```
4. (Optional) If you plan to connect to a Hadoop cluster or work with a Pentaho Data Service, move the contents of the `pdi-ee-10.2.0.0-<build number>-hadoop-addon.zip` file into the `pentaho/design-tools/data-integration` directory.
