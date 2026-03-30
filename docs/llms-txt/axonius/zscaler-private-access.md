# Source: https://docs.axonius.com/docs/zscaler-private-access.md

# Zscaler Private Access (ZPA)

Zscaler Private Access (ZPA) is a zero trust network access solution that provides secure remote access to applications.

## Asset Types Fetched

* Devices, SaaS Applications, Network/Firewall Rules

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Zscaler Private Access (ZPA) server that Axonius can communicate with via the [Required Ports](#required-ports).
   * If an organization logs into **ZPA::Zscaler Private Access**, then the hostname of the ZPA API Portal for that organization is `config.private.zscaler.com`.
   * If an organization logs in to **zpatwo.net**, then the hostname of the ZPA API Portal for that organization is `config.zpatwo.net`.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has permissions to fetch assets. For more information about authentication, see [Getting Started](https://help.zscaler.com/zpa/getting-started-zpa-api#Authenticate).

3. **Customer ID** *(required)* - The customer ID for a user account provided by Zscaler that has permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Zscaler Private Access.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Zscaler%20Private%20Access.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

To fetch different asset types from specific endpoints, enable or disable the following options:

1. **Fetch Devices of sub type app\_connector from App Connector Endpoint**
   1. **Fetch Devices of sub type private\_service\_edge from Private Service Edge Endpoint**
   2. **Fetch Devices of sub type cloud\_and\_branch from Cloud and Branch Connector Endpoint**
2. **Fetch DiscoveredSaasApplications from Applications Endpoint**
3. **Enrich App Connector Endpoint with Global Policy Endpoint**
4. **Fetch Devices of sub type private\_service\_edge from Private Service Edge Endpoint**
5. **Fetch Devices of sub type cloud\_and\_branch from Cloud and Branch Connector Endpoint**
6. **Fetch Firewall of sub type access\_policy from Access Policy Rules**
7. **Fetch Firewall of sub type global\_policy from Global Policy Rules**

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Zscaler ZPA API](https://help.zscaler.com/zpa/getting-started-zpa-api).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.56.0