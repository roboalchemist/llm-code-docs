# Source: https://docs.axonius.com/docs/drata.md

# Drata

Drata is a compliance automation platform that offers continuous monitoring and evidence collection.

### Asset Types Fetched

* Devices, Users, SaaS Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the [Drata API](https://help.drata.com/en/articles/6695964-drata-public-api).

### Permissions

To fetch the data via the Drata API connection, the following permissions are required:

* **For listing vendors**: `(/vendors GET): Vendors: List Vendors`

* **For listing devices**: `(/devices GET): Devices: List Devices`

* **For listing users**: `(/vendors GET): Users: List Users`

#### Supported From Version

Supported from Axonius version 7.0.6

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Drata server.
2. **API Key** - An API Key associated with a user account that has the Required Permissions to fetch assets.

<Image alt="Drata.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Drata.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).