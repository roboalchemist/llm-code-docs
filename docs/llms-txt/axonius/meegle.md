# Source: https://docs.axonius.com/docs/meegle.md

# Meegle

Meegle is a platform that offers digital marketing and reputation management services.

### Asset Types Fetched

* Users, Tickets

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Plugin ID/Plugin Secret

### APIs

Axonius uses the following APIs:

* [Get Tenant User List](https://meegle.com/b/helpcenter/developer/get-tenant-user-list)
* [Get the Specified Work Item List (Across Space)](https://meegle.com/b/helpcenter/developer/get-work-item-across-space)

### Permissions

The Plugin ID/Plugin Secret must be granted the appropriate permissions to make the API calls listed.

#### Supported From Version

Supported from Axonius version 6.1.68

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Meegle server.
2. **Plugin ID** and **Plugin Secret**  - The credentials associated with a user account that has the permissions to fetch assets. For more information, see [Obtain a plugin access token](https://meegle.com/b/helpcenter/developer/plugin-access-token-obtain-a-plugin-access-token).

![Meegle.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Meegle.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).