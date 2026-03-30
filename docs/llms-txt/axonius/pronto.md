# Source: https://docs.axonius.com/docs/pronto.md

# Pronto

Pronto enables organizations to accelerate collaboration and efficiency by seamlessly integrating data and workflows across departments and enterprise systems.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Token

### APIs

Axonius uses the [Pronto REST API](https://developers.pronto.io/docs/pronto-api/75d92f56e1789-list-all-users-in-your-org).

### Permissions

The following permissions are required:

* **Fetch User**: org-users-read

* **Create User, Update User, Suspend User**: org-users-write

#### Supported From Version

Supported from Axonius version 7.0.6

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: `https://api.pronto.io/api`)* - The hostname or IP address of the Pronto server.
2. **API Token** - An API Token associated with a user account that has the  Required Permissions to fetch assets. For information on creating an API Token, see [Authentication](https://developers.pronto.io/docs/pronto-api/cd5e0c8aa2bc1-overview#authentication).

![Pronto.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Pronto.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).