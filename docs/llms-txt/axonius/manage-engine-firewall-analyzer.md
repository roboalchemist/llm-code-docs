# Source: https://docs.axonius.com/docs/manage-engine-firewall-analyzer.md

# ManageEngine Firewall Analyzer

ManageEngine Firewall Analyzer is an agentless log analytics and configuration management software that analyzes logs from firewalls and generates real-time alert notifications and security and bandwidth reports.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ManageEngine Firewall Analyzer server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. To create the API Key click 'Generate API Key' under Settings `>` Basic Settings `>` REST API on the vendor’s platform dashboard.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ManageEngineFirewallAnalyzer](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageEngineFirewallAnalyzer.png)

## APIs

Axonius uses the [ManageEngine Firewall Analyzer API](https://www.manageengine.com/products/firewall/help/firewall-analyzer-rest-api.html)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* 80, 443

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have ReadOnly   permissions in order to   fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                               | Supported | Notes |
| ------------------------------------- | --------- | ----- |
| ManageEngine Firewall Analyzer v1.0.0 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.8