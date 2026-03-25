# Source: https://docs.axonius.com/docs/betterstack-uptime.md

# Better Stack Uptime

Better Stack Uptime is a monitoring solution that provides real-time alerts and incident management for website and service availability.

### Asset Types Fetched

* Domains & URLs, Application Services

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* API Token

### APIs

Axonius uses the following APIs:

* [List monitors](https://betterstack.com/docs/uptime/api/list-all-existing-monitors/)
* [Monitor availability](https://betterstack.com/docs/uptime/api/get-a-monitors-availability-summary/)
* [List heartbeats](https://betterstack.com/docs/uptime/api/list-all-existing-hearbeats/)
* [Get a heartbeat's availability summary](https://betterstack.com/docs/uptime/api/get-a-heartbeats-availability-summary/)

### Permissions

API access to both `/monitors` and `/heartbeats` and their `/availability_summary` endpoints is gated only by a valid Bearer API token.

The token must belong to a user or service account that has read access to the workspace/team where those monitors or heartbeats exist.

#### Supported From Version

Supported from Axonius version 6.1.71

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Better Stack Uptime server.
2. **Token**  - An API Token associated with a user account that has the Required Permissions to fetch assets. For information on how to obtain an API Token, see [Get an API token](https://betterstack.com/docs/uptime/api/getting-started-with-uptime-api/).

![Better Stack Uptime.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Better%20Stack%20Uptime.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).