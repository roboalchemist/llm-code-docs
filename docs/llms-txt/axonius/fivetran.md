# Source: https://docs.axonius.com/docs/fivetran.md

# Fivetran

Fivetran is a data integration tool that provides automated data pipelines for seamless data movement.

### Asset Types Fetched

* ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Groups.svg) Groups | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Roles.svg) Roles | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_resources.svg) Application Resources

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

API key authentication.

### APIs

Axonius uses the [Fivetran REST API v1](https://fivetran.com/docs/rest-api/getting-started)

### Permissions

The following permissions are required:

The API key must be able to read Users, Roles, Destinations, Groups, and Connections.  The API key should have an Account Reviewer role.

#### Supported From Version

Supported from Axonius version 8.0.9

<br />

## Connecting the Adapter in Axonius

* Navigate to the Adapters page, search for Fivetran, and click on the adapter tile.
* Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address**  *(default: `https://api.fivetran.com`)* - The hostname or IP address of the fivetran server.

2. **API Key** and **API Secret**  - The credentials for a user account that has the Required Permissions to fetch assets. Refer to [Fivetran REST API.](https://fivetran.com/docs/rest-api/getting-started#scopedapikey) for details of how to get the **API Key** and **API Secret**.

<Image align="center" alt="BackBox connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Fivetran.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

5. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.
   <br />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />