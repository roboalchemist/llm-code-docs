# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/install-the-pdi-tools-and-plugins/use-the-pentaho-installation-wizard-to-install-pdi-client-utilities-and-plugins.md

# Use the Pentaho installation wizard to install PDI client, utilities, and plugins

The Pentaho Business Analytics Installation Wizard is the recommended method for installing the PDI client, utilities, and plugins.

Perform the following steps to use the Pentaho Business Analytics Installation Wizard to install the PDI client, utilities, and plugins:

1. Run the Pentaho Business Analytics Installation Wizard according to the instructions in the **Try Pentaho Data Integration and Analytics** document.

   Be sure to perform the following steps while running the wizard.
2. On the Setup Type window, select the **Let me decide for myself** option.
3. When the Pentaho Applications window displays during the installation process, select the **Data Integration (ETL)** check box.
4. When the installation wizard is complete, start the tools using one of the following ways:
   * Windows: Select the tool you want to start from the **Start** menu.
   * Linux: Open a Terminal window, then navigate to `~/pentaho/design-tools/` and launch the tool.
   * Mac: Navigate to the `Applications/pentaho/design-tools/` and double-click the file.
5. Linux users only: You need to install `libwebkitgtk-1.0` on your system. For example, if you are running Ubuntu you can use the command `sudo apt-get install libwebkitgtk-1.0-0` to install the library.
