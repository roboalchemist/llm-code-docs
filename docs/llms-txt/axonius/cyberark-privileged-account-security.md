# Source: https://docs.axonius.com/docs/cyberark-privileged-account-security.md

# CyberArk Privileged Account Security

CyberArk Privileged Account Security provides privileged password management, session recording, least privilege enforcement, and privileged data analytics.

### Asset Types Fetched

* Devices, Users, Groups, Secrets

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* CyberArk
* Windows
* LDAP
* RADIUS
* SAML
* OAuth2

### APIs

Axonius uses the <Anchor label="CyberArk REST API" target="_blank" href="https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/11.1/en/Content/WebServices/API%20Commands.htm">CyberArk REST API</Anchor>.

To use the SAML authentication method you need to enable the SAML IdP initiated SSO flow. Follow instructions in <Anchor label="Configure the IdP" target="_blank" href="https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/12.1/en/Content/PAS%20INST/SAML-Authentication.htm#!#Configur">Configure the IdP</Anchor> to implement this. This returns the SAML Response.

### Permissions

The value supplied in [User Name](#required-parameters) must have **Audit users** permission.

The Client ID/Secret permissions must be updated to match the <Anchor label="Create a Service user for API requests" target="_blank" href="https://docs.cyberark.com/privilege-cloud-shared-services/Latest/en/Content/ISPSS/ISPSS-API-Authentication.htm#Step1CreateaServiceuserforAPIrequests">Create a Service user for API requests</Anchor> section.

The following permissions are only relevant if you are using the OAuth2 authentication (i.e., with the cloud version):

You must update the domain to be `<subdomain>.privilegecloud.cyberark.cloud`.

Example: `https://ihg.privilegecloud.cyberark.cloud`

You need the following permissions:

* privilege cloud auditors
* privileged cloud users

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **CyberArk Domain** - The hostname or IP address of the CyberArk IIS server.
2. **Authentication Method** *(default: CyberArk)* - The authentication method used for the connection. The following authentication methods are supported: **CyberArk**, **Windows**, **LDAP**, **RADIUS**, **SAML**, and **OAuth2**. Refer to [APIs](#APIS) for details about configuring SAML authentication.
3. **User Name/Client ID** and **Password/Client Secret** - The credentials for a user account that has the Required Permissions to fetch assets. Fill in Client ID and Client Secret for OAuth2 authentication. When you choose SAML authentication this field is not required.
4. **Tenant ID - Cloud Only** - Specify the Tenant ID if you choose OAuth2 authentication. The OAuth2 method only works with the cloud version.

<Callout icon="📘" theme="info">
  **Finding the Tenant ID**

  1. From CyberArk Privilege Cloud, click the user icon in the top-right corner, then click **Tenant details**.
     2\. The value next to ID is the Tenant ID that you need to use. Copy this into the **Tenant ID** field in Axonius.
</Callout>

5. **SAML Response** - When you use the **SAML** authentication method insert the SAML Response.

![CyberArk PAS connection screen](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/CyberArkPAS_AddConnection.png)

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **API Gateway Connection** - Enable this to use API gateway parameters for authentication. After enabling this option, under **API Gateway Type**, choose Layer7 and fill in the parameters that are displayed (in addition to **CyberArk Domain**). Read about [Layer7 API Gateway Parameters](/docs/adding-a-new-adapter-connection#layer7-api-gateway-parameters).

<Callout icon="📘" theme="info">
  Note

  When you use an API gateway connection, the other authentication parameters are not required. However, to add the connection successfully, you need to enter placeholder values in these fields.
</Callout>

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch accounts** - Select whether to fetch CyberArk PAS accounts.
2. **Fetch account activities** - Select whether to fetch the activities for each account. In order to enable this option, the Fetch accounts option must be enabled as well.
3. **Fetch extended accounts overview** - Select whether to fetch additional data about each account. In order to enable this option, the Fetch accounts option must be enabled as well.
4. **Parse the Domain value as an associated device** - Select this option to parse the domain value as an associated device.
5. **Fetch Secrets from Safe** - Select this option to fetch Safes as secrets.
6. **Enrich Users and Groups with permitted safes** - Select to enrich Users and Groups assets with safe information. To use this capability, you must also enable **Fetch Secrets from Safe**.
7. **Fetch Groups as Assets** - Select this option to fetch Groups as asset.
8. **Ignore Logon Domain** - Select this option to ignore the logon domain and use only the domain taken from the 'Address' field.
9. **Fetch Platforms** - Select this option to enrich account data with platform information. This setting is only available only when 'Fetch Accounts' is enabled.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](https://docs.axonius.com/docs/advanced-settings).
</Callout>

<br />

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version                                 | Supported | Notes |
| --------------------------------------- | --------- | ----- |
| Privileged Access Security Version v10+ | Yes       |       |