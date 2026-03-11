# Source: https://docs.axonius.com/docs/xensam-xupervisor.md

# Xensam Xupervisor

Xensam Xupervisor is a software asset management tool that provides real-time visibility and control over software usage and licenses.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* User Name/Password
* API Key

### APIs

Axonius uses the Xupervisor API.

### Permissions

Xensam provides viewer access. For more information about permissions, see [Xupervisor API Guide - Requirements](https://wiki.xensam.com/s/73d58956-264b-4c44-94a0-297035386672/doc/xupervisor-api-guide-iQ3DkT5dlF#h-2-requirements).

#### Supported From Version

Supported from Axonius version 6.1.67

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Xensam Xupervisor server.
2. **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.
3. **API Key** - An API Key associated with a user account that has the Required Permissions to fetch assets.

![Xensam Xupervisor.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Xensam%20Xupervisor.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).