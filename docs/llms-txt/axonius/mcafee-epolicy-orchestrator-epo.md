# Source: https://docs.axonius.com/docs/mcafee-epolicy-orchestrator-epo.md

# Trellix ePolicy Orchestrator (ePO)

Trellix ePolicy Orchestrator (ePO) is a security management platform that provides real-time monitoring of security solutions.  This adapter connects to the ePO server to import information about devices managed by that solution.

<Callout icon="📘" theme="info">
  Note

  This adapter was previously named **McAfee ePolicy Orchestrator (ePO)**.
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications

## Parameters

1. **Host** *(required)* - The hostname of the Trellix ePolicy Orchestrator (ePO) server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Port** *(required)* - Use TCP port 8443.

3. **User** and **Password** *(required)* - The credentials for a user account that has permissions to fetch assets.

4. **Installed Software Query ID** *(optional)*  - The ID from the URL bar in the ePO.  Set this for product name parsing. It should contain the following fields:
   * DiscoveredSystemOnApps.Name
   * DiscoveredSystemOnApps.Version
   * DiscoveredSystemOnApps.Publisher
   * EPOComputerProperties.ComputerName

5. **Drive Encryption Query ID** *(optional)*  - The ID of an existing EPO Query that contains at least 'EPOLeafNode.NodeName' and 'EPESystems.State' information to populate Hard Drive Encryption data for devices. The user specified for the connection must have permissions to access the saved query in order for the additional data to be fetched.

6. **Non-Compliant Devices Query ID** *(optional)* - Select this option to run the query specified by the Query ID. The query itself must be configured to at least return the EPOLeafNode.NodeName column. Any device in which the NodeName matches a result from this query will have the **Non-Compliance Detected** field set to true. All devices not returned in this query will have the **Non-Compliance Detected** field set to False.

7. **Events Management Query ID** *(optional)* - Specify the Events Management Query ID to fetch threat events.

8. **Benchmark Query ID** *(optional)* - Specify the Benchmark Query ID to query audit logs.

9. **OAM Query ID** *(optional)* - Specify the OAM Query ID to fetch additional information.

10. **Solidcore Query ID** *(optional)* - Enter a Query ID for Solidcore client data.

11. **Applied Policy Query ID** - Select this option to fetch assigned Policy information, such as applied firewall rules.

12. **Use Rolled Up Query** - Select whether to use a rolled-up query from multiple databases.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).
 

<Image alt="addconnection" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-WC79GHX8.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Read Timeout (seconds)** *(optional)* - Set the timeout in seconds for reading data from the ePO connection.
2. **Exclude IPv6 addresses** - Select this option to fetch IPv6 addresses (as well as IPv4 addresses).
3. **ePO tags Include list** *(optional)* - Specify a comma-separated list of Trellix ePO tags.
   * If supplied, all connections for this adapter will only fetch devices tagged in Trellix ePO with the tags provided in this list.
   * If not supplied, the connection for this adapter will fetch all devices from Trellix ePO.
4. **Include devices with no Agent GUID** - Select to include devices with no Agent GUID, using their EPOLeafNode.NodeName as the ID. When option is cleared, these devices are ignored.
5. **Fetch COAMS Data** - Select this option to fetch COAMS data. To obtain COAMS, query the `OAM_OperationalAttributes` table by selecting the following fields: `EPOComputerProperties.ComputerName APS_OAM_CombinedAttributesView.TagName`                      `APS_OAM_CombinedAttributesView.TagValue APS_OAM_CombinedAttributesView.FQN`. Then join the `EPOComputerProperties, APS_OAM_CombinedAttributesView` tables.
6. **Enrich data for each device dynamically using these query IDs** *(optional)* - Type a value, and then press **Enter**, comma, or semicolon to add each additional value to the list of query IDs to enrich each device. You can also paste a comma-separated list into the field.
7. **Enable software name sanitization** - Toggle on this option to specify how to sanitize software names.
   * **Regular expression and replacement list** - Enter a comma-separated list of regular expressions and replacements. Each string in this list holds two values separated by `#AX_REPLACE_WITH#`. The first value must be a valid regular expression that matches what you want to replace. The second value must be what you wish to replace it with. Example: `_#AX_REPLACE_WITH#` to replace underscores with spaces. Example: `^[0-9]{4}-[0-9]{2}-[0-9]{2}#AX_REPLACE_WITH#` to remove dates from the start of the name.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Trellix ePO API](https://developer.manage.trellix.com/public/mvision/apis/v2-devices).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 8443**

## Required Permissions

Create a service account in Trellix ePO that has View access to the systems tree tab and sub systems tree.
Additionally, in the Permissions Sets section under User Management, select the following:
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MCEPONew%20permis.png)

### Related Enforcement Actions

[Trellix ePolicy Orchestrator (ePO) - Add Assets](/docs/epo-add-asset)
[Trellix ePolicy Orchestrator (ePO) - Add or Remove Tag to/from Assets](/docs/tag-in-mcafee-epolicy-orchestrator-epo)