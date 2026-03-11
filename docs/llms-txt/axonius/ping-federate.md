# Source: https://docs.axonius.com/docs/ping-federate.md

# PingFederate

PingFederate from Ping Identity is an enterprise authentication federation server that enables user authentication and single sign-on.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* All Application Extensions
* All Application Extension Instances
* SaaS Applications
* Certificates
* Admin Managed Extensions
* Application Addons
* User Initiated Extensions
* Admin Managed Extension Instances
* Application Addon Instances
* Application Keys
* User Initiated Extension Instances

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the PingFederate server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Port** *(required)* - The API endpoint is available at the administrative port as defined in the pf.admin.https.port property. See [Accessing the API interactive documentation](https://docs.pingidentity.com/r/en-us/pingfederate-112/pf_access_api_interact_documentation) for more information.

3. **Authentication Method** - Select if you want to authenticate with **Basic Auth** or **OAUTH 2**. The following fields are displayed based on the authentication method you select (see screenshots below).
   * **Basic Authentication**:
     * **User Name and Password** - The credentials for a an admin user account that has the permissions to fetch assets.
   * **OAUTH 2:**
     * **Authorization URL** *(required)* - The URL to authorize access via OAUTH2 (located in the `<pf_install>/pingfederate/bin/oauth2.properties` file).
     * **Client ID** and **Client Secret** - The Client ID and Client Secret for an account that has read access to the API. These parameters are located in the `<pf_install>/pingfederate/bin/oauth2.properties` file.
     * **Scopes** - Enter the scopes you want to grant for this connection.
     * For more information, see [Enabling OAuth 2.0 authorization](https://docs.pingidentity.com/pingfederate/12.3/developers_reference_guide/pf_enable_oauth20_authoriz.html).

4. **SSO provider** - If your organization uses PingFederate for SSO, you can select this check box (selected by default). For more information, see [Connecting your SSO Solution Provider Adapter](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider).

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

**Adapter connection with Basic Auth authentication**
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PingFederate_BasicAuth.png)

**Adapter connection with OAuth2 authentication**
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PingFederate_OAuth2.png)

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Users from dataStores** - Select this option to fetch User Extensions from dataStores.
2. **Fetch OAuth clients** - Select this option to fetch OAuth clients.
3. **Fetch Certificates** - Select this option to fetch Certificates from the following endpoints: idp/spConnection, sp/idpConnections, keyPairs/signing, keyPairs/sslServer.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [ PingFederate API](https://docs.pingidentity.com/pingfederate/12.3/developers_reference_guide/pf_access_api_interact_documentation.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **9999** or as defined in run.properties file on the Ping Federate node.

## Adapter Integration Setup

Follow instructions in the [PingFederate documentation](https://docs.pingidentity.com/r/en-us/pingfederate-112/pf_enable_oauth20_authoriz) to generate the following parameters for the adapter connection form.

* Authorization URL for OAUTH2
* Client ID
* Client Authentication Password

## Supported From Version

Supported from Axonius version 5.0