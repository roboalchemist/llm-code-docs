# Source: https://docs.axonius.com/docs/advanced-configuration-for-adapters.md

# Advanced Configuration for Adapters

You can configure Advanced Configuration parameters for a  wide range of adapters.
You can configure the Advanced Configuration parameters for all connections for an adapter, or configure separate parameters for each adapter connection. Configuring separate parameters for each connection can be useful if you want to configure a number of fetch cycles for the same set of assets. For instance, if you want to configure a light frequent fetch cycle, and a fetch cycle which is less frequent but consumes more resources.

## Configuring Advanced Configuration Parameters for all Connections

To configure Advanced Configuration parameters for all connections for an adapter:

1. Select the adapter you want to configure.
2. Under  **Advanced Settings**, select **Advanced Configuration**.

<Image alt="AdvacnedSettingsADaptersNew" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdvacnedSettingsADaptersNew.png" />

3. Verify that **Enable advanced configuration  for each connection separately** is not toggled on.

<Image alt="AdvConfigig" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdvConfigig.png" />

4. Configure the settings as required as explained in the relevant documentation for the adapter.

## Configuring Advanced Configuration Parameters for each Connection

To configure separate advanced configuration parameters for each connection for an adapter:

1. Under  **Advanced Settings**, select **Advanced Configuration**.

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdvacnedSettingsADaptersNew.png" />

2. Toggle on **Enable advanced configuration for each connection separately**.

<Image alt="EnableAdvConfig" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EnableAdvConfig.png" />

3. Click **Save.** The **Advanced Configuration** tab now also appears on the **Add Connection** drawer.
4. Click **Add Connection**. The **Connection Configuration** drawer now has 2 tabs.

<Image alt="AdvConfig5" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdvConfig5.png" />

5. Configure the  **Connection Configuration** tab.

6. Click **Advanced Configuration**.

<Image alt="AdvConfig5a" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdvConfig5a.png" />

7. Toggle on **Enable advanced configuration**. The advanced configuration parameters are displayed with the default settings for this adapter.

8. Configure the required parameters for this connection. If you do not configure specific parameters, the connection uses the default settings for that adapter.

9. If necessary, set a specific scheduling for this connection. Refer to [Adapter Discovery Configuration](/docs/adapter-discovery-configuration).

10. After completing the configuration, select either **Save** or **Save and Fetch**.

<Image alt="adv6New" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/adv6New.png" />

<Callout icon="📘" theme="info">
  Note

  Once you have configured advanced configuration for a specific adapter connection, if you toggle off the configuration, the system keeps your choices.
</Callout>

<br />

## Export / Import Adapter Advanced Configuration

You can export or import the settings from the Advanced Configuration page of any adapter using a JSON file. Use this feature to:

* Manage and deploy complex adapter configurations across different environments or even across multiple adapter connections within the same environment.
* Create a backup of your adapter settings before making changes. This allows you to quickly revert to a stable configuration in case of failed changes or unintended outcomes.

<Image alt="Export / Import from Adapter Advanced Configuration page" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/AdaptersAdvancedConfigurationExportImportJSON.png" />

**Export**:

1. Click **Export to JSON**.
2. All fields are exported except for the following fields:
   a. Classified fields (passwords, secrets, keys, etc.)
   b. Files uploaded to the adapter Advanced Configuration.

<Callout icon="📘" theme="info">
  Note

  The export is performed at the GUI level, not the database level. Therefore, unsaved changes displayed in the GUI will be included in the exported file.
</Callout>

**Import**:

1. Click **Import JSON**.
   A browse dialog opens.
2. Select a JSON file and click **Open**.
   The Advanced Configuration fields are automatically populated with the data from the JSON file.

<Callout icon="📘" theme="info">
  Note

  If fields were changed, added to, or removed from the Advanced Configuration page between Axonius versions, the import process will fail.
</Callout>