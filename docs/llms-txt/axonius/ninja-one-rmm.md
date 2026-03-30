# Source: https://docs.axonius.com/docs/ninja-one-rmm.md

# Ninja One (RMM)

Ninja One is an RMM (Remote Monitoring and Management) solution for MSPs and IT organizations, allowing them to automate, manage, and remediate endpoint management tasks.

### Use Cases the Adapter Solves

* **Endpoint Visibility**: Gain a comprehensive view of all devices managed by Ninja One, including detailed software and patch information.
* **Security Monitoring**: Identify devices with missing patches or unauthorized software to ensure endpoint security compliance.
* **Asset Enrichment**: Enrich device data with volume information and Windows services to support deep technical auditing and troubleshooting.

### Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg) Software | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications

<br />

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

<Tabs>
  <Tab title="Client Credentials Authentication">
    While creating the api client\_id and secret, the customer will need to select scope='Monitoring', and Grant\_type='Client Credentials'.
  </Tab>

  <Tab title="Authorization Code Authentication">
    Enable the **Use Authorization Code Authentication** toggle to use this method. This requires a Redirect URI and Authorization Code obtained by registering the Axonius app in NinjaOne with `offline_access` and `monitoring` scopes.
  </Tab>
</Tabs>

### APIs

Axonius uses the [Ninja RMM Public API 2.0](https://app.ninjarmm.com/apidocs/?links.active=core).
`/v2/device/{id}/windows-services` - to fetch Windows services.

### Permissions

The following permissions are required:

* Scope: 'Monitoring' (required for fetching assets).
* Scope: 'Management' (required only to run Enforcement Sets).
* Grant Type: 'Client Credentials' or 'Authorization Code' and 'Refresh Token' depending on the auth method.

<Callout icon="📘" theme="info">
  Note:

  If you do not see these options, the account may have restricted permissions. Please contact your NinjaOne admin.
</Callout>

#### Supported From Version

Supported from Axonius version 4.6

### Setting Up Ninja One to Work with Axonius

Either obtain the API Client ID and Client Secret or the Authorization Code

<Tabs>
  <Tab title="To obtain the API Client ID and Client Secret:">
    1. From the Ninja RMM Management portal, open the **Integrations** page.

    <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NinjaCionfig1.png" width="500px" alt="NinjaCionfig1.png" />

    2. Under **API** select **Client App IDs** and click **Add** to add an API Key.

    <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Ninjaconfig2.png" width="500px" alt="Ninjaconfig2.png" />

    3. Configure the API as shown below. Set the **Name** as needed.

    <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NinjaConfig3.png" width="500px" alt="NinjaConfig3.png" />

    4. Click **Save**. The **Client Secret key** is displayed. It is only shown once. Copy the Client Secret Key and make sure you save it to a safe place. Then click **Close**.

    <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Ninjacoinfig4.png" width="500px" alt="Ninjacoinfig4.png" />

    5. The **Client ID** is now displayed on the API page. Copy the Client ID and save it to a safe place.

    <Image align="center" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NinjaConfig5.png" width="500px" alt="NinjaConfig5.png" />
  </Tab>

  <Tab title="Authorization Code">
    1. * To obtain the **Redirect URI** and **Authorization Code**:
    2. Register your Axonius app in the NinjaOne application. To learn more, refer to [Register Regular Web Applications](https://ca.ninjarmm.com/apidocs-beta/authorization/create-applications/regular-web-apps). To continue, your app must include the following grant types: Authorization Code and Refresh Token.
    3. Select **Web** as the Application Platform.
    4. Enter a **Redirect URI(s)**.
    5. Select the **Scope** of your app: `offline_access` (always required), `monitoring` (always required), or `management` (required only to run Enforcement Sets).
    6. Navigate to: `https://NINJA_DOMAIN/oauth/authorize?response_type=code&client_id=CLIENT_ID&client_secret=CLIENT_SECRET&redirect_uri=REDIRECT_URL`. Ensure to replace NINJA\_DOMAIN, CLIENT\_ID, CLIENT\_SECRET, and REDIRECT\_URI with the actual values.
    7. You are redirected to a NinjaOne Login page.
    8. After you log in, you are redirected to the REDIRECT\_URI you provided earlier. It should be in the following format: `http://localhost/?code=YjAzYzgyNDYtZTE3YS00OWZkLTg2YTgtNDc3Zjg4YzFiZDlkNTRlN2FhMjMtYzUz&state=AXONIUS_STATE`.
    9. Copy the **code** query parameter and use it as the Authorization Code in your Webex adapter.
    10. To learn more, refer to [Authorization Code Flow](https://ca.ninjarmm.com/apidocs-beta/authorization/flows/authorization-code-flow).
  </Tab>
</Tabs>

<br />

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for **Ninja One**, and click on the adapter tile.\
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Ninja One (RMM) server.

<Tabs>
  <Tab title="Client ID and Client Secret">
    1) **Client ID** - Credentials to connect to the Ninja One (RMM) server.
    2) **Client Secret** - Credentials to connect to the Ninja One (RMM) server.
  </Tab>

  <Tab title="Use Authorization Code Authentication">
    1. **Use Authorization Code Authentication**   - Enable this toggle to use the Authorization Code Authentication method instead of the default  Client Credentials Authentication. When you enable this, the following fields become required:

    * **Redirect URI** - The URI you use to register the Axonius app in NinjaOne.
    * **Authorization Code** - The code obtained from the NinjaOne authorization flow. See the instructions above.
  </Tab>
</Tabs>

<br />

**Connection Label** - A label to help you distinguish between multiple connections for the same adapter. See [Connection label](/docs/adding-a-new-adapter-connection#setting-adapter-connection-parameters).

<Image align="center" alt="NinjaOne RMM config" border={false} width="500" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/NinjaOneRMM.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting via the HTTPS Proxy.
4. **HTTPS Proxy Password** - The password to use when connecting via the HTTPS Proxy.
5. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

<br />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

1. **Fetch Users** - (default true) Select this option to fetch users.
2. **Fetch Device software and patch information** - Select to fetch software and patch information for devices.
3. **Fetch Device volume information** - Select to fetch volume information for devices.
4. **Fetch Windows Services** - Select this option to fetch Windows Services.

<br />

### Related Enforcement Actions

* [Ninja One - Run Scripts on Device](/docs/ninja-rmm-run-scripts)

### Version Matrix

| Version          | Supported | Notes |
| :--------------- | :-------- | :---- |
| Ninja One RMM V2 | Yes       |       |

Verify