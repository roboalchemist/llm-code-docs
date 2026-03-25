# Source: https://docs.axonius.com/docs/black-kite-v2.md

# Black Kite V2

Black Kite is a risk management tool that provides cyber risk intelligence and third-party risk assessment solutions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Aggregated Security Findings
* SaaS Applications
* Domains & URLs

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Black Kite server.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **API Rate Limit (Calls per Minute)** *(default 60)* - Set the the maximum number of API requests the adapter will make to the Black Kite API per minute.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/BlackKiteV2.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Company Names** - Enter a list of company names. The adapter will fetch assets related only to the specified companies. If left blank, the adapter will fetch assets for all companies.
2. **Fetch users from findings** *(default: true)* - By default, the adapter fetches users from findings. Clear this option to not fetch users from findings.
3. **Finding statuses to fetch** - Select one or more statuses to include in the fetch. By default, **Active** is selected. Clear options that you want to exclude from the fetch.
4. **Finding severities to fetch** - Select one or more severities to include in the fetch. By default, **Low**, **Medium**, **High**, and **Critical** are selected. Clear options that you want to exclude from the fetch.

<Callout icon="📘" theme="info">
  Note

  At least one of the options in each of the dropdowns must be selected.
</Callout>

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Black Kite API](https://app.blackkitetech.com/ApiDocs/v2/swagger/#/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Supported From Version

Supported from Axonius version 6.1.39.0