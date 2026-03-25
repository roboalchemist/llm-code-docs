# Source: https://docs.axonius.com/docs/ns1.md

# NS1

NS1 is a DNS solution for advanced traffic routing, automation, and application resiliency.

### Asset Types Fetched

* ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Network_Services.svg) Network Services |

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

API Key

### APIs

Axonius uses the [NS1 API Documentation](https://ns1.com/api?docId=2184).

### Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have Read permissions to fetch assets.

#### Supported From Version

Supported from Axonius version 4.8

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: `https://api.nsone.net`)* - The hostname or IP address of the NS1 server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key**  - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Image alt="NS1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NS1.png" />

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**  - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

* **Record Types to fetch** - Select the specific DNS record types (such as `A, AAAA,` or `CNAME`) that you want Axonius to fetch. By default all record types are fetched, remove record types from the list to filter those you do not want to fetch.