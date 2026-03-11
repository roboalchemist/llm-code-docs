# Source: https://docs.axonius.com/docs/zscaler-zcc.md

# Zscaler Client Connector

Zscaler Client Connector enables secure access to business applications from any device.

## Asset Types Fetched

* Devices, Application Settings

## Before You Begin

### APIs

Axonius uses the [Zscaler Client Connector API](https://help.zscaler.com/client-connector/getting-started-client-connector-api).

### Authentication Methods

* API Key Authentication
* OneAPI (OAuth)Authentication

<Callout icon="📘" theme="info">
  **Note**

  For optimal fetch of Application Settings, it is recommended to use OneAPI (OAuth)Authentication.
</Callout>

### Required Permissions

When using API Key authentication, the **API Key** must be associated with credentials that have read permissions.

## Connecting the Adapter in Axonius

### Required Parameters

1. **Host Name or IP Address** *(required, default: `https://api-mobile.zscaler.net/`)* - The hostname or IP address of the Zscaler Client Connector server.

2. **Auth Method** - Select between API Key and OneAPI (OAuth).

### Required Parameters - API Key Authentication

1. **API Key** and **Secret Key** - The required credentials to get access to the Client Connector API. For information on adding a new API Key, see [Adding an API Key](https://help.zscaler.com/client-connector/adding-api-key).

![connect with api key](https://files.readme.io/3ecf58304d74f2b1d391eca1a54f9430bffb7c345e73f5957d6784242caf4f73-image.png)

### Required Parameters - OneAPI (OAuth)Authentication

1. **Client ID** and **Client Secret** - The client credentials sent in the request that were verified by ZIdentity, using the client registration details configured in the ZIdentity Admin Portal. See [OAuth 2.0 Client Registration](https://www.rfc-editor.org/rfc/rfc6749#section-2) for more details on the creation and syntax of these parameters.
2. **Vanity Domain** - The domain name used by your organization. Make sure you only add the "domain organization".  For more information, see the 'Accessing OneAPI' section in the [ Zscaler Getting Started with OneAPI docs](https://help.zscaler.com/oneapi/getting-started).

![connect with oauth](https://files.readme.io/b3f0e0d49035eab0d27525f8c62aa5b61c062d2bae536f514ceb85de849dbfc5-image.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Ignore duplicated MAC addresses** - Select this option to ignore MAC addresses that are associated with more than one device fetched from Zscaler.
* **Avoid hostnames duplications** - Select this option to avoid returning duplicate hostname fetches.
* **Add last used users information for duplicated devices** - Select this option to add the last used users information for duplicated devices. This is applicable only when “Avoid hostnames duplications” is used.
* **Fetch registered device details** - Select this to fetch additional device details, including service status fields. Specifically fields regarding the service status of other Zscaler agents/products: ZDX, ZIA, ZPA and Zscaler Deception.\
  Note: Enabling this setting may considerably increase fetch duration due to Zscaler’s strict 100 requests-per-hour API rate limit.
* **RateLimit (requests/hour)** *(optional, default: 95)* - Enter the maximum rate of requests per hour by Axonius to the Zscaler server.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Supported From Version

Supported from Axonius version 6.0