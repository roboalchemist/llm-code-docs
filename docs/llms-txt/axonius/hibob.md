# Source: https://docs.axonius.com/docs/hibob.md

# Hibob

Hibob HR is a human resources management platform that provides onboarding, employee management, engagement tools, and more.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* User Name/Password for Cloud
* API Token for on-prem

### APIs

Axonius uses the [Bob API](https://apidocs.hibob.com/reference).

### Permissions

The value supplied in [API Token](#required-parameters) must be associated with credentials that have View People report permissions.

#### Supported From Version

Supported from Axonius version 4.5

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The API URL of the Hibob server that Axonius can communicate with via the Required Ports. The default value is [https://api.hibob.com/api](https://api.hibob.com/api)"
2. **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **API Token** is not supplied, **User Name** and **Password** are required.
</Callout>

3. **API Token** - An API Token associated with a user account that has the Required Permissions to fetch assets. Refer to [Generating the API Token](https://apidocs.hibob.com/docs/getting-started) for information about how to generate the API Token.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **API Token** is required.
</Callout>

![Hibob.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Hibob.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Lifecycle History** - Select this option to fetch employee lifecycle history.
2. **Fetch Inactive Users** - Select this option to fetch inactive users.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>