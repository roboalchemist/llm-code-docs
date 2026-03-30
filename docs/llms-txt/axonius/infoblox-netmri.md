# Source: https://docs.axonius.com/docs/infoblox-netmri.md

# Infoblox NetMRI

Infoblox NetMRI provides network change and configuration management (NCCM), enabling users to automate network change, understand network health, manage network configurations, and meet a variety of compliance requirements.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Infoblox NetMRI domain** *(required)* - The hostname or IP address of the Infoblox NetMRI server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
3. **Fetch Neighbors** *(required, default: false)* - Select to fetch neighbor devices for this device, presenting them as aggregated.
4. **Fetch Discovery Status** *(optional, default: false)* - Select to fetch the discovery status of each device.
5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![NetMRI\_17-1-22](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NetMRI_17-1-22.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Number of requests in parallel** *(required, default: 50)* - Specify the number of requests to make at the same time in order to fetch information about devices.
* **Fetch Infrastructure Devices** - Select this option to fetch infrastructure devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, and it is not functioning as expected.

| Version               | Supported | Notes |
| --------------------- | --------- | ----- |
| Infoblox NetMRI V 7.2 | Yes       |       |