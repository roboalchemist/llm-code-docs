# Source: https://docs.axonius.com/docs/cisco-nexus-dashboard.md

# Cisco Nexus Dashboard

Cisco Nexus Dashboard is a platform that offers centralized management and monitoring for network operations.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* User Name and Password

### APIs

Axonius uses the [Cisco Nexus Dashboard API](https://developer.cisco.com/docs/nexus-dashboard/latest/api-reference/).

#### Supported From Version

Supported from Axonius version 6.1.65

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Cisco Nexus Dashboard server.

2. **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets. For information on authorization with these credentials, see [Authorization Using User Credentials and API Token](https://developer.cisco.com/docs/nexus-dashboard/latest/getting-started/#authorization-using-user-credentials-and-api-token).

3. **Authentication Domain** - Specify the name of the authentication domain.

![Cisco Nexus Dashboard.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cisco%20Nexus%20Dashboard.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).