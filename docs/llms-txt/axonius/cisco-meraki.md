# Source: https://docs.axonius.com/docs/cisco-meraki.md

# Cisco Meraki

Cisco Meraki solutions include wireless, switching, security, EMM, communications, and security cameras, all centrally managed from the web.

### Asset Types Fetched

* Devices
* Software
* Application Settings
* SaaS Applications
* Networks
* Accounts/Tenants
* Network/Firewall Rules
* Alerts/Incidents (if **Fetch Air Marshal data** is selected in [Advanced Settings](#advanced-settings))

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### Creating an API Key

To create an API key:

1. Navigate to the Admin panel. After logging into the panel, click  the username in the top right of the screen and then on **My profile**:

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(10\).png)

2. Click **My Profile**.

3. Under the **API Access** section, click **Generate new API key** and save it to a secure location (you will need it later when configuring the adapter).

   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(11\).png)

4. Refer to [Enabling APIs](https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API#Enable_API_Access) for further information.

### Permissions

The value supplied in [API Key](#required-parameters) for a user account that has permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  * The minimum permission required to fetch assets in Meraki is called Organization (Read).

  * A non-SAML admin with the Organization privilege in Meraki must enable Dashboard API Access under **Organization `>` Settings `>` Dashboard API access**.

  * If an organization has SAML enabled, admins with SAML access cannot generate an API key (these are accounts with a SAML administrator role in Meraki's nomenclature). The account with the Organization (Read) privilege used for generating the API key must be a non-SAML account.
</Callout>

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Cisco Meraki Domain** - The hostname or IP address of the Cisco Meraki server. The domain is: [https://api.meraki.com](https://api.meraki.com)
2. **API Key** - An API key for a user account that has the Required Permissions to fetch assets.

<Image alt="CiscoMeraki.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscoMeraki.png" />

### Optional Parameters

1. **API Prefix** - An API prefix. Either use the default value displayed or leave empty.

2. **VLAN Exclude List** - Enter a comma-separated list of VLANs from which devices are not fetched. If there are any surrounding spaces, they are automatically removed.

3. **Exclude No VLAN Clients** - Select to not fetch devices which are not associated with a VLAN.

4. **SSID Exclude List** - Enter a comma-separated list of SSIDs from which devices are not fetched. If there are any surrounding spaces, they are automatically removed.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch clients URLs history** - Select this option to fetch clients URLs history.
2. **Time in seconds to sleep between each request** *(optional, default: 0)* - Specify sleeping time in seconds between each API request Axonius sends to this adapter.
3. **Fetch MDM devices** *(required, default: true)* - Select this option to fetch MDM devices from Google Workspace.
4. **Fetch additional data for MDM devices** - Select this option to fetch the following data for Cisco Meraki MDM devices:
   * Device profiles
   * Restrictions
   * Security centers
   * Installed software
5. **Fetch client policies** - Select this option to fetch client policies.
6. **Fetch firewall rules** - Select this option to fetch firewall rules.
7. **Fetch Air Marshal data** - Select this option to fetch data from the 'getNetworkWirelessAirMarshal' endpoint.
8. **Parse hostname** - From the dropdown, select the source data for hostname parsing.

<Callout icon="📘" theme="info">
  Note

  * A licensed version of Systems Manager is required for this option to work.

  * 'Fetch MDM Devices' requires the Meraki adapter specific field 'Device Type' to be populated with 'MDM Device'.  Without the MDM Device value present in this field, the 'Fetch MDM Devices' advanced option will not work.
</Callout>

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [Cisco Meraki - Provision Client Policy](/docs/cisco-meraki-provision-client)
* [Cisco Meraki - Update Client Policy](/docs/update-client-policy-in-cisco-meraki)

## Troubleshooting

If your Meraki uses IP restrictions, then make sure you add the IP address of the Axonius instance to the Permissions list.