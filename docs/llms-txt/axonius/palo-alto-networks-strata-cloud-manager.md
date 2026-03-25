# Source: https://docs.axonius.com/docs/palo-alto-networks-strata-cloud-manager.md

# Palo Alto Networks Strata Cloud Manager

Strata Cloud Manager is a platform that offers cloud infrastructure management and optimization solutions.

### Asset Types Fetched

* Devices, Aggregated Security Findings, SaaS Applications
  , Network/Firewall Rules

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Client ID/Secret

### APIs

Axonius uses the [Palo Alto Networks Strata Cloud Manager APIs](https://pan.dev/scm/api/config/ngfw/setup/list-devices/).

### Permissions

To retrieve the list of devices via the `GET /config/setup/v1/devices` endpoint, the API token must be tied to a service account with sufficient rights to:

* Access the Configuration Setup service
  * Grants access to NGFW configuration data, including device inventory and connection metadata.
* Read device metadata and inventory details
  * Includes visibility into fields like `id`, `name`, `ip_address`, `hostname`, `model`, and `labels`.
* Query within the appropriate TSG scope
  * Ensures the service account's token is scoped to the tenant(s) whose devices should be fetched.

<br />

#### Supported From Version

Supported from Axonius version 6.1.73

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Palo Alto Networks Strata Cloud Manager server.
2. **Client ID** and **Client Secret**  - The credentials for a user account that has the  Required Permissions to fetch assets. For more information, see [Authentication](https://pan.dev/scm/api/config/ngfw/setup/configuration-setup/#authentication).
3. **Tenant Service Group (TSG) ID** - Enter a scope value of `tsg_id:XXXXXXXXXX`, where `XXXXXXXXXX` is the Tenant Service Group (TSG) ID. Make sure you only enter the Tenant Service Group (TSG) ID itself, and not the prefix tsg\_id:
4. **Token URL** *(default: `https://auth.apps.paloaltonetworks.com/oauth2/access_token`)* - Enter the Token URL.

![PAN\_StrataCloud](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-DLO9555Y.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

### Endpoint Config

This section contains options to fetch specific assets from specific endpoints. Some of the options allow for additional enrichment once enabled.

For example, enable **Fetch Devices of sub type iot\_device from IoT Devices Endpoint** to fetch IoT devices from the **IoT Devices** endpoint. When you enable this, you can also select to **Enrich IoT Devices Endpoint with Vulnerability Instances Endpoint**.

* When you enable **Fetch Firewall of sub type security\_rule from Security Rules**, you can filter the results by Folder Name. Enter folder names to filter the results by.
* When you enable **Fetch Firewall of sub type nat\_rules from NAT Rules**, you can filter the results by Folder Name. Enter folder names to filter the results by. By default this is filtered by *Remote Networks*.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>