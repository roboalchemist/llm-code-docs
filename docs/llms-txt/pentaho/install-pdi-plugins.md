# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/install-the-pdi-tools-and-plugins/perform-a-manual-installation-of-the-pdi-client-utilities-and-plugins/install-pdi-plugins.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/install-the-pdi-tools-and-plugins/install-pdi-plugins.md

# Step 4: Install PDI plugins

If you have the PDI client already installed, you can manually download and install the plugins via a ZIP file, or you can install the plugins through the PDI Marketplace in PDI client.

## Perform a manual installation of the PDI plugins

1. Download the plugin you want to install.
2. Unzip it in the appropriate subdirectory in: `pentaho/design-tools/data-integration/plugins`

   To determine the correct subdirectory, see the instructions for the plugin you are installing.

Perform the following steps to manually install the PDI plugins, follow these steps.

## Visit the PDI Marketplace to install the PDI plugins

Perform the following steps to install the PDI plugins through the PDI Marketplace:

1. Start Pentaho Data Integration (PDI).
2. Select **Tools** > **Marketplace**.

   The PDI Marketplace window appears.
3. The name of the plugin appears in the **Detected Plugins** section of the page.

   Note which plugins are installed. You can filter the list by typing the name of the plugin in the **Detected Plugins** text box.
4. Click the name of the plugin to expand it.

   Information about the plugin, including the documentation, source code, and support information appears.
5. Click **Install this plugin**.

   The **Progress Information** dialog box appears, indicating the operation is in process. When the plugin has been successfully installed, a message appears indicating that you will need to restart your client, which is the PDI client (Spoon).
6. Click **OK**.
7. Restart PDI.
8. To verify that the plugin was installed, open the PDI Marketplace window again.

   The plugin should be listed as installed.

The plugin should appear in the logical place in the PDI client interface. For example, if the plugin that you install is the 'CMIS Input' plugin, then it will appear in the **Design** tab within the **Output Steps** category.

<br>
