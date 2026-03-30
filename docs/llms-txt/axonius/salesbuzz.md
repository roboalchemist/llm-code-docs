# Source: https://docs.axonius.com/docs/salesbuzz.md

# Salesbuzz

Salesbuzz is a mobile sales force automation platform that provides trip planning, contact management, order processing, inventory control, reporting, and ERP integration.

### Asset Types Fetched

* Users, Roles, Permissions

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### Permissions

* To successfully authenticate and access the SalesBuzz API, the API uses Bearer Token authentication.

* SalesBuzz includes a predefined Administrator role, which grants full system access.

* To gain full visibility and manageability across the platform, it is recommended to authenticate using a user explicitly assigned the Administrator role.

#### Supported From Version

Supported from Axonius version 7.0.4

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Salesbuzz server.
2. **User Name** and **Password**  - The credentials for a user account that has the  Required Permissions to fetch assets.
3. **Business Unit (BUID)** - The business unit IDs for which to pull the data.

![Salesbuzz.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Salesbuzz.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Related Enforcement Actions

* [Salesbuzz - Create User](/docs/salesbuzz-create-user)
* [Salesbuzz - Manage Users](/docs/salesbuzz-manage-users)