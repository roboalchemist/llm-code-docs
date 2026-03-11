# Source: https://docs.axonius.com/docs/juniper-junos-space-network-management-platform.md

# Juniper Junos Space

Juniper Junos Space Network Management Platform automates management of Juniper's switching, routing, and security devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users, Networks, Network/Firewall Rules

## Parameters

1. **Domain Name or IP Address** *(required)* - The hostname or IP address of the Junos Space device.

2. **User Name** and **Password** *(required)* - The credentials for an admin user that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Juniper Junos Space](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Juniper%20Junos%20Space.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch users** - Select this option to fetch users. This option requires the permissions *ReadUser*, *CreateDomain*, *ModifyDomain*. For more information, see the [Junos Space REST API](https://www.juniper.net/documentation/en_US/junos-space-sdk/23.1/apiref/com.juniper.junos_space.sdk.help/JSUserMgtSvc/Docs/rest.users.html#GET_vnd.net.juniper.space.user-management.users/v3;q=0.03GET).

2. **Fetch Junos Space Juniper devices only** *(required, default: False)*
   * If enabled, all connections for this adapter will only fetch information on Juniper devices, not including extra information through SSH.
   * If disabled, all connections for this adapter will fetch all information, including ARP tables.

3. **Fetch only Juniper clients Information** *(required, default: False)*
   * If enabled, all connections for this adapter will only fetch switches metadata.
   * If disabled, all connections for this adapter will fetch all information, including ARP tables.

4. **Fetch clients ARP devices information** - Select this option to fetch devices of type ARP, in addition to the default devices.

5. **Fetch clients FDB devices information** - Select this option to fetch devices of type FDB, in addition to the default devices.

6. **Fetch Vlans and interfaces information** *(required, default: True)*
   * If enabled, all connections for this adapter will fetch Vlans and interfaces information.
   * If disabled, all connections for this adapter will not fetch Vlans and interfaces information.

7. **Fetch Network Entities** - Select to fetch addresses and Firewall Policies Rules.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the following APIs:

* [Juniper Junos Space User Management API](https://www.juniper.net/documentation/en_US/junos-space-sdk/23.1/apiref/com.juniper.junos_space.sdk.help/JSUserMgtSvc/Docs/rest.users.html#GET_vnd.net.juniper.space.user-management.users/v3;q=0.03GET)
* [Juniper Junos Space Device Manager API](https://www.juniper.net/documentation/en_US/junos-space-sdk/23.1/apiref/com.juniper.junos_space.sdk.help/DeviceDiscoveryManagerRest/Docs/rest.devices.html)

## Required Permissions

You must define an API Access Profile with "OpenSSH" and "ReadDevices" RPC command rules, and associate that API Access Profile to the defined user.

Admin users requires those RPC command rules to run XML RPC commands on the remote devices.

For more details, see Juniper TechLibrary:

* [Creating Users in Junos Space Network Management Platform](https://www.juniper.net/documentation/en_US/junos-space17.1/platform/topics/task/configuration/junos-space-user-accounts-creating.html)
* [Creating an API Access Profile](https://www.juniper.net/documentation/en_US/junos-space17.1/platform/topics/task/configuration/api-access-profile-creating.html)

The permissions *ReadUser*, *CreateDomain*, and *ModifyDomain* are required in order to fetch users.

## Version Matrix

Axonius should be compatible with any version of the Juniper Junos Space Network Management Platform and its connected Juniper endpoint devices.