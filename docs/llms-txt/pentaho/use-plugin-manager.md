# Source: https://docs.pentaho.com/pdia-data-integration/use-plugin-manager.md

# Use Plugin Manager

You can extend Pentaho Data Integration (PDI) by installing plugins. Plugins can add steps, job entries, and extensions.

Plugin Manager is available in:

* the PDI client
* the Pentaho User Console (PUC)

You can use Plugin Manager to:

* Install plugins.
* Update plugins.
* Uninstall plugins.

{% hint style="info" %}
**Notes**

* If you cannot use Plugin Manager, download plugin files from the [Customer Portal](https://support.pentaho.com).
* Plugins installed outside Plugin Manager might not appear in Plugin Manager.
  {% endhint %}

### Install plugins in PDI client

In the PDI client, you can install plugins to extend functionality.

**Before you begin**

* Back up your environment.
* Make sure you have internet access.
* Make sure you have admin privileges, if required.
* Make sure you can write to the plugin directory.
* If you need a custom plugin location, set custom paths in system properties.

**Steps**

1. Open the PDI client.
2. Select **Tools** > **Plugin Manager**.
3. Find the plugin you want.
4. Install the plugin:
   * For the latest version, select **Install**.
   * For an older version:
     1. Select the plugin row.
     2. Pick a version in **Select the plugin version**.
     3. Select **Install**.
5. Restart the PDI client.

{% hint style="info" %}
**Note:** New plugins are not active until you restart the client.
{% endhint %}

6. Verify the install:
   1. Select **Tools** > **Plugin Manager**.
   2. Find the plugin.
   3. Confirm the version appears in **Installed Version**.

### Update plugins in PDI client

Update installed plugins to newer versions.

**Before you begin**

* Make sure you can write to the plugin directory.
* Make sure you have admin privileges, if required.
* Confirm compatibility with your installed Pentaho version.

{% hint style="info" %}
**Note:** Back up your environment before you change plugins.
{% endhint %}

**Steps**

1. Open the PDI client.
2. Select **Tools** > **Plugin Manager**.
3. Next to **Search**, select **Update Available**.
4. Find the plugin you want to update.
5. Select **Update**.
6. Restart the PDI client.
7. Verify the update:
   1. Select **Tools** > **Plugin Manager**.
   2. Find the plugin.
   3. Confirm the version appears in **Installed Version**.

### Uninstall plugins in PDI client

Uninstall plugins you no longer need.

**Steps**

1. Open the PDI client.
2. Select **Tools** > **Plugin Manager**.
3. Next to **Search**, select **Installed**.
4. Find the plugin you want to uninstall.
5. Select the plugin row.
6. In the version list, pick the version to remove.
7. Select **Uninstall**.
8. Confirm the uninstall.
9. Restart the PDI client.
10. Verify the uninstall:
    1. Select **Tools** > **Plugin Manager**.
    2. Next to **Search**, select **Not Installed**.
    3. Confirm the plugin appears as not installed.
