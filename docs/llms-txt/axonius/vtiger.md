# Source: https://docs.axonius.com/docs/vtiger.md

# Vtiger CRM

Vtiger CRM is a customer relationship management tool that provides unified sales, marketing, support, automation, analytics and contact management.

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* CRM Username and Access Key

### APIs

Axonius uses the [Vtiger REST API](https://vtap.vtiger.com/platform/rest-apis.html).

### Permissions

* **Authentication**:
  * Uses HTTP Basic Auth with `USERNAME:ACCESS_KEY`.
  * The Access Key can be found under **My Preferences** in the CRM.

* **Base URL format**:
  `https://yourdomain.com/restapi/v1/vtiger/default`

* User must have profile permissions (Retrieve/Query) for the target module.

* Access is limited to records owned or shared with the user (unless they are an admin).

* Module names must be spelled exactly (e.g., 'Contacts', not 'Contact').

#### Supported From Version

Supported from Axonius version 7.0.6

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Vtiger instance host URL or IP address** - The hostname or IP address of the Vtiger CRM server.
2. **CRM Username** - The credentials for a user account that has the Required Permissions to fetch assets.
3. **Access Key** - An Access Key associated with a user account that has the Required Permissions to fetch assets.

![Vtiger CRM.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vtiger%20CRM.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).