# Source: https://docs.axonius.com/docs/citrix-adm-nitro.md

# Citrix Application Delivery Management (ADM)

Citrix Application Delivery Management (ADM) is a platform enabling automation, orchestration, management, and analytics across hybrid multi-cloud environments.

The Citrix ADM adapter enables Axonius to fetch and catalog application delivery assets, including load balancers and service records, ensuring comprehensive visibility into network traffic management and infrastructure dependencies.

## Asset Types Fetched

* Devices
* Load Balancers

## Before You Begin

### Required Ports

* TCP port 80/443

### Authentication Methods

* User Name/Password for Cloud
* Client ID/Client Secret for on-premises

### APIs

Axonius uses the following APIs to retrieve asset data:

* <Anchor label="ADM NITRO API" target="_blank" href="https://developer-docs.netscaler.com/en-us/citrix-adm-nitro-api-reference/">ADM NITRO API</Anchor>
* <Anchor label="Citrix Cloud API" target="_blank" href="https://developer-docs.citrix.com/en-us/citrix-cloud/citrix-cloud-api-overview/get-started-with-citrix-cloud-apis/">Citrix Cloud API</Anchor>

### Required Permissions

The user account used for the connection must have permissions to access the Nitro API and view asset data.

### Supported from Version

This adapter is supported from Axonius version 6.1.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Citrix Application Delivery Management (ADM) server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** - The credentials for a user account that has permission to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **Token Authentication** is not supplied, **User Name** and **Password** are required.
</Callout>

3. **Use Token Authentication** - Enable this option to use Token Authentication. If enabled, then Client ID, Client Secret, and Customer ID are displayed.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **Token Authentication** is required.
</Callout>

* **Client ID** and **Client Secret** - The Client ID and Client Secret used to authenticate the request.
  * **Customer ID** - The customer ID for a user account provided by Citrix Application Delivery Management (ADM) that has the permissions to fetch assets.

<Image alt="Citrix ADM" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Citrix%20ADM.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

* **Fetch Devices of sub type ns\_service from NS LB Service Records** - Enable this option to fetch load balancer service records as Devices.
* **Fetch LoadBalancers from NS LBVServer** - Enable this option to fetch Load Balancer data with <Anchor label="ns_lbvserver" target="_blank" href="https://developer-docs.netscaler.com/en-us/citrix-adm-nitro-api-reference/configuration/network-functions/loadbalancing/ns_lbvserver">ns\_lbvserver</Anchor>.
* **Enrich NS LBVServer-Service Bindings with NS LB Service Records** - Select this option to enrich fetched Load Balancer Virtual Servers (NS LBVServer) with details from their bound service records (NS LB Service Records).