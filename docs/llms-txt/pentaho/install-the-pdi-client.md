# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/install-the-pdi-tools-and-plugins/perform-a-manual-installation-of-the-pdi-client-utilities-and-plugins/install-the-pdi-client.md

# Install the PDI client

Perform the following steps to install the PDI client:

1. Download the `pdi-ee-client-9.3.0-<build number>-dist.zip` file from the [Support Portal](https://support.pentaho.com/hc/en-us).
   1. On the [Support Portal](https://support.pentaho.com/hc/en-us) home page, sign in using the Pentaho support username and password provided in your Pentaho Welcome Packet.
   2. In the Pentaho card, click **Download**.

      The Downloads page opens.
   3. In the **9.x** list, click **See all \<number> articles** to see the full list of **9.x** downloads.
   4. On the **9.x** page, click **Pentaho 9.3 GA Release**.
   5. Scroll to the bottom of the Pentaho 9.3 GA Release page.
   6. In the file component section, navigate to the `Client Tools/PDI Spoon` directory.
   7. Download the `pdi-ee-client-9.3.0-<build number>-dist.zip`
2. Use a ZIP tool to extract the file you just downloaded.

   **CAUTION:**

   Do not use Unarchiver 3.3 to unzip files; it might corrupt the plugin file names.
3. Open a Command Prompt or Terminal window and navigate to the folder that contains the files you just extracted.
4. Enter one of the following at the prompt.
   * For Windows: `install.bat`
   * For Linux: `./install.sh`
5. Read the license agreement that appears. Select **Accept**, then click **Next**.

   **Note:** If you are unpacking the file in a non-graphical environment, open a Terminal or Command Prompt window and type `java -jar install.jar -console` and follow the instructions presented in the window.
6. Specify where you want the file to be unpacked.

   The location you specify can be temporary because you will be manually placing the files in the appropriate directories later in these instructions.
7. Click **Next**.

   The Installation in Progress window appears.
8. When the installation progress is complete, click **Quit** to exit the Unpack Wizard.
9. Create a directory for your tools and utilities.

   If you are unsure of what directory to create, consider creating a `pentaho` directory and `design-tools` subdirectory on your workstation. If you choose this option, the directory path should look like the following example:

   ```
   pentaho/design-tools
   ```
10. Copy or move the extracted files to the `pentaho/design-tools` directory.

    The design tool, utilities, and plugins appear in the following path:

    ```
    pentaho/design-tools/data-integration (Spoon, Kitchen, Pan, Carte)
    ```
