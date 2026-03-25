# Source: https://docs.axonius.com/docs/immuniweb.md

# ImmuniWeb

ImmuniWeb develops machine learning and AI technologies providing continuous monitoring for web applications and APIs.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Domains & URLs, Alerts/Incidents

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ImmuniWeb server.

2. **Discovery ID** *(required)* - The unique ID that can be found on the project itself and can be found on the “Discovery Projects” tab after you click on the "create API keys" button.

3. **API Key** and **API Secret** *(required)* - Refer to your ImmuniWeb API documentation for information on how to generate the API Key and the API Secret.

4. **Tab Types** *(optional)* - From the dropdown, select one or more of the following tab types: cloud, domains, incidents, mobileapps, network, repositories, and webapps.

5. **API Version** *(optional, default: Version 1)* - Select the version of the ImmuniWeb API.

6. **Risk Level** *(optional, only used for API Version 2)* - From the dropdown, select the risk level. If selected, only assets with the specified risk level are retrieved.

7. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

8. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

9. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

10. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ImmuniWeb](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ImmuniWeb.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Parse domains tab as Domains and URLs** - Select this option to force parse the domains tab as Domains and URLs and as devices.
2. **Parse domains without IP addresses as domains and URLs only** - Select this option to parse the domains tab as a Domains and URLs entity only.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the ImmuniWeb API.

## Supported From Version

Supported from Axonius version 6.0