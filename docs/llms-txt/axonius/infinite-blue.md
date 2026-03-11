# Source: https://docs.axonius.com/docs/infinite-blue.md

# Infinite Blue

Infinite Blue is a business continuity and disaster recovery platform that offers planning and management solutions.

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* User Name/Password
* API Key

### APIs

Axonius uses the [Infinite Blue Platform REST v2.0 API](https://documentation.infiniteblue.com/Resources/AdditionalFiles/RESTv2.html#tag/Record/operation/getRecordsCount).

### Permissions

The following permissions are required:

* View permissions for all Objects ([Setting permissions by role](https://documentation.infiniteblue.com/platform/Setting_permissions_by_role.htm))

#### Supported From Version

Supported from Axonius version 6.1.66

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Infinite Blue server.
2. **Authentication Method** *(required)* - Select Authentication method, either **Basic Authentication** (default) or **API Key Authentication**.
   * **Basic Authentication**
     * **User Name** and **Password** - The credentials for a user account that has permissions to fetch assets.
   * **API Key Authentication**
     * **API Key** - An API Key associated with a user account that has permissions to fetch assets.

![Infinite Blue.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Infinite%20Blue.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).