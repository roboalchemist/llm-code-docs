# Source: https://docs.axonius.com/docs/bigid.md

# BigID

BigID is data security solution that provides enterprise protection and privacy of personal data.

The BigID adapter enables Axonius to fetch and catalog data sources, providing visibility into their classification, privacy attributes, and compliance status.

## Asset Types Fetched

* Devices

## Before you begin

### Required Ports

* TCP Port 443 (HTTPS)

### Required Permissions

The BigID adapter requires a **User** or **API Token** with **Read-Only** permissions to the assets you intend to fetch.

The account must have the ability to:

* **Read Catalog** - Retrieve data objects, tables, and files from the inventory.
* **Read Data Sources** - Access details about connected data sources and their classifiers.
* **Read Attributes and Tags** - Fetch metadata, including privacy attributes and tags associated with assets.
* **Read Cases** - Retrieve details of open remediation or privacy cases.

### APIs

Axonius uses the <Anchor label="BigID REST API" target="_blank" href="https://developer.bigid.com/wiki/BigID_API">BigID REST API</Anchor> to retrieve asset data.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **BigID Domain** - Enter the hostname or IP address of the BigID server.
2. **User Name** and **Password** - Enter the credentials for a user account that has the permissions to fetch assets.
3. **API  Token** - Enter the API Token to use for authentication. Refer to <Anchor label="BigID API/API Tutorial" target="_blank" href="https://developer.bigid.com/wiki/BigID_API/API_Tutorial">BigID API/API Tutorial</Anchor> for details about generating the API Token.

<Callout icon="📘" theme="info">
  Note

  * When **User Name** and **Password** are not supplied, **API Token** is required.
  * When **API Token** is not supplied, **User Name** and **Password** are required.
  * If you supply both an API token and a username and password, the system will use the username and password for authentication.
</Callout>

<Image alt="BigID new.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BigID%20new.png" />

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

1. **Fetch Catalog Data** *(default: true)* – Select this option to fetch catalog items as assets. This is the primary setting to retrieve data inventory from BigID. If you do not select this option, the catalog data is not fetched.
2. **Fetch attributes list** – Select this option to retrieve the list of attributes associated with the catalog items.
3. **Fetch tags list** – Select this option to retrieve the tags associated with the fetched assets.
4. **Fetch datasources classifiers count** – Select this option to fetch the total count of classifiers identified for each data source.
5. **Use RDB URL as Hostname** – Select this option to use the Relational Database (RDB) URL as the hostname for the device, instead of the default name.
6. **Fetch Open Cases** – Select this option to fetch details regarding open remediation or privacy cases that are managed within BigID.