# Source: https://docs.axonius.com/docs/xage.md

# Xage

Xage is a platform that provides identity-based access control, zero trust remote access, and microsegmentation for IT, OT, and cloud assets.

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password
* Access Request Token

### APIs

Axonius uses the Xage API.

### Permissions

You must have one of the following roles in order to obtain an Access Token for these calls:

* Read Only Admin
* Site Admin
* Super Admin

#### Supported From Version

Supported from Axonius version 7.1.11

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Xage server.
2. **Auth Method** - Select the authentication method, either **User Name** and **Password** or **Access Request Token**.
   * **User Name** and **Password**  - The credentials for a user account that has the  Required Permissions to fetch assets.
   * **Access Request Token** - An access request token associated with a user account that has the Required Permissions to fetch assets.

<Image alt="Xage.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Xage.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).