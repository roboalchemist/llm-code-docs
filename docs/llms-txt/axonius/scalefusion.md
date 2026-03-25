# Source: https://docs.axonius.com/docs/scalefusion.md

# Scalefusion

Scalefusion is a tool that offers mobile device management solutions for securing and managing endpoints.

### Asset Types Fetched

* Devices, Users, Software, SaaS Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the [Scalefusion Developer API](https://help.scalefusion.com/v1/docs/scalefusion-developer-api).

### Permissions

To use the Scalefusion API for device, app, and user data, the API token must be linked to an account with:

* Access to the Developer API
* Read permissions for Devices, Device Apps, and User Management

Without proper RBAC permissions, API responses may be incomplete or return permission errors.

**Recommended Steps**:

* Enable Developer API in the dashboard and generate an API key.
* Ensure the account has at least read access to:
  * **Devices** – for `GET /api/v2/devices.json`
  * **Device Apps** – for `GET /api/v2/devices/device_apps/installed_apps.json`
  * **Organization Users** – for `GET /api/v1/user_management/organization_users.json`
* Use a built-in role (e.g., Device Admin) or create a custom role with the required access.

#### Supported From Version

Supported from Axonius version 7.0.7

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Scalefusion Domain** *(default: `https://api.scalefusion.com/`)* - The hostname or IP address of the Scalefusion server.
2. **API Key** - An API Key associated with a user account that has the  Required Permissions to fetch assets.

![Scalefusion.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Scalefusion.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).