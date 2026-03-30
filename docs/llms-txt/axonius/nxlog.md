# Source: https://docs.axonius.com/docs/nxlog.md

# NXLog

NXLog is a multi-platform log collection and centralization tool designed to gather logs from various sources and route them to central log management systems.

The NXLog adapter enables Axonius to fetch and catalog log collection agents, providing visibility into their operational status and configuration.

## Asset Types Fetched

* Devices

## Data Retrieved through the Adapter

* **Agent Identity** - Hostnames, agent IDs, and platform details.
* **Operational Status** - Connection status (online/offline) and last seen timestamps.
* **Configuration** - Agent versions and operating system information.

## Before You Begin

### Required Ports

* TCP port 443 (HTTPS)

### Authentication Methods

* **Personal Access Token (recommended)** - Used for the new NXLog Platform API. The token is sent as a **Bearer Token** in the authorization header.
* **User Name and Password** - Used for legacy NXLog Manager configurations (basic authentication).

### Required Permissions

The user or token must have permissions to read agent information, specifically the agents or agent info endpoints.

### APIs

Axonius uses the <Anchor label="NXLog Agent Management API" target="_blank" href="https://docs.nxlog.co/api/agent-management/index.html">NXLog Agent Management API</Anchor>.

The following base endpoints are used:

* **New Platform API (token-based)** - `/api/v1/agents`
* **Legacy API (User/Password)** - `/restservice/agentinfo`

### Supported from Version

Supported from Axonius version 6.1.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the NXLog server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Auth Method** - Select the authentication method that matches your environment:
   * **User Name and Password** - Select this for legacy connections.
   * **Personal Access Token** - Select this for the modern NXLog Platform (recommended).

3. **Personal Access Token** - If this authentication method is selected in **Auth Method**, enter the API token generated from the NXLog Platform console.

<Image align="center" alt="NXLog adapter - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/NXLog_Add_Connection.png" className="border" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).