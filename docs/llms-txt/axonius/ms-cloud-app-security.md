# Source: https://docs.axonius.com/docs/ms-cloud-app-security.md

# Microsoft Cloud App Security

Microsoft Cloud App Security is a Cloud Access Security Broker (CASB) that supports various deployment modes including log collection, API connectors, and reverse proxy.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* SaaS data

## Parameters

1. **Cloud Environment** - Configure the Cloud Environment you want to use. The authentication domain of adapter will change accordingly. The options are Global, China, Azure US Gov Cloud, and Azure US Gov DoD Cloud.

2. **Portal URL** *(required)* - The hostname or IP address of the Microsoft Cloud App Security server that Axonius can communicate with via the [Required Ports](#required-ports). Refer to [Cloud App Security REST API](https://docs.microsoft.com/en-us/cloud-app-security/api-introduction#api-url-structure) for details.

3. **Authentication Method** - Select the Authentication Method, either 'Token' or 'OAuth2'. If you choose Token, then 'Token' is displayed. If you choose 'OAuth2', 'Client ID', 'Client Secret', and 'Tenant ID' are displayed.

4. **Token** *(required)* - This option is available when you choose 'Token' as the 'Authentication Method'. A Token associated with a user account that has  permissions to fetch assets. Refer to [API Tokens](https://docs.microsoft.com/en-us/cloud-app-security/api-introduction#api-tokens) for details.

5. OAuth2 Options: The following options are displayed when you choose 'OAuth2' as the 'Authentication Method'. To use them you need to register the application, as explained in [Access with application context](https://learn.microsoft.com/en-us/defender-cloud-apps/api-authentication-application).
   1. **Client ID** and **Client Secret** - Provided after registering the Application.
   2. **Tenant ID** - Provided by Microsoft.

6. **Username** and **Password** *(Required to fetch SaaS data)* - The credentials for a user account that has the permissions needed to fetch SaaS data.

7. **2FA Secret Key** *(Optional)* - The secret generated in Microsoft Entra ID for setting up 2-factor authentication for the Microsoft user. For information on how to generate this key, see the [Microsoft Entra ID and Microsoft Intune documentation](https://docs.axonius.com/docs/microsoft-azure-active-directory-ad#/enable-or-exclude-multi-factor-authentication). This is needed if the Entra ID user requires 2FA authentication.

8. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

9. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

10. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

11. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

**Connecting the Adapter with OAuth2**
![Connecting with auth](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MCAS_Adapter_OAUTH.png)
**Connecting the Adapter with a token**
![Connecting with token](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MCAS_Adapter_Token.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **How to fetch user entities** - You can select which fetching method to use to fetch user entities. Your selection will affect the fetching time. You can either enable it in Normal Fetch (will increase the fetching time significantly), enable it in Background Fetch, or not fetch user entities at all.
2. **Ignore users with no domain** *(optional, default: true)*   - Select this option to ignore Microsoft Cloud App Security users that do not have a domain field.
3. **Ignore external users** - Select this option to ignore external users.
4. **Ignore SaaS Applications Repository and parse all applications** *(only for accounts with Axonius SaaS Applications)* - Select this option to parse and save all the SaaS applications, even if they are not known by the Axonius SaaS Applications Repository.
5. **Timeframe** - Set the fetch timeframe: 30 (default), 60, or 90 days.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Microsoft List - Entities API](https://docs.microsoft.com/en-us/cloud-app-security/api-entities-list).

Refer to [Connecting to Cloud App Security API](https://blog.ciaops.com/2019/10/08/connecting-to-cloud-app-security-api/) to learn how to generate a token.

## Required Ports

Axonius must be able to communicate with the value supplied in [Portal URL](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [Token](#parameters) must be associated with credentials that have permissions to fetch assets.

If OAuth2 is selected as the authentication method, the application associated with the Client ID must be granted the following permissions:

* discovery.read
* investigation.read
* settings.read

### Accessing OAuth2 Permissions

1. In the Azure portal navigate to **App registrations `>` `{App name}` `>` API Permissions.**

2. Click **Add a permission**.

3. Click the **APIs my organization uses** tab, locate and click **Microsoft Cloud App Security**.
   ![api permissions](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MCAS_RequestAPIPermission.png)

4. Click **Application permissions**.

5. Select the permissions mentioned above.
   ![request premissions](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MCAS_Permissions.png)

6. Click **Add permssions**.

7. Click **Grant admin consent for `{Directory name}`**.

8. When prompted, click **Yes**.

## Supported From Version

Supported from Axonius version 4.4