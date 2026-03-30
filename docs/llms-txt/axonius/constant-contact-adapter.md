# Source: https://docs.axonius.com/docs/constant-contact-adapter.md

# Constant Contact

Constant Contact is a digital marketing platform used to manage email and digital outreach campaigns, contact lists, and engagement metrics.

## Use Cases the Adapter Solves

* Detects and analyzes unmanaged marketing accounts for better digital campaign visibility.
* Verifies third-party contact list access and associations for compliance and audit readiness.

### Asset Types Fetched

* ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users |

## Data Retrieved through the Adapter

The following data can be fetched by the adapter:

**Users**- Fields such as email address, status, roles.

## Before You Begin

**Ports**

TCP port 443

**Authentication Method**

OAuth 2.0 Access Token

### APIs

[Constant Contact v3 API](https://developer.constantcontact.com/api_guide/v3_technical_overview.html)\
GET] `https://api.cc.email/v3/account/emails`

### Permissions

The following permissions are required:

* `account:read` scope

#### Supported From Version

Supported from Axonius version 8.0.12

### Setting Up Constant Contact to Work with Axonius

To Generate the Client ID (API Key), and Client Secret follow the procedure in [Constant Contact Quick Start Guide 'Register Your First Application'](https://developer.constantcontact.com/api_guide/getting_started.html)

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Constant Contact, and click on the adapter tile.\
Click **Add Connection**.

### Required Parameters

To connect the adapter in Axonius, provide the following parameters:

1. **Host Name or IP Address** - Enter the hostname or IP address of the Constant Contact server. For Constant Contact, this is typically `https://api.cc.email`
2. **Client ID and Client Secret** - The unique identifier assigned to your Constant Contact application when you register it in the Constant Contact Developer Portal. This is required for OAuth 2.0 authentication and identifies your integration when requesting an access token. Obtainable from the Constant Contact Developer Portal when you create or view your API application.
3. **Client Secret** - A confidential key associated with your Constant Contact application, also obtained from the Developer Portal.  Available in the Constant Contact Developer Portal alongside the Client ID.
4. **Connection Label** - A name for this connection.

![ConstandContact](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/ConstantContact.png)

<br />

### Optional Parameters

* **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **HTTPS Proxy**.
* **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

**Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

<br />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

<br />

<br />

<br />

<br />

***