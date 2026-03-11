# Source: https://docs.axonius.com/docs/zimperium.md

# Zimperium

Zimperium Mobile Threat Defense is an on‑device security engine that detects and prevents mobile threats across device, network, phishing and app attacks using machine‑learning.

## &#x20;Assets Types Fetched

This adapter fetches the following types of assets:

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg" /> Devices | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Findings.svg" /> Aggregated Security Findings | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg" /> Users | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Roles.svg" /> Roles | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg" /> SaaS Applications | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Incidents.svg" /> Alerts/Incidents

## Before You Begin

### Authentication Methods

* API V1 uses and API Key
* API V2 authentication is based on JSON Web Tokens (JWTs), which are generated using a Client ID and Client Secret.

### Required Permissions

The API key must be associated with a Role that grants the necessary View scopes for all required asset types.

* Users: users:view
* Roles: roles:view
* Devices: devices:view
* Vulnerabilities (Aggregated Security Findings): os\_risk:view
* Alerts/Incidents: threats:view

### APIs

Axonius uses the [Zimperium zIPS](https://www.zimperium.com/zips-mobile-ips/) API.

### Supported From Version

Supported from Axonius version 4.7

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address**  - The hostname or IP address of the Zimperium server.

2. **API Version**  - Select the API version you are using and enter the relevant parameters.

<Tabs>
  <Tab title="API v1">
    1) **API Key**- An API Key associated with a user account that has permissions to fetch assets. To obtain the API Key: Contact the Zimperium Customer Success team and request an API Key value to access the API requests.
  </Tab>

  <Tab title="API v2">
    **Client ID** and **Client Secret** - generate them in  the Console's Account Management section, under the "*Authorizations*” menu. On the Authorizations page, click the + Generate API Key button\
    to create a client ID and client secret.
  </Tab>
</Tabs>

<br />

<br />

<Image alt="zimperium" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/4339fc87d52ff1eb003d9fb5d520602324fad1c5/Images/zimperium.png" />

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch device vulnerabilities** - Select whether to fetch vulnerabilities on devices.
2. **Fetch Roles** *(for API V2)* - Fetch SecurityRoles from the roles endpoint.
3. **Fetch Incidents (Threats)** *(for API V2)* - Fetch incidents from the threats endpoint.
4. **Fetch Incidents From Last X Days (default 30)** *(for API V2)* - Fetch incidents from the previous X days.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />