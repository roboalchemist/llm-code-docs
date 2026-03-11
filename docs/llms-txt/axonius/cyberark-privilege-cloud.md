# Source: https://docs.axonius.com/docs/cyberark-privilege-cloud.md

# CyberArk Privilege Cloud

CyberArk Privilege Cloud is a privileged access management (PAM) solution for securing, managing, and monitoring privileged accounts.

CyberArk Privilege Cloud is a privileged access management (PAM) solution for securing, managing, and monitoring privileged accounts.

### Asset Types Fetched

* Users, Roles, Groups, Secrets, Application Resources

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

The adapter supports the following authentication methods:

* CyberArk, Windows, LDAP, RADIUS, SAML, or ISPSS

### APIs

Axonius uses the [CyberArk REST APIs](https://docs.cyberark.com/privilege-cloud-standard/latest/en/content/webservices/implementing%20privileged%20account%20security%20web%20services%20.htm).

### Required Permissions

The user account used for the adapter connection:

* Must have Audit permissions.
* Must be a member of a Safe in a CyberArk Vault.
* Must have List Accounts permissions in the Safe.

In addition, each authentication method requires specific permissions. See [Connecting the Adapter in Axonius](https://docs.axonius.com/docs/cyberark-privilege-cloud#connecting-the-adapter-in-axonius) for more information.

To assign the required permission to your Axonius user:

1. Go to **CyberArk** -> **Identity Administration** -> **Core Services** -> **Roles**.
2. Select **Create a new Role**.
3. Select **Administrative Rights** and click **Add**.
4. Add the following permission: Read Only System Administration.
5. Click **Save**.
6. Assign the new Role to the Axonius user.

#### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters - General

1. **Host Name or IP Address** - The hostname or IP address of the CyberArk Privilege Cloud server.
2. **Authentication Method** - Select the authentication method you want to use. The required parameters and permissions vary depending on the selected authentication.

### Parameters and Requirements per Authentication Method

<Tabs>
  <Tab title="CyberArk, Windows, LDAP, and RADIUS Authentication">
    These methods are typically used for direct authentication to the CyberArk Privilege Cloud server.

    #### Requirements

    * Ensure the user account has the Audit, Safe membership, and List Accounts permissions.
    * The selected network protocols must be properly configured for the CyberArk server.

    #### Parameters

    1. **User Name** and **Password** - The credentials for a user account that has the [required permissions](/docs/cyberark-privilege-cloud#required-permissions) to fetch assets.
       * For more information on creating accounts within CyberArk Privilege Cloud, see [Add and Manage Users](https://docs.cyberark.com/privilege-cloud-standard/latest/en/Content/Privilege%20Cloud/privCloud-user-mng.htm?tocpath=Setup%7CAdd%20and%20manage%20users%7C_____0).
       * For more information about logging in, see [CyberArk, LDAP, RADIUS](https://docs.cyberark.com/privilege-cloud-standard/latest/en/Content/SDK/CyberArk%20Authentication%20-%20Logon_v10.htm?tocpath=Developers%7CREST%20APIs%7CAuthentication%7CLogon%7C_____1).
  </Tab>

  <Tab title="SAML Authentication">
    #### Requirements

    You must enable the SAML IdP initiated SSO flow in your CyberArk environment. To implement this, follow the instructions in [Configure the IdP](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/12.1/en/Content/PAS%20INST/SAML-Authentication.htm#!#Configur). This returns the SAML Response used for connection.

    #### Parameters

    1. **User Name** and **Password** - The credentials for a user account that has the required permissions to fetch assets.
  </Tab>

  <Tab title="ISPSS Authentication">
    ISPSS Authentication (Identity Security Platform Shared Services) is **only relevant to the SaaS hosted version of CyberArk Privilege Cloud**. It requires specific configuration of a service account and careful attention to the different URLs for the Privilege Cloud and Identity Console.

    #### Requirements

    * Create an ISPSS service account. For more information, see [API token authentication for CyberArk Identity Security Platform Shared Services](https://docs.cyberark.com/ispss-access/latest/en/content/ispss/ispss-api-authentication.htm).
    * The CyberArk user account used for this connection must have the following settings enabled:
      * Is service user
      * Is OAuth confidential client
    * Password never expires (Crucial for service accounts)
    * The value of the **Host Name of IP Address** parameter must be in the following format: `https://ORGANIZATIONNAME.privilegecloud.cyberark.cloud`. The OrganizationName corresponds to the subdomain when logged into the Cyberark Privilege Cloud Console.

    #### Parameters

    1. **Use ISPSS APIs** - Check this option to enable the use of ISPSS APIs.
    2. **User Name** and **Password** - The credentials of an ISPSS service account that has the required permissions to fetch assets.
    3. **Use Subdomain for tenant URL**:
       * If the URL for the ID console is `https://TENANTNAME.id.cyberark.cloud`, **disable** this option.
       * If the URL for the ID console is `https://TENANTNAME.my.idaptive.app`, **enable** this option.
    4. **Tenant ID** - The subdomain used to access the CyberArk Identity Console. The value of this parameter must correspond to the correct URL format of your CyberArk Identity Console - `https://TENANTNAME.id.cyberark.cloud` or `https://TENANTNAME.my.idaptive.app`. In the Tenant ID field you need to enter the ID that is found under Identity in Cyberark.
  </Tab>
</Tabs>

![CyberArkPrivilegeCloud.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CyberArkPrivilegeCloud.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Endpoints Config** - Click on `>` to open the following settings for configurable endpoints:
  * **Enrich Users with User Roles** - Enable this option to enrich the Users endpoint with User Roles. This setting is relevant only when using the ISPSS authentication method.
  * **Enrich Users with Safe Members** - Enable this option to enrich the Users endpoint with Safe Members.
  * **Fetch Users of sub type account from Accounts** - Enable this option to fetch users of the subtype 'account' from the Accounts endpoint. When enabled, the following settings can be configured:
    * **Enrich Accounts with Account Activities** - Enable this option to enrich the Accounts endpoint with Account Activities.
    * **Enrich Accounts with Account Extended Data** - Enable this option to enrich the Accounts endpoint with Account Extended Data.
  * **Fetch Users of sub type users\_from\_safe\_members from Users From Safe Members** - Enable this option to fetch users of the subtype 'users from safe members' from the Users From Safe Members endpoint. This setting is relevant only when using the ISPSS authentication method.  When enabled, the following settings can be configured:
    * **Enrich Users From Safe Members with Safe Members** - Enable this option to enrich the Users From Safe Members endpoint with Safe Members.
    * **Enrich Users From Safe Members with Role Members** - Enable this option to enrich the Users From Safe Members endpoint with Role Members.
  * **Fetch Users of sub type users\_from\_role\_members from Users From Role Members** - Enable this option to fetch users of the subtype 'users from role members' from the Users From Role Members endpoint. This setting is relevant only when using the ISPSS authentication method.  When enabled, the following settings can be configured:
    * **Enrich Users From Role Members with Safe Members** - Enable this option to enrich the Users From Role Members endpoint with Safe Members.
    * **Enrich Users From Role Members with Role Members** - Enable this option to enrich the Users From Role Members endpoint with Role Members.
  * **Fetch Groups from Groups** - Enable this option to fetch groups from the Groups endpoint. When enabled, the following settings can be configured:
    * **Enrich Groups with Safe Members** - Enable this option to enrich the Groups endpoint with Safe Members.
  * **Fetch Secrets from Safes** - Enable this option to fetch secrets from the Safes endpoint. When enabled, the following settings can be configured:
    * **Enrich Safes with Safe Members** - Enable this option to add safe members data to Safes.
  * **Fetch ApplicationResources of sub type safe from Safes** - Enable this option to fetch application resources of the subtype 'safe' from the Safes endpoint. When enabled, the following settings can be configured:
    * **Enrich Safes with Safe Members** - Enable this option to add safe members data to Safes.
  * **Fetch ApplicationResources of sub type account from Accounts** - Enable this option to fetch application resources of the subtype 'account' from the Accounts endpoint.
  * **Fetch SecurityRoles from Built-in Roles** - Enable this option to fetch security roles from the Built-in Roles endpoint. This setting is relevant only when using the ISPSS authentication method. When enabled, the following settings can be configured:
    * **Enrich Built-in Roles with Role Members** - Enable this option to enrich the Built-in Roles endpoint with Role Members.
    * **Enrich Built-in Roles with Safe Members** - Enable this option to enrich the Built-in Roles endpoint with Safe Members.
* **Parser Config** - Click on `>` to open the following settings for configurable endpoints:
  * **Parse the Domain value as an associated device** - Select this option to parse the domain value as an associated device.
  * **Account Domain Source**  - Choose the source for the account domain parsing.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>