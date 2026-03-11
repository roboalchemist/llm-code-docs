# Source: https://docs.axonius.com/docs/bmc-footprints.md

# BMC FootPrints

BMC FootPrints is an IT service management solution that offers comprehensive service desk capabilities.

### Asset Types Fetched

* Tickets

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses BMC FootPrints Service Core Web Services.

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

#### Supported From Version

Supported from Axonius version 8.0.3

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the BMC FootPrints server.

2. **User Name** and **Password**  - The credentials for a user account that has the  Required Permissions to fetch assets.

<Image alt="BMC FootPrints connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/BMC_FootPrints_AddConnection.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Search IDs - applies context on the following endpoints: Run Search By ID**
  * **Custom Search IDs** *(optional)* - Enter a list of custom search IDs.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Related Enforcement Actions

* [Create BMC FootPrints Ticket](https://docs.axonius.com/axonius-help-docs/docs/create-bmc-footprints-ticket)
* [Link BMC FootPrints Ticket](https://docs.axonius.com/axonius-help-docs/docs/link-bmc-footprints-ticket)
* [Update BMC Footprints Ticket](https://docs.axonius.com/axonius-help-docs/docs/update-bmc-footprints-ticket)