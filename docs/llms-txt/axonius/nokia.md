# Source: https://docs.axonius.com/docs/nokia.md

# Nokia Network Services Platform (NSP)

Nokia Network Services Platform (NSP) is a network automation and management system that provides centralized control, provisioning, and monitoring of IP and optical networks.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the Nokia NSP API.

### Permissions

To retrieve network element inventory data from the Nokia NSP API, the API token must be associated with an account that has sufficient rights to:

* Access the “Equipment Inventory” or “Network Element Management” modules
* Use the `nsp-equipment` RESTCONF data model
* Execute `GET` requests against `/restconf/data/nsp-equipment:network/network-element` endpoints
* View sensitive metadata such as device IP addresses, MAC addresses, operational/admin state, and software versions

If the account lacks proper RBAC permissions, the RESTCONF calls may return:

* Empty datasets

* 403 Forbidden or 401 Unauthorized errors

* Truncated fields (e.g., no version, no MAC address)

#### Supported From Version

Supported from Axonius version 6.1.68

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Nokia server.
2. **User Name** and **Password**  - The credentials for a user account that has the Required Permissions to fetch assets.

<Image alt="Nokia NSP.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Nokia%20NSP.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).