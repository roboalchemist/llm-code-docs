# Source: https://docs.axonius.com/docs/red-hat-insights.md

# Red Hat Insights

Red Hat Insights is a managed service for the automated discovery and remediation of issues in Red Hat products.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Aggregated Security Findings
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Red Hat Insights server.

2. **Auth Method** - Select an Authentication method, either **API Key** (default) or **Client ID and Secret**.
   * **API Key** - An API Key associated with a user account that has permissions to fetch assets.
   * **Client ID** and **Client Secret** - The credentials for a user account that has  permission to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="RedHatInishts" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RedHatInishts.png" />

## APIs

Axonius uses the [Red Hat Inisights API](https://developers.redhat.com/cheat-sheets/red-hat-insights-api-cheat-sheet).

## Supported From Version

Supported from Axonius version 5.0