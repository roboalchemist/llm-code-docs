# Source: https://docs.axonius.com/docs/appspace.md

# Appspace

Appspace is a collaboration platform that provides digital signage and workplace experience solutions.

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the the following APIs:

* [RetrieveUsers](https://app9.cloud.appspace.com/docs/Home/ServiceContent?serviceName=UserService\&operationName=RetrieveUsers)
* [RetrieveDevices](https://app9.cloud.appspace.com/docs/Home/ServiceContent?serviceName=DeviceService\&operationName=RetrieveDevices)

### Permissions

The following roles are required:

* Portal Administrator

* Account Administrator

* Account Owner

* Network Administrator

#### Supported From Version

Supported from Axonius version 6.1.67

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Appspace server.
2. **User Name** and **Password**  - The credentials for a user account that has the  Required Permissions to fetch assets.

![Appspace.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Appspace.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).