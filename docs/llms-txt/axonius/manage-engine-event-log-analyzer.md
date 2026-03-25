# Source: https://docs.axonius.com/docs/manage-engine-event-log-analyzer.md

# ManageEngine EventLog Analyzer

ManageEngine EventLog Analyzer is a web-based SIEM solution that provides real-time log monitoring, threat detection, compliance reporting, and forensic analysis across diverse IT environments.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

The EventLog Analyzer REST API uses API key-based authentication.

* To generate an API Key, go to:
  Settings → Admin Settings → API Settings → Generate API Key
* The API key must be included as a query parameter in every request:
  `apiKey=<YOUR_API_KEY>`

### APIs

Axonius uses the [Eventlog Analyzer REST APIs](https://www.manageengine.com/products/eventlog/help/StandaloneManagedServer-UserGuide/AdminSettings/get-log-sources.html).

### Permissions

Users must have Administrator privileges to generate the API key and access these API endpoints.

These permissions are governed via the EventLog Analyzer's role-based access control (RBAC) within the Admin Settings panel.

#### Supported From Version

Supported from Axonius version 7.0.5

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the ManageEngine EventLog Analyzer server.
2. **API Key**  - An API Key associated with a user account that has the  Required Permissions to fetch assets.

<Image alt="ManageEngine EventLog Analyzer.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageEngine%20EventLog%20Analyzer.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).