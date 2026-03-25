# Source: https://docs.axonius.com/docs/connectwise.md

# ConnectWise Automate

ConnectWise Automate monitors, manages, and supports client networks using out-of-the-box scripts, continuous monitoring, and automation capabilities.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ConnectWise Automate server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![connectWiseAutomate.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/connectWiseAutomate.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch patching stats** - Select whether to fetch statistics about the device’s patches.
2. **Fetch Microsoft patches** - Select whether to fetch data about Microsoft updates and patches relating to the device.
3. **Fetch third-party patches** - Select whether to fetch third-party patches, such as installed software updates.
4. **Fetch device software** - Select whether to fetch data about the software installed on each device.
5. **Fetch device drives** - Select whether to fetch data about the drives of each device.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [ConnectWise API](https://developer.connectwise.com/Products/Automate/Integrating_with_Automate/API/REST).

## Required Permissions

To connect, Multi-factor authentication must be turned off.

## Supported From Version

Supported from Axonius version 4.5