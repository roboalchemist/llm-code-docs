# Source: https://docs.axonius.com/docs/bishop-fox-adapter.md

# Bishop Fox

Bishop Fox performs offensive security, penetration testing, red teaming, and attack surface management.

### Asset Types Fetched

* Devices, Domains & URLs, Networks

<br />

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key/API Secret

### APIs

Axonius uses the Bishop Fox API.

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

#### Supported From Version

Supported from Axonius version 5.0

<br />

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Bishop Fox API server.

2. **Authentication Domain** *(default: `https://www.bishopfox.auth0.com/`)* - Specify the name of the authentication domain.

3. **API Key** - An API Key associated with a user account that has permissions to fetch assets.

4. **API Secret** - The API Key secret displayed when the API key is created.

5. **Organization ID** - The organization ID of the specific organization the customer wishes to fetch devices from.

6. **API Version** *(default: v1)* - Select the API Version you want to use to connect, either v1 or v5.

<Image alt="BishopFox" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BishopFox.png" />

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**  - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

**Endpoints Config**

This section lists assets types and sub-types that the adapter can fetch from different endpoints. Enable each setting to fetch the specified asset type from the specified endpoint. For example:

* Enable **Fetch Devices of sub type domains from Devices from Domains** to fetch devices of the sub-type 'domains' from the Devices from Domains endpoint.

The following options are available:

* **Fetch Devices of sub type domains from Devices from Domains**
* **Fetch Devices of sub type subdomains from Subdomains**
* **Fetch Devices of sub type targets from Devices from Targets**
* **Fetch Devices of sub type hostname\_services from Hostname Services**
* **Fetch Devices of sub type ipaddress\_services from IP Addresses Services**
* **Fetch Devices of sub type dns\_records from DNS Records**
* **Fetch URLs of sub type domains from URLs from Domains**
* **Fetch URLs of sub type subdomains from Subdomains**
* **Fetch URLs of sub type targets from URLs from Targets**
* **Fetch Networks from Networks**

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>