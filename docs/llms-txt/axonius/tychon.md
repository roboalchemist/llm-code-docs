# Source: https://docs.axonius.com/docs/tychon.md

# TYCHON

TYCHON is an endpoint analytics and remediation platform that allows users to search, visualize, remediate, and monitor security compliance across assets.

## Types of Assets Fetched

* Devices
  , Aggregated Security Findings
  , SaaS Applications, Software, SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the TYCHON server.
2. **Port** *(required, default: 9200)* - The port used for the connection.
3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **API Key** is required.
</Callout>

4. **API Key ID** and **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **API Key** is not supplied, **User Name** and **Password** are required.
</Callout>

5. **Assets Index** *(optional, default: tychon\_internal\_assets)* - Enter one or more comma-separated indexes of devices to fetch.
6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Tychon" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Tychon.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Vulnerabilities Index** *(optional, default: tychon\_audits)* - Enter one or more comma-separated indexes of vulnerabilities to fetch. Wildcard (\*) expressions are supported.
2. **Software Index** *(optional, default: tychon\_tasks\_software)* - Enter one or more comma-separated indexes of software to fetch. Wildcard (\*) expressions are supported.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Elasticsearch REST APIs](https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html).

## Supported From Version

Supported from Axonius version 4.7