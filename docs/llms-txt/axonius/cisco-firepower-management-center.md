# Source: https://docs.axonius.com/docs/cisco-firepower-management-center.md

# Cisco Firepower Management Center

Cisco Firepower Management Center provides management over firewalls, application control, intrusion prevention, URL filtering, and advanced malware protection.

## Assets Types Fetched

* Devices, Networks, Network/Firewall Rules

## APIs

* Axonius uses the [Firepower Management Center REST API](https://www.cisco.com/c/en/us/td/docs/security/firepower/630/api/REST/Firepower_Management_Center_REST_API_Quick_Start_Guide_630/Objects_in_the_REST_API.html)
* Review info about Authentication [here](https://www.cisco.com/c/en/us/td/docs/security/firepower/630/api/REST/Firepower_Management_Center_REST_API_Quick_Start_Guide_630/Connecting_with_a_Client.html).

## Required Permissions

The value supplied in [User Name](#parameters) must have Devices `>` Device Management permissions in order to fetch assets.

The following permissions are required in order to enable the advanced configurations:

* **Get the device hosts**:
  * Object Manager
* **Fetch firewall rules**:
  * Object Manager
  * Devices `>` NAT `>` NAT List
  * Policies `>` Access Control `>` Access Control Policy

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Cisco Firepower Management Center server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Cisco Firepower Management Center](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cisco%20Firepower%20Management%20Center.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Get the device hosts** - Select this option to retrieve all devices of the type host. When enabled, the adapter fetches data from the `object/hosts` API endpoint, which returns host objects - network objects representing IP addresses or hosts configured in Firepower.

   <Callout icon="📘" theme="info">
     **Note**

     You must have the Object Manager permission to enable this setting.
   </Callout>
2. **Fetch firewall rules** - Select this option to fetch firewall rules. For the permissions required to enable this setting, see [Required Permissions](/docs/cisco-firepower-management-center#required-permissions).
3. **Enrich firewall access rules with hit counts** - Select this option to enrich firewall rules with hit-counts-per-rule information.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />