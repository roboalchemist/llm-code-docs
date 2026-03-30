# Source: https://docs.axonius.com/docs/sap-ariba.md

# SAP Ariba

SAP Ariba is a cloud-based procurement, spend management, and supply chain services solution.

### Asset Types Fetched

* Users, Groups

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key / Realm Name / Client Secret

### APIs

Axonius uses the [SAP Ariba APIs](https://api.sap.com/api/mds_search/path/get_entities__entityName_).

### Permissions

Consult with your vendor for permissions for reading the objects.

#### Supported From Version

Supported from Axonius version 6.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **API Domain** *(default: `https://openapi.ariba.com/api/mds-search/v1/prod`)* - The API Access URL address provided as part of the API Token Summary.
2. **API Key** - An API Key associated with a user account that has permissions to fetch assets.
3. **Realm Name** - The Realm Name for which the information has to be fetched. The Realm Name should be the authorized realm via application/OAuth Client configured in gateway.
4. **Client Secret** - The Client Secret for an account that has read access to the API.

![SAP%20Ariba](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAP%20Ariba.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Groups from Find all groups (from Master Data)** - Enable this option to fetch groups from the Master Data Retrieval API.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>