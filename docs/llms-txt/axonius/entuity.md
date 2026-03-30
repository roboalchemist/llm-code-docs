# Source: https://docs.axonius.com/docs/entuity.md

# Entuity

Entuity is a network management tool that offers comprehensive monitoring and analysis capabilities.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the [Entuity RESTful API](https://support.entuity.com/hc/en-us/articles/360006535413-Introduction-to-Entuity-RESTful-API).

### Permissions

To interact with the Entuity Device Inventory API (`/api/inventory`), the API token or user credentials must be associated with an account that has sufficient rights to:

* Access the Asset Management or Device Inventory feature within Entuity
* View the list of devices, including their metadata and management state

If the account does not have the appropriate RBAC (Role-Based Access Control) permissions, API requests will return partial or no data, or result in HTTP `403 Forbidden` errors.

#### Supported From Version

Supported from Axonius version 7.0.3

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Entuity server.
2. **User Name** and **Password**  - The credentials for a user account that has the Required Permissions to fetch assets.

![Entuity.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Entuity.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).