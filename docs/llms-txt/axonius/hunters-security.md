# Source: https://docs.axonius.com/docs/hunters-security.md

# Hunters

Hunters is a security platform that offers threat detection and response capabilities.

### Asset Types Fetched

* Alerts/Incidents

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Client ID/Secret

### APIs

Axonius uses the Hunters API.

### Permissions

**Required Permissions and Access**:

* **Access Control Philosophy** - Hunters emphasizes using minimal, tightly scoped access (e.g., read‑only) where possible when setting up API credentials.
* **API token roles** - Assign roles to the API tokens to control which of the platform users can use the API token to gain access to routes using that token. To access Leads & Stories, the API token role of ‘*Customer*’ or higher is needed.

#### Supported From Version

Supported from Axonius version 7.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Hunters server.
2. **Client ID** and **Client Secret** - The credentials for a user account that has the Required Permissions to fetch assets.

![Hunters.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Hunters.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).