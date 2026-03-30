# Source: https://docs.axonius.com/docs/smarthub-infer.md

# SmartHub INFER

SmartHub INFER is a unified endpoint lifecycle management solution for edge devices that provides visibility, monitoring, asset management, and security.

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the [SmartHub INFER IoT Center Server Rest API](https://inst01.us01.infer.smarthub.ai/openapi/index.html).

### Permissions

* **Permissions** - Only users with the Administrator or Viewer roles can retrieve device and user data through the API.

* **Organization scope** - Access to device and user data through the Smarthub INFER™ API is scoped to the organization associated with the API key or token. If your account has access to multiple organizations, only data from the selected organization will be returned in API responses.

* **Access limitations** - If the API key belongs to a user who does not have permission to view devices or users in a given organization, those resources will not appear in API results. Attempts to access resources outside of the user’s assigned scope may return empty results or access errors.

#### Supported From Version

Supported from Axonius version 7.0.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the SmartHub INFER server.
2. **User Name** and **Password**  - The credentials for a user account that has the Required Permissions to fetch assets.

![SmartHub INFER.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SmartHub%20INFER.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).