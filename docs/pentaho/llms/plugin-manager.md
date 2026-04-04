# Source: https://docs.pentaho.com/pba/pentaho-user-console/modern-design/plugin-manager.md

# Plugin Manager

Use the Plugin Manager to install, update, and uninstall plugins for the **Pentaho User Console (PUC).** Plugins extend the Pentaho Platform by adding new components and new capabilities, such as new visualizations, dashboards, and content access extensions. The Plugin Manager is available exclusively in Modern Design interface of PUC.

## Before you begin&#x20;

* Back up your environment before making any changes to plugins. This is a recommended best practice.
* Verify that you meet the following requirements:&#x20;
  * You have internet access. The environment within which Pentaho Server is deployed must have internet access. If this is not the case, please contact Support to deploy plugins.&#x20;
  * You have *Write* permissions to the plugin directory.
  * If a plugin requires administrative privileges to manage, verify that you have those privileges.
* If you want to install plugins in a custom location, set the custom paths in the system properties. By default, the Plugin Manager detects writable plugin directories and avoids restricted locations, such as `tomcat/bin`.

## Install plugins in PUC

Install plugins to extend the Pentaho Platform by adding new components and new capabilities, such as new visualizations, dashboards, and content access extensions.

To install a plugin, complete the following steps:&#x20;

1. Log into **PUC**.
2. Open the **Plugin Manager** by taking one of the following actions:&#x20;

   1. If you are using the **Modern Design** of PUC, in the menu on the left side of the page, click **Plugin Manager**.&#x20;
   2. If you are using the **Classic Design** of PUC, click **Switch to the Modern Design,** and then in the menu on the left side of the page, click **Plugin Manager.**

   The **Plugin** **Manager** opens with a list of plugins shown in a table.&#x20;
3. Search for or browse to the plugin you want to install.
4. Install the plugin by taking the following actions:

   1. Click the table row for the plugin. The ***Plugin name*** dialog box opens.
   2. Select the plugin from the **Select the plugin version** list and click **Install.**&#x20;
   3. If prompted, confirm the installation to proceed.&#x20;

   The plugin is installed.
5. Restart the **Pentaho Server**.&#x20;

   **Note:** Newly installed plugins are not active until the server is restarted.
6. Refresh **PUC** in the browser.
7. To verify that the plugin is installed, complete the following steps:
   1. In the **Plugin Manager** for **PUC**, search for or browse to the plugin.&#x20;
   2. Verify the version you installed is listed in the **Installed Version** column.

{% hint style="info" %}
**Notes**:&#x20;

* If you cannot use Plugin Manager, you can download plugin installation files and documentation from the [Customer Portal](https://support.pentaho.com).&#x20;
* Plugins installed outside of the Plugin Manager might not be listed in the Plugin Manager and must be maintained manually.
  {% endhint %}

## Update plugins in PUC

Update existing plugins to a later version that is compatible with your installed version of **Pentaho**.

To update a plugin, complete the following steps:&#x20;

1. Log into **PUC**.
2. Open the **Plugin Manager** by taking one of the following actions:&#x20;

   * If you are using the **Modern Design** of **PUC**, in the menu on the left side of the page, click **Plugin Manager**.&#x20;
   * If you are using the **Classic Design** of PUC, click **Switch to the Modern Design,** and then in the menu on the left side of the page, click **Plugin Manager.**

   The **Plugin** **Manager** opens with a list of plugins shown in a table.&#x20;
3. To the right of the **Search** box, open the list and select **Update Available**. A list of plugins with available updates is shown.
4. Search for or browse to the plugin you want to update.
5. Click **Update**. The plugin is updated.
6. Restart the **Pentaho Server**.&#x20;
7. Refresh **PUC** in the browser.
8. To verify that the plugin is updated, complete the following steps:
   1. In the **Plugin Manager** for **PUC**, search for or browse to the plugin.&#x20;
   2. Verify the plugin's new version is listed in the **Installed Version** column.

## Uninstall plugins in PUC

Uninstall plugins that you no longer need.

To uninstall a plugin, complete the following steps:&#x20;

1. Log into **PUC**.
2. Open the **Plugin Manager** by taking one of the following actions:&#x20;

   * If you are using the **Modern Design** of **PUC**, in the menu on the left side of the page, click **Plugin Manager**.&#x20;
   * If you are using the **Classic Design** of PUC, click **Switch to the Modern Design,** and then in the menu on the left side of the page, click **Plugin Manager.**&#x20;

   The **Plugin** **Manager** opens with a list of plugins shown in a table.&#x20;
3. To the right of the **Search** box, open the list and select **Installed**. A list of installed plugins is shown.
4. Search for or browse to the plugin you want to uninstall.
5. Click the table row that contains the plugin. The ***Plugin name*** dialog box opens.
6. In the list at the bottom of the dialog box, select the version of the plugin that you want to uninstall.
7. Click **Uninstall**. A confirmation dialog box opens.&#x20;
8. Click **OK**. A dialog box with the status of the plugin opens.
9. Click **OK**.&#x20;
10. Restart the **Pentaho Server** and **PDI client**.
11. To verify that the plugin is uninstalled, complete the following steps:
    1. Log into **PUC**.
    2. Open the **Plugin Manager** by taking one of the following actions:&#x20;

       * If you are using the **Modern Design** of **PUC**, in the menu on the left side of the page, click **Plugin Manager**.&#x20;
       * If you are using the **Classic Design** of PUC, click **Switch to the Modern Design,** and then in the menu on the left side of the page, click **Plugin Manager.**&#x20;

       The **Plugin** **Manager** opens with a list of plugins shown in a table.&#x20;
    3. To the right of the **Search** box, open the list and select **Not Installed**. A list of plugins that are not installed is shown.
    4. Verify the plugin is uninstalled by searching for or browsing to the plugin in the **Not Installed** table.
