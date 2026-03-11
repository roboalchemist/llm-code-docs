# Source: https://docs.axonius.com/docs/netapp.md

# NetApp

NetApp offers hybrid cloud data services for management of applications and data across cloud and on-premises environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the NetApp server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
5. **Fetch disks** - Select this option to fetch information about the physical storage disks.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![NetAPp](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NetAPp.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Async chunks in parallel** *(required, default: 50)* - Specify the number of parallel requests all connections for this adapter will send to the NetApp server in parallel at any given point.
2. **Fetch Connected NFS Clients** - Select this option to fetch connected NFS clients.
3. **Create Users from CIFS/SMB Connected Sessions** - Select this option to create users from CIFS/SMB connected sessions.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [ONTAP REST API](https://library.netapp.com/ecmdocs/ECMLP2856304/html/index.html).

## Required Permissions

Use an admin username and use the Cluster management IP address.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version        | Supported | Notes |
| -------------- | --------- | ----- |
| ONTAP 9.6, 9.7 | Yes       |       |