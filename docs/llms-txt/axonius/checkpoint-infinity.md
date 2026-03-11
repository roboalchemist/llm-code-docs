# Source: https://docs.axonius.com/docs/checkpoint-infinity.md

# Check Point Infinity

Check Point Infinity protects against cyber threats across networks, endpoint, cloud and mobile devices. This adapter supports the entire Infinity platform, *including Check Point firewalls*.

<Callout icon="📘" theme="info">
  Note

  To enable Axonius to fetch data:

  * In **Checkpoint Infinity Management API** > **Access Settings**,  the *Accept API calls* setting must be set to *All IP addresses that can be used for GUI clients*, or to *All IP Addresses*,.
  * When working with a Tunnel, in the Checkpoint Management Server WEB UI configuration, the IP address of the Tunnel Server must be added to **Host Access**.
</Callout>

## Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Network_Firewall_Rules.svg) Network/Firewall Rules | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Network_Routes.svg) Network Routes

## Before You Begin

### Permissions

A user account with permission to access the System Data domain in Check Point Infinity is required.
This can be achieved through either of the following:

* A Superuser account
* A custom read-only permission profile that includes System Data access.

### Creating a read-only user for Check Point Infinity

Creating a read-only permission profile varies between different versions of Check Point Infinity and instructions for doing so can be found in the Check Point user manual. As a general reference,[the following guide can be used](https://sc1.checkpoint.com/documents/R80.10/WebAdminGuides/EN/CP_R80.10_SecurityManagement_AdminGuide/html_frameset.htm?topic=documents/R80.10/WebAdminGuides/EN/CP_R80.10_SecurityManagement_AdminGuide/162331) to create read-only users.

### Finding the Management API Key and the Management Server URL in the Check Point Infinity Portal

If you are using the Check Point Infinity Portal to manage the Check Point firewall management server, the required URL and API Key can be found under the menu “Settings” `>` “API & Smart Console”. See the screenshot below for reference.

<Image alt="Check Point Infinity portal API Key" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Check%20Point%20Infinity%20portal%20API%20Key.png" />

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Check Point Host URL** - The hostname of the Check Point Infinity server.

<Callout icon="📘" theme="info">
  Note

  When the **Check Point Host URL** is a managed server, you need to set the full login URL and use **API Key** instead of **User Name** and **Password**. For more information, see [Finding the Management API Key and the Management Server URL in the Check Point Infinity Portal](/docs/checkpoint-infinity#finding-the-management-api-key-and-the-management-server-url-in-the-check-point-infinity-portal).
</Callout>

2. **User Name** and **Password** - The credentials for a user account that has Read-only permissions to fetch assets.
3. **API Version** *(default: v1.6 and later)*  - Select the API Version to use, either **v1.5 or earlier** or **v1.6 and later**.  Refer to [Check Point Management API Reference](https://sc1.checkpoint.com/documents/latest/APIs/index.html#api_versions~v1.9%20).

<Image alt="CheckPointInfiNew" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CheckPointInfiNew.png" />

### Optional Parameters

1. **API Key** - An API Key associated with a user account that has permissions to fetch assets.
2. **Check Point Domain** - An optional domain to connect within the Check Point Infinity server. Use a Multi-Domain Server (MDS) in order to also fetch administrator users. “System Data” is the default MDS domain name.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Calculate Last Seen from creation/modification date** *(optional)* - Select whether to calculate **Last Seen** based on the Last Modified Date or Creation Date.
2. **Compare devices to "Unused Objects" database** *(optional)* - When selected, assets that match a record in the Unused Objects database by their UID receive a new **Detected as Unused Object** field set to **Yes** in the Query Wizard; assets that don't match any such records are set to **No** in the Query Wizard.
3. **Exclude devices that match "Unused Objects"** *(optional)* - When selected, regardless of the **Compare devices to "Unused Objects" database** parameter, assets that match a record in the Unused Objects database are excluded from the fetch, and aren't added to Axonius.
4. **Use System Data Domain for Users fetch.** - Select this option to switch the authentication/login context so the fetch is done on global/MDS-level users, instead of domain-level ones.
5. **Create Devices from Smart Mgmt logs** *(optional)* - Select to create devices from Smart Management API logs.
6. **Extended NAT Handling for device enrichment** - Select this option to match host objects against the NAT rulebase to anticipate additional IP addresses for those objects.
7. **Add IPs from NAT policy as device interfaces** - Select this option to add IP addresses from the NAT policy as devices interfaces.
8. **Extend NAT Rules as connected devices** - Select this option to parse the NAT rules as connected devices for the Checkpoint Device Asset.
9. **Policy Packages for Extended NAT handling (All when empty)** - Enter policy packages to use for extended NAT handling.
10. **Match NAT rules on original columns**  *(default: Original Source or Destination)* - Select how to match the NAT rules on original columns.
11. **Match NAT rule method** - Select this option to match the NAT rule method.
12. **Internal CIDR blocks** *(optional, default: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)* - Enter the internal CIDR blocks that you want to fetch from.
13. **Log search timeframe** *(optional, default: last-hour)* - Filter search results of logs by the specified timeframe. The Smart Management log API can return a maximum of 1 million records.
14. **Log search criteria** *(optional, default: blade:"Firewall")* - Filter search results of logs by specific types of devices and products.
15. **Fetch Threat Protection data** - Enable this to fetch all threat prevention policies and threat protection signatures, and enrich gateway devices with CVEs that are protected by their assigned threat prevention profiles.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

[Checkpoint Infinity - Tag Devices that are Publicly Exposed by a FW/NAT Rule](/docs/checkpoint-r80)