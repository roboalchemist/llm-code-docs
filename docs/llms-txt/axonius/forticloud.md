# Source: https://docs.axonius.com/docs/forticloud.md

# FortiCloud

FortiCloud is a cloud-based platform offering compliance, security and management services for Fortinet solutions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Licenses, SaaS Applications, Network/Firewall Rules

## Parameters

1. **Host Name or IP Address** *(required, default: `https://www.forticloud.com/`)* - The hostname or IP address of the FortiCloud server. You will need to enter one of the following hostnames, depending on your region.

| FortiCloud Region | Hostname                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------ |
| Global            | [https://api.fortigate.forticloud.com/forticloudapi](https://api.fortigate.forticloud.com/forticloudapi)     |
| US                | [https://usapi.fortigate.forticloud.com/forticloudapi](https://usapi.fortigate.forticloud.com/forticloudapi) |
| EU                | [https://euapi.fortigate.forticloud.com/forticloudapi](https://euapi.fortigate.forticloud.com/forticloudapi) |
| Japan             | [https://jpapi.fortigate.forticloud.com/forticloudapi](https://jpapi.fortigate.forticloud.com/forticloudapi) |

2. **Host Name or IP Address for Authentication** *(optional, default: `https://customerapiauth.fortinet.com/`)* - The hostname or IP address of the FortiCloud server needed for authentication.

3. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

4. **Password** *(required)* - The password for a user account that has permission to fetch assets.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![FortiCloud](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FortiCloud.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Firewall of sub type firewall\_v3 from v3 Product Details** - Toggle on this option to fetch the firewall of subtype `firewall_v3` from the v3 product details.
* **Use Asset Management API** - Select this option to use the FortiCare Registration API v3 to fetch all registered Fortinet assets. This fetches hardware inventory data from the Asset Management portal.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [FortiGate Cloud API](https://docs.fortinet.com/document/fortigate-cloud/latest/administration-guide/557024/api-access).

## Supported From Version

Supported from Axonius version 6.1