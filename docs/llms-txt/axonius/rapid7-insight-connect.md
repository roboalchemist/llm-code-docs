# Source: https://docs.axonius.com/docs/rapid7-insight-connect.md

# Rapid7 InsightConnect

Rapid7 InsightConnect is a security orchestration, automation, and response tool that offers streamlined incident response workflows.

### Asset Types Fetched

* Tickets

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* API Key

### APIs

Axonius uses the [Rapid7 InsightConnect API](https://docs.rapid7.com/insightconnect/api/#tag/Jobs/operation/Jobs#List).

### Permissions

To retrieve job data from the InsightConnect (SOAR) API, the API key must be associated with an account that has sufficient rights to:

* Access the InsightConnect (SOAR) product
* View and manage workflow jobs and executions
* Retrieve workflow execution metadata such as job status, owner, and runtime logs

If the account does not have the appropriate RBAC permissions (Role-Based Access Control) or lacks access to InsightConnect, API calls such as GET /connect/v1/jobs or GET /connect/v1/jobs/`{jobId}` will return permission errors (e.g., HTTP 403) or empty responses.

#### Supported From Version

Supported from Axonius version 6.1.68

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: `https://us.api.insight.rapid7.com`)* - The hostname or IP address of the Rapid7 InsightConnect server.
2. **API Key** - An API Key associated with a user account that has the Required Permissions to fetch assets.

![Rapid7 InsightConnect.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Rapid7%20InsightConnect.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).