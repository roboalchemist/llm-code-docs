# Source: https://docs.axonius.com/docs/trimedx.md

# TRIMEDX

TRIMEDX is a healthcare technology management service that offers medical equipment management and maintenance solutions.

### Use Cases the Adapter Solves

* **Healthcare Equipment Inventory Management:** Gain complete visibility into all medical devices and equipment managed by TRIMEDX, ensuring comprehensive tracking of critical healthcare technology assets across your organization.

### Asset Types Fetched

* Devices

## Data Retrieved through the Adapter

The following data can be fetched by the adapter

**Devices** - Field such as: MDSP Source Device ID, TRIMEDX CEID, TRIMEDX Equipment ID, Last Modified Date

## Before You Begin

### Required Ports

TCP port 443 (HTTPS)

### Authentication Methods

OAuth2 Password Grant Authentication

### APIs

Axonius uses the TRIMEDX MDSP API. The following endpoints are called:

* `POST /oauth2/v1/token`
* `GET /mdsp-inventory/inventory`

### Required Permissions

The API user account must have:

* The following user permission: `mdsp.inventory.read`, `openid`

### Supported From Version

Supported from Axonius version 8.0.16.0

### Setting Up TRIMEDX to Work with Axonius

To obtain API credentials for use with Axonius:

1. Contact your TRIMEDX account representative or support team and Request API access credentials for the MDSP Inventory API. These include the  Username, Password, Client ID, Ocp-Apim-Subscription-Key (Subscription Key)

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for TRIMEDX, and click on the adapter tile.

Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - Base domain for the API, should contain a prefix of http\:// or https\://. Do not add any specific endpoints after the domain. Example: `https://api.trimedx.com`
2. **User Name** - The username provided by TRIMEDX for API authentication.
3. **Password** - The password provided by TRIMEDX for API authentication.
4. **Client ID** - OAuth2 Client ID provided by TRIMEDX.
5. **Subscription Key** - Ocp-Apim-Subscription-Key provided by TRIMEDX.

<br />

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/TRIMDEX.png)

### Optional Parameters

<br />

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).