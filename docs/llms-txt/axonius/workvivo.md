# Source: https://docs.axonius.com/docs/workvivo.md

# Workvivo

Workvivo is an employee experience platform that provides internal communication, engagement analytics, recognition, and API-based integrations.

### Asset Types Fetched

* Users, Groups

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Token

### APIs

Axonius uses the [Workvivo API](https://developer.workvivo.com/#intro).

### Permissions

* Requires Developer role to access the Developer Apps portal.
* Must register an app via [https://workvivo.com/admin/developers/apps/manage](https://workvivo.com/admin/developers/apps/manage).

#### Supported From Version

Supported from Axonius version 7.0.10

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Workvivo server.
2. **Organization ID** - Specify your Workvivo organization ID.
3. **API Token**  - An API Token associated with a user account that has the  Required Permissions to fetch assets.

![Workvivo.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Workvivo.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).