# Source: https://docs.axonius.com/docs/vmware-horizon.md

# Omnissa Horizon

Omnissa Horizon is a platform for secure delivery of virtual desktops and apps across the hybrid cloud.

<Callout icon="📘" theme="info">
  Note

  This adapter was previously named VMWare Horizon.
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Compute Services

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Omnissa Horizon server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Domain** *(required, default: vsphere.local)* - The Omnissa Horizon server Domain.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![OmnissaHorizon.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-FOGMO07R.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Application Pools** - Select this option to fetch application pools and their entitlements. They are fetches as Devices.
2. **Fetch Farms** - Select this option to fetch farms as Compute Services asset type.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [VMware Horizon Server](https://code.vmware.com/apis/1007/view-rest-api) API.

## Required Permissions

The value supplied in [User Name](#parameters) must be connected to the Administrators on Root access group as Read Only to fetch assets.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 8.0     | Yes       |       |