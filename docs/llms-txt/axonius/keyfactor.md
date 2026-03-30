# Source: https://docs.axonius.com/docs/keyfactor.md

# Keyfactor

Learn about Keyfactor's PKI as-a-Service, asset types fetched, setup, and advanced settings for Axonius integration.

Keyfactor provides PKI as-a-Service enabling protection of every device, workload, and digital transaction with a unique and trusted identity.

## Asset Types Fetched

* Devices
* Users
* Licenses
* SaaS Applications
* Certificates

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

User Name and Password or OAuth Authentication

### APIs

Axonius uses the Keyfactor Web API.

### Permissions

The following permissions are required:

* Certificates: Read
* SystemSettings: Read

To use the endpoint 'GET SSH Users' the following permissions are required:

* SSH: ServerAdmin
  **OR**
* SSH: EnterpriseAdmin

#### Supported From Version

Supported from Axonius version 4.8

<br />

### Setting Up Keyfactor to Work with Axonius

When you are using OAuth Authentication:

* You need to obtain the [Client ID and  Client Secret](https://software.keyfactor.com/Core-OnPrem/Current/Content/InstallingServer/Main/KeyfactorIdP_Using.htm#ServiceAccounts).
* You need to obtain the [Token to Authenticate to the Keyfactor API.](https://software.keyfactor.com/Core-OnPrem/Current/Content/WebAPI/AuthenticateAPI.htm#AcquireToken)

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Keyfactor, and click on the adapter tile. Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Keyfactor server.

**Authentication Methods**

<Tabs>
  <Tab title="User Name and Password">
    1. **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.
  </Tab>

  <Tab title=" OAuth Authentication">
    1. **Client ID** and **Client Secret** - The Client ID and Client Secret provided by the Identity Provider.

    2. **Token URL for OAuth Authentication**  - The Token URL of your identity provider’s token endpoint. For example:
       `https://my-keyidp-server.keyexample.com/realms/Keyfactor/protocol/openid-connect/token`
  </Tab>
</Tabs>

<br />

<br />

<Image alt="Keyfactor" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Keyfactor.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

<br />

1. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Fetch certificates by collections** - Toggle on to fetch certificates from all the collections the customer has in Keyfactor.
   * **Collection names** - If **Fetch certificates by collections** is enabled, you can enter a comma-separated list of collections to fetch from instead of all the collections.

<br />

<br />

<br />