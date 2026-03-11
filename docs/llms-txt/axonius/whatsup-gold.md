# Source: https://docs.axonius.com/docs/whatsup-gold.md

# WhatsUp Gold

WhatsUp Gold is network monitoring software.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the WhatsUp Gold server.

2. **Auth Method** - Select an Authentication method, either **Authentication with Credentials** (default) or **Authentication with Token**.
   * **Authentication with Credentials**: **User Name** and **Password** - The credentials for a user account that has permissions to fetch assets.
   * **Authentication with Token**: **Access Token** - An Access Token associated with a user account that has permissions to fetch assets.

3. **Port** *(required, default: 9644)* - The port used for the connection.

4. **Group ID** *(default: -2)* - Use this to display the devices the user has access to. -2 fetches the entire network.

5. **Verify SSL** *(required, default: false)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![WhatsupGold](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WhatsupGold.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch devices attributes** - Select this option to fetch additional device attributes from the endpoint [WhatsUp Gold Device\_FindAttributes API](https://docs.ipswitch.com/NM/WhatsUpGold2019_2/02_Guides/rest_api/#operation/Device_FindAttributes).
2. **Fetch devices credentials** - Select this option to fetch device credentials from the endpoint [WhatsUp Gold Device\_Credentials API](https://docs.ipswitch.com/NM/WhatsUpGold2019_2/02_Guides/rest_api/#operation/Device_Credentials).
3. **Fetch devices uptime in the last months** - Enter a number of months to fetch data on the state of the device as well as the uptime of the device's power supply from the endpoint [WhatsUp Gold DeviceReport\_DeviceStateChangeReport API](https://docs.ipswitch.com/NM/WhatsUpGold2019_2/02_Guides/rest_api/#operation/DeviceReport_DeviceStateChangeReport).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [WhatsUp Gold RESTful API (v1)](https://docs.ipswitch.com/NM/WhatsUpGold2019_2/02_Guides/rest_api/).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| v1      | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5