# Source: https://docs.axonius.com/docs/trendmicro-vision-one.md

# Trend Micro Vision One

Trend Micro Vision One is a threat defense platform that provides advanced extended detection and response (XDR) capabilities.

The Trend Micro Vision One adapter enables Axonius to fetch and catalog endpoints, identities, and software inventory, providing unified visibility into their inventory details and security posture.

## Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Vulnerabilities.svg) Aggregated Security Settings | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg) Software | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications

## Before You Begin

### Required Ports

* TCP port 443 (HTTPS)

### Authentication Methods

* Token

### Required Permissions

The value supplied in [User API Token](#required-parameters) must be associated with credentials that have the following permissions:

* **Report Management**
  * View
  * Configure and download

* **Endpoint Inventory**
  * View

### APIs

Axonius uses the [Trend Vision One Public API (v3.0)](https://automation.trendmicro.com/xdr/api-v3#tag/) to retrieve asset data.

### Supported From Version

Supported from Axonius version 4.8.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the the hostname or IP address of the Trend Micro Vision One server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Token** - Enter an API Key associated with a user account that has permissions to fetch assets. Read [here](https://docs.trendmicro.com/en-us/documentation/article/trend-micro-vision-one-automation-center-first-steps-toward-u) about getting the API.

![TrendMicroVisionONe](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TrendMicroVisionONe.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Fetch Device Vulnerabilities** *(default: true)* - By default Axonius fetches device vulnerabilities. Clear this option to not fetch device vulnerabilities.
2. **Fetch Installed Software** *(default: false)* - Select this option to enrich devices with installed software.
3. **Fetch Extended Endpoint Details** *(default: false)* - Select this option to fetch extended endpoint details (including network interfaces (IP addresses and MAC addresses), cloud provider, and cloud ID). All of this data can significantly help with correlation.
4. **Fetch Risky Devices** *(default: true)* - By default, Axonius fetches risky devices. Clear this option to disable the risky devices endpoint.
5. **Fetch Users** *(default: false)* - Select this option to fetch users.
6. **Fetch last logon** *(default: false)* - Select this option to enrich device data with the most recent logon event timestamp.
7. **Fetch MITRE ATT\&CK Techniques** *(default: false)* - Select this option to enrich fetched devices with adversary behaviors and techniques mapped to the MITRE ATT\&CK framework.
8. **Fetch Processes**  - Select this option to enrich devices with Processes.
9. **Fetch Scheduled Tasks**  - Select this option to enrich devices with scheduled tasks.
10. **Fetch DLL/Module Loads**  - Select this option to enrich devices with recently loaded modules.
11. **Fetch Recent Executables** - Select this option to enrich devices with 'Recent Executables'.
12. **Page Size** *(default: 200)* - Specify the number of entities returned per page request.