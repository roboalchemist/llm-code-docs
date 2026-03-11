# Source: https://docs.axonius.com/docs/aurion.md

# Aurion

Aurion is a software solution that offers human resource management and payroll services.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the Aurion 11 SOAP API.

### Permissions

* The service user must be explicitly granted access to `GET_USER_DETS` (or other target API functions).

#### Supported From Version

Supported from Axonius version 7.0.13

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Aurion server.

2. **User Name** and **Password**  - The credentials for a user account that has the Required Permissions to fetch assets.

<Image alt="Aurion Connection Screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Aurion_AddConnection.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

### Related Enforcement Actions

* [Aurion - Create User](https://docs.axonius.com/axonius-help-docs/docs/aurion-create-user)
* [Aurion - Update User](https://docs.axonius.com/axonius-help-docs/docs/aurion-update-user)
* [Aurion - Suspend User](https://docs.axonius.com/axonius-help-docs/docs/aurion-suspend-user)