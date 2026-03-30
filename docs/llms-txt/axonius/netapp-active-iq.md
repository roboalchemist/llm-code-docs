# Source: https://docs.axonius.com/docs/netapp-active-iq.md

# NetApp Active IQ Unified Manager

Active IQ Unified Manager provides performance monitoring capabilities and event root-cause analysis for systems running NetApp ONTAP software.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users, File Systems

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Active IQ Unified Manager server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![NetappActiveIQunifiedMan](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NetappActiveIQunifiedMan.png)

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Fetch SVMs** - Select this option to fetch SVMs.
2. **Fetch file systems** - Select this option to fetch file systems.
3. **Fetch users** - Select this option to fetch users.

## APIs

Axonius uses the [Active IQ Unified Manager API](https://library.netapp.com/ecmdocs/ECMLP2865023/html/index.html#/datacenter/node_collection_get)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [User Name](#parameters) must have read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 5.0