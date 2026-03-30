# Source: https://docs.axonius.com/docs/trend-micro-cloud-app-security.md

# Trend Micro Cloud App Security

Trend Micro Cloud App Security provides threat and data protection for cloud applications and services such as Google G Suite, Dropbox, Microsoft 365, and more.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Trend Micro Cloud App Security server.

2. **API Token** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Fetch logs from the last X hours (max. 72)** *(required, default: 3)* - Specify the number of last hours logs data should be fetch.
   * The maximum number of hours supported is 72.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1502\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Async chunks in parallel** *(required, default: 50)* - Specify the number of parallel requests all connections for this adapter will send to the Trend Micro Cloud App Security server in parallel at any given point.

<Callout icon="📘" theme="info">
  NOTE

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Trend Micro Cloud App Security - Get Security Logs API](https://docs.trendmicro.com/en-us/enterprise/cloud-app-security-integration-api-online-help/supported-cloud-app-_001/log-retrieval-api/get-security-logs.aspx).

## Required Permissions

The value supplied in [API Token](#parameters) must have read access to users.
To generate an Authentication Token, see [Getting Started with Cloud App Security APIs - Generating an Authentication Token](https://docs.trendmicro.com/en-us/enterprise/cloud-app-security-integration-api-online-help/getting-started-with/generating-an-authen.aspx).