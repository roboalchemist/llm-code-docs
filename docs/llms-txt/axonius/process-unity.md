# Source: https://docs.axonius.com/docs/process-unity.md

# ProcessUnity

ProcessUnity is a risk and compliance management platform that provides workflows and automation to assess, monitor and mitigate third-party and enterprise risks.

### Asset Types Fetched

* Alerts/Incidents

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses ProcessUnity's External API Connections.

### Permissions

The following permissions are required:

* Admin access is required to configure and view External API Connections.

* Specific workflow actions (like “Get from External API”) must be manually enabled via UI.

#### Supported From Version

Supported from Axonius version 7.0.2

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the ProcessUnity server.
2. **Web Service User Name** and **Web Service Password**  - The credentials for the Web Service user account that has the Required Permissions to fetch assets.
3. **Process Unity User Name** and **Process Unity Password**  - The credentials for the ProcessUnity user account that has the Required Permissions to fetch assets.
4. **Process Unity Instance** - The name of your instance for ProcessUnity.
5. **Process Unity Report ID List** - A list of IDs of the Reports that the adapter fetches from.

![ProcessUnity.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ProcessUnity.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).