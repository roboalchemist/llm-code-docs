# Source: https://docs.axonius.com/docs/airlock-digital.md

# Airlock Digital

Airlock Digital is an application whitelisting software provider.

## &#x20;Asset Types Fetched

Devices, Groups

## Before You Begin

**Ports**

Port 3129 is used.

### APIs

* Axonius uses the Airlock Digital REST API version 4.6.
* Get the API Token from the web.
* API keys are available under the user settings in the web-gui.

### Required Permissions

The user must have the generate\_apikey permission to create an API key. Refer to Airlock Digital documentation for information about any permissions relevant to fetching assets.

#### Supported From Version

Supported from Axonius version 4.4

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Airlock Digital server.

2. **Cloud Authentication** - Toggle on to enable cloud authentication.
   * **Directory ID** - The Airlock Digital directory ID associated with a user account that has permissions to fetch assets.
   * **Tenant ID** - The Airlock Digital tenant ID.

3. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

4. **Port** *(required, default: 3129)* - The port used for the connection.

![Airlock Digital](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/AirLockDigital.png)

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch group policies** - Select this option to fetch information about group policies.
* **Parse Observable IP** *(default =True)* - By default, Axonius parses the Observable IP field. Clear this option to not parse the Observable IP field and only parse the Local IP field.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                     | Supported | Notes |
| --------------------------- | --------- | ----- |
| Airlock Digital version 1.0 | Yes       |       |

<br />

## Related Enforcement Actions

* [Airlock Digital - Move Agent to Group](https://docs.axonius.com/axonius-help-docs/docs/airlock-digital-move-agent-to-group)