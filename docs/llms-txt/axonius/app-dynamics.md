# Source: https://docs.axonius.com/docs/app-dynamics.md

# Cisco AppDynamics

Cisco AppDynamics is an application performance monitoring tool.

### Use Cases the Adapter Solves

* **Detecting Unmanaged Assets**: Identify devices and application components monitored by AppDynamics that may not be present in your inventory.
* **Verifying Coverage**: Ensure that all critical business applications are being actively monitored by cross-referencing AppDynamics data with other infrastructure sources.
* **Analyzing Access**: Gain visibility into user accounts and their associated permissions within the AppDynamics environment to maintain security hygiene.

### Asset Types Fetched

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg" /> Devices

***

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

The AppDynamics adapter uses **OAuth 2.0 authentication** with Client Credentials Grant.

### APIs

Axonius uses the [Cisco AppDynamics API](https://docs.appdynamics.com/display/PRO40/Use+the+AppDynamics+REST+API).

The adapter uses the following REST API endpoints:

| Endpoint                                       | Purpose                                             |
| ---------------------------------------------- | --------------------------------------------------- |
| `/controller/api/oauth/access_token`           | OAuth 2.0 authentication (Client Credentials Grant) |
| `/controller/rest/applications`                | Lists all applications                              |
| `/controller/rest/applications/{id}/nodes`     | Lists nodes (devices) for each application          |
| `/controller/sim/v2/user/machines/keys`        | Lists machine agent keys (optional)                 |
| `/controller/sim/v2/user/machines/{machineId}` | Gets machine agent details (optional)               |

### Permissions

The API Client needs to be assigned roles with the following permissions:

To fetch devices and applications, the API Client needs to be assigned **roles with the following permissions**:

### Minimum Required Permissions

* **View Applications** - To list and access application data
* **View Nodes** - To retrieve node (device) information from applications
* **View Server Infrastructure Monitoring (SIM)** - To access machine agent data (only required if the "Fetch Machine Agent Data" advanced setting is enabled)

#### Supported From Version

Supported from Axonius version 6.0

### Setting Up Cisco AppDynamics to Work with Axonius

## Setup Instructions

### Step 1: Create an API Client

1. Log in to the AppDynamics Controller UI as an **Account Owner** or **Administrator**
2. Navigate to **Settings > Administration > API Clients**
3. Click **+ Create**
4. Enter the following information:
   * **Client Name** - A descriptive name for the API client
   * **Description** - Purpose of this API client
5. Click **Generate Secret** to create the Client Secret (this is a UUID)
6. Set the **Default API-generated Token Expiration** (default is 5 minutes)
7. **Important:** Copy and save the Client Secret immediately - it cannot be retrieved later

### Step 2: Assign Roles with Required Permissions

1. In the API Client creation screen, add roles that have the required permissions:
   * **View Applications**
   * **View Nodes**
   * **View Server Infrastructure Monitoring** (if fetching machine agent data)
2. You can use existing roles or create custom roles with these specific permissions
3. See [Manage Custom Roles for Splunk AppDynamics](https://docs.appdynamics.com/) for details on creating custom roles
4. Click **Save**

***

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Cisco AppDynamics, and click on the adapter tile.\
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Cisco AppDynamics server.
2. **Client ID** and **Client Secret** - The Client ID and Client Secret for an account that has read access to the API. The client ID should be in the format: `clientID@account`.
3. **Connection Label** - A label to help you distinguish between multiple connections for the same adapter. See [Connection label](/docs/adding-a-new-adapter-connection#setting-adapter-connection-parameters).

<Image align="center" alt="Cisco AppDynamics connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/BackBox.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.
5. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />