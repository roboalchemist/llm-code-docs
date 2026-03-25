# Source: https://docs.axonius.com/docs/forticlient-ems.md

# FortiClient EMS

FortiClient Enterprise Management Server (FortiClient EMS) is a security management solution that enables scalable and centralized management of multiple endpoints.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the FortiClient EMS server.

2. **Auth Method** - Select an Authentication method, either **On Premise** (default) or **Cloud**.
   * **On Premise**: **User Name** and **Password** - The credentials for a user account that has the permissions to fetch assets.
   * **Cloud**: **Access Key** and **Account Email** - The credentials for the **Access Key** and **Account Email** that have the required permissions to fetch assets.

3. **Version** *(optional, default 6.2)* - The API version, either 6.2 or 6.4 or higher.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![FortiClient EMS](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FortiClient%20EMS.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Do not fetch devices without Last Seen** *(required, default: True)* - Select whether to fetch devices that do not have the 'Last Seen' attribute.
   * When enabled, all connections for this adapter will not fetch devices that do not have the  'Last Seen' attribute.
   * When disabled, all connections for this adapter will fetch all devices.
2. **Fetch software information** *(optional, default: False)* - Select to fetch software information together with the devices. Note that a license is required in order to enable this setting.

<Callout icon="📘" theme="info">
  Note

  For details about general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [FortiClient EMS API](https://fndn.fortinet.net/index.php?/fortiapi/48-forticlient-ems/).

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions.  Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed which is not functioning as expected.

| Version                             | Supported | Notes |
| ----------------------------------- | --------- | ----- |
| FortiClient EMS  6.2, 6.4 or higher | Yes       | ---   |