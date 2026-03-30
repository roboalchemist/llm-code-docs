# Source: https://docs.axonius.com/docs/samsung-knox-mobile-enrollment.md

# Samsung Knox Mobile Enrollment (KME)

Samsung Knox Mobile Enrollment (KME) is a device enrollment tool that provides automated bulk registration and configuration of Samsung mobile devices for enterprise management.

The Samsung KME adapter enables Axonius to fetch and catalog mobile devices, ensuring comprehensive visibility into your enterprise device enrollment and configuration status.

## Asset Types Fetched

* Devices

## Data Retrieved through the Adapter

* **Devices** - ID, IMEI, serial number, model, state, user name, tenant name, profile ID, profile name, reseller name, create/update times, and order/upload IDs.

## Before You Begin

### Required Ports

* TCP port 443

### Authentication Methods

* OAuth 2.0 Client Credentials

### Required Permissions

The **Client ID** and **Client Secret** used for the connection must be associated with an account that has permissions to fetch assets via the [Knox Mobile Enrollment API](#apis).

The registered OAuth 2.0 client must be granted one or more of the following read permission scopes to access device data:

* `kme`
* `kme.devices`
* `kme.devices:view`

### Generating the Client ID and Client Secret

1. Log in to the <Anchor label="Samsung Knox Dashboard" target="_blank" href="https://www.samsungknox.com/en/dashboard">Samsung Knox Dashboard</Anchor>.
2. Navigate to the **Knox Cloud Services** (or **API Integration**) section to manage OAuth clients.
3. Create a new **OAuth Client** (or **Application**) for the Axonius adapter.
4. During creation, ensure you select the **Client Credentials** grant type.
5. Assign the **Required Permissions** (Scopes) listed above.
6. Generate the credentials.
7. Copy the **Client ID** and **Client Secret** and save those in a secure location.

### APIs

Axonius uses the <Anchor label="Samsung Knox Mobile Enrollment API" target="_blank" href="https://docs.samsungknox.com/dev/knox-mobile-enrollment/server-integration/api">Samsung Knox Mobile Enrollment API</Anchor> to retrieve asset data.

### Supported from Version

This adapter is supported from Axonius version 8.0.7.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the URL of the Samsung Knox API region your tenant is hosted in (for example: `https://us-kcs-api.samsungknox.com`).
2. **Client ID** - Enter the Client ID (OAuth 2.0) generated from the Knox Cloud API portal.
3. **Client Secret** - Enter the Client Secret (OAuth 2.0) associated with the Client ID.

<Image align="center" alt="Samsung KME adapter - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Samsung_Knox_ME_Add_Connection.png" className="border" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).