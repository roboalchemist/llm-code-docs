# Source: https://docs.axonius.com/docs/hpe-switches.md

# HPE Switches

HPE Switches provide switch inventory and ARP table information.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices (fetches from switches)
* [ARP tables](https://arubanetworking.hpe.com/techdocs/AOS-CX/10.10/HTML/ip_services_6200/Content/Chp_ARP/ARP_cmds/sho-arp.htm) (fetches from Hewlett Packard Enterprise (HPE))
* Networks (via advanced setting)

## Parameters

1. **Host Name** *(required)* - The hostname of the HPE Switches server.
2. **Username** and **Password** *(required)* - The credentials for a user account that has  permission to fetch assets.
3. **Protocol** - Select the desired protocol from the dropdown, either **SSH**, **SNMP V2**, or **SNMP V3**.

   * **SSH**
     * **Private Key** *(optional)* - Upload a private key file. Axonius can use the **Private Key** in the file for authentication.

<Callout icon="📘" theme="info">
  Note

  For authentication, you must specify at least password, but you can also specify both password and private key.
</Callout>

* **Private Key Passphrase** *(optional)* - Enter a private key passphrase, in the case that the private key is protected by a passphrase.
  * **SSH Port** *(optional, default: 22)* - Enter a value for the SSH port to use for the connection. Otherwise, Axonius uses the default port 22.
  * **Verify Fingerprint** *(optional)* - Enter the host key configured on the SSH server, which is used to verify that the client is connecting to the correct host. The value can be usually found in \~/.ssh/known\_hosts.
  * **SNMP V2**
    * **SNMP Port** *(required, default: 161)* - Enter a value for the SNMP port to use for the connection. Otherwise, Axonius uses the default port 161.
    * **SNMP Read Community** - Enter a value for the SNMP Read Community. This value requires read-only permissions used in SNMP v1/v2c to control access to a device’s monitoring data.
  * **SNMP V3**
    * **SNMP Port** *(required, default: 161)* - Enter a value for the SNMP port to use for the connection. Otherwise, Axonius uses the default port 161.
    * **SNMPv3 Authentication Passphrase (authKey)** *(required)* - Specify the user authentication key passphrase (authKey).
    * **SNMPv3 Private Passphrase (privKey)** *(required)* - Select the user private key passphrase (privKey).
    * **SNMPv3 Authentication Type (authProtocol)** *(optional, default: hmac\_md5)* - Select the authentication type (authProtocol).
    * **SNMPv3 Privacy Type (privProtocol)** *(optional, default: aescfb128)* - Select the privacy type (privProtocol).
    * **SNMPv3 Security Level (level)** *(optional, default: authPriv)* - Select the security level (level).

<Image alt="HPE_Switches" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HPE_Switches.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch network assets** - Select to fetch Networks as assets using the `show ip route connected` and `show ip route static` commands.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 4.2     | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.0