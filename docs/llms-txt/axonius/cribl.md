# Source: https://docs.axonius.com/docs/cribl.md

# Cribl

Cribl is a vendor-agnostic observability pipeline used to collect, reduce, enrich, normalize, and route data.

<br />

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password for Cloud
* Client ID/Client Secret for on-prem

### APIs

Axonius uses the [Cribl API Reference](https://docs.cribl.io/api/).

### Permissions

The value supplied in [User Name](#required-parameters) must have reader\_all permissions in order to fetch assets.

#### Supported From Version

Supported from Axonius version 6.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address**  - The hostname or IP address of the Cribl server.

2. **Auth Method** - Select an Authentication method, either **User Name and Password** (default) or **Client ID and Client Secret**.
   * **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.

   * **Client ID** and **Client Secret** - The Client ID and Client Secret for an account that has permissions to fetch assets. Refer to [API Docs | Cribl Docs](https://docs.cribl.io/stream/api-tutorials/#create-credential) for information on how to create the  Client ID and Client Secret.

<Image alt="Cribl with User Name and Password" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cribl%20with%20User%20Name%20and%20Password.png" />

*Cribl Settings with **User Name and Password** Authentication Method*

<Image alt="Cribl with Client ID and Client Secret" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cribl%20with%20Client%20ID%20and%20Client%20Secret.png" />

*Cribl Settings with **Client ID and Client Secret** Authentication Method*

<br />

### Optional Parameters

1. **Port**  - The port used for the connection. If the Auth Method is set to 'User Name and Password', then it defaults to 9000. If the 'Auth Method' is set to 'Client ID and Client Secret', it defaults to 443.

2. **Group Name Suffix** - Enter a group name suffix to the Users endpoint (Example: /m/group\_name)

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).