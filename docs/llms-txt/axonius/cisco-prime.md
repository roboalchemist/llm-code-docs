# Source: https://docs.axonius.com/docs/cisco-prime.md

# Cisco Prime

Cisco Prime offers a suite of tools to automate the management of wired and wireless Cisco networks.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### Permissions

Consult with your vendor for permissions for reading the objects.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Cisco Prime Infrastructure URL** - The URL of the management service.
2. **User Name** and **Password** - The user name and password for a read-only account with the “NBI Credential” and “NBI Read” permissions.

![CiscpoPrime.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscpoPrime.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **Wireless VLAN Exclude List** - You can exclude devices associated with one or a list of VLANs separated by comma.
3. **Wireless SSID Exclude List** - You can exclude devices associated with one or a list of SSIDs separated by comma.
4. **Wireless SSID Include List** - You can include devices associated with one or a list of SSIDs separated by comma.

<Callout icon="📘" theme="info">
  Note

  Cisco Prime applies rate limits to API requests from non-admin users.  In large networks, using a read-only account may cause delays during the discovery process.  In those cases, an account with admin privileges may be used; or the rate limits may be adjusted per [Cisco Rate Limiting](https://d1nmyq4gcgsfi5.cloudfront.net/media/pi_3_4_devnet/api/v4/index.html@id=rate-limiting-doc.html).
</Callout>

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Ignore devices with "FF:FF:00" MAC addresses** - Select whether to ignore devices with unassigned MAC addresses.
2. **Fetch access point devices** - Select this option to fetch data about access point devices and create new devices for each access point. When enabled, the setting below may be configured.
   * **Fetch Network Maps for Access Points** - Select this option to fetch network map images for access points.
3. **Use fetch time as last seen for unassociated active devices** - When this setting is enabled, the adapter will set the **Last Seen** value equal to the **Fetch Time** for reachable devices that have an invalid date-time value for **associationTime**.
4. **Fetch ARP devices from fetched Cisco devices** *(default: true)* - Select this option to fetch ARP devices from the Cisco devices that are fetched. If you clear this option, ARP devices will no longer be fetched from all of the Cisco devices.
5. **Fetch running configurations for each device** - Select this option to fetch configuration files for each device. This setting works only if you have a version equal to or higher than 3.7.1.
6. **Fetch only PRIME\_WIFI\_CLIENT devices** - Select this option to only fetch PRIME\_WIFI\_CLIENT devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>