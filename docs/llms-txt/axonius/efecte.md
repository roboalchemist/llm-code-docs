# Source: https://docs.axonius.com/docs/efecte.md

# Efecte

Efecte is an IT service management (ITSM) and collaboration platform with a focus on SaaS security and configuration management.  The Efecte adapter for Axonius allows organizations to aggregate and manage assets from the Efecte platform to gain visibility into their IT infrastructure and service environment.

## &#x20;Assets Types Fetched

This adapter fetches the following types of assets:

* Devices, Software, SaaS Applications

**Authentication Method**

User Name and Password

**Required Ports**

TCP port 443

### Required Permissions

To use the REST API:

* AREST API license is required.
* A technical (local) user and a role defined for access management purposes.
* Folder permissions
* Template permissions
* Permissions to use the External API

#### Supported From Version

Supported from Axonius version 6.1

<br />

### Setting Up Efecte  to Work with Axonius

The Efecte Service Management tool needs to have a local EMS user account for Axonius with the required permissions.

Create an account as follows:

1. Create a role and select 'Efecte External API module permissions.
2. Add folder and template permissions to the role.
3. Create a REST API user for Axonius.
4. Add the user to the Role you created

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Efecte, and click on the adapter tile.
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Efecte server.

2. **User Name** and **Password**   - The credentials for a user account that has permission to fetch assets.

<Image alt="Efecte" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Efecte.png" />

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**  - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**   - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />