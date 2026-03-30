# Source: https://docs.axonius.com/docs/f5-distributed-cloud.md

# F5 Distributed Cloud

F5 Distributed Cloud is a cloud-based security and application management platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the F5 Distributed Cloud server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Namespace** *(required)* - Specify the Namespace of the F5 Distributed Cloud server.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="F5 Distributed Cloud" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/F5%20Distributed%20Cloud.png" />

## APIs

Axonius uses the [F5 Distributed Cloud Services API](https://docs.cloud.f5.com/docs/api).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Enrich Firewalls with Firewall Details** and **Enrich Load Balancers with Load Balancer Details** - Enable these settings to enrich those assets with additional data about their possible public exposure to the internet.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Supported From Version

Supported from Axonius version 6.1.30.0