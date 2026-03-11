# Source: https://docs.axonius.com/docs/pulse-connect-secure.md

# Ivanti Connect Secure

Ivanti Connect Secure provides zero trust secured access from any device to applications and services in the cloud and data center.

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password for Cloud
* API Key for on-prem

### APIs

Axonius uses the [Pulse Connect Secure REST API](https://help.ivanti.com/ps/legacy/PCS/9.1Rx/9.1R7/9.1R7-PCS_PPS-REST-API-Solutions-Guide.pdf).

### Permissions

The value supplied in [User Name](#required-parameters) must have access to the API.
REST API authentication is successful only for those users who have access to the API.

**To enable access to the API**

1. Go to **Authentication** `>` **Auth. Servers** `>` **Administrators** `>` **Update Administrator admin1**.
2. Select **Allow access to REST APIs**.
3. Click  **Save Changes**.

   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1453\).png)

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Pulse Connect Secure server.
2. **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **API Key** is not supplied, **User Name** and **Password** are required.
</Callout>

3. **API Key** - An API Key associated with a user account that has the Required Permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **API Key** is required.
</Callout>

<Image alt="IvantiConnectSecure" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IvantiConnectSecure.png" />

### Optional Parameters

1. **Add specific Prefix for URL** - Enter a prefix to add to the host URL.

2. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-amp-ca-settings).

3. **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

4. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Devices** *(default: true)* - By default this adapter fetches devices. Disable this option to not fetch devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>