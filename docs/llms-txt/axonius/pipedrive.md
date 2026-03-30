# Source: https://docs.axonius.com/docs/pipedrive.md

# Pipedrive

Pipedrive is a sales CRM tool that provides pipeline management and sales automation features.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

Each API request must include a valid API token for authentication. The token is generated per Pipedrive user account and serves as the credential to authorize access.

### APIs

Axonius uses the [Pipedrive API](https://developers.pipedrive.com/docs/api/v1).

### Permissions

The following permissions are required:

* To view other users in the organization, the requesting user must have the relevant permission.
* For guaranteed full visibility, an Admin-level token is recommended.

#### Supported From Version

Supported from Axonius version 7.0.8

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Pipedrive server.
2. **API Key** - An API Key associated with a user account that has the  Required Permissions to fetch assets.

![Pipedrive.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Pipedrive.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

### Related Enforcement Actions

* [Add Pipedrive User](/docs/add-pipedrive-user)
* [Suspend Pipedrive User](/docs/update-pipedrive-user)