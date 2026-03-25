# Source: https://docs.axonius.com/docs/cyberark-endpoint-privilege-manager.md

# CyberArk Endpoint Privilege Manager

CyberArk Endpoint Privilege Manager enforces least privilege, providing credential theft protection and application control at scale.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the CyberArk Endpoint Privilege Manager server.
2. **Authentication Method** - The authentication method used for the connection. The following methods are supported for  authentication: EPM or Windows. To use SAML select Use SSO Authentication.
3. **Application ID** *(required)* - If you are not using SSO Authentication, enter the Application ID which is a unique value to identify the "Axonius" application. This is a unique value that has not been used in CyberArk EPM.
4. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
5. **Verify SSL** *(required, default: False)* - Choose whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
6. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
7. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
8. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

**Using SSO Authentication**

1. Toggle on **Use SSO Authentication**.

2. Select your **Identity Provider**.

3. Select *SAML* as the **SSO Protocol**.

4. Enter the **Redirect URL**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="CyberArkEnpintPrivilegeManager" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CyberArkEnpintPrivilegeManager.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch events** - Select this option to fetch event info, file info, source, pre-history and reputation information from CyberArk
2. **Fetch policies** - Select this option to fetch policies and enrich the computers (devices) with matching policies under the field "Policies".

<Callout icon="📘" theme="info">
  Note

  Fetching policies might increase the fetch time significantly.
</Callout>

4. **Customize rate limits** - Toggle on this option to customize rate limits. Use the options below to limit the number of requests the adapter sends per unit of time.

   * **Number of requests per second** *(default: 5)* - Set the number of requests per second. Set the number of seconds to send the request in 'Number of seconds'.

   * **Number of seconds** - Set the number of seconds during which the requests will be sent.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [CyberArk’s Web Services SDK](https://docs.cyberark.com/Product-Doc/OnlineHelp/EPM/Latest/en/Content/WebServices/API%20Commands.htm).

The adapter should reach the following endpoints:

* Policies list: [https://docs.cyberark.com/epm/latest/en/Content/WebServices/GetPolicies.htm](https://docs.cyberark.com/epm/latest/en/Content/WebServices/GetPolicies.htm)
* Policy details: [https://docs.cyberark.com/epm/latest/en/Content/WebServices/GetPolicyDetails.htm](https://docs.cyberark.com/epm/latest/en/Content/WebServices/GetPolicyDetails.htm)
  * Policy structure: [https://docs.cyberark.com/epm/latest/en/Content/WebServices/ApplicationPolicyDefinitions.htm#Policydetails](https://docs.cyberark.com/epm/latest/en/Content/WebServices/ApplicationPolicyDefinitions.htm#Policydetails)

## Required Permissions

The value supplied in [User Name](#parameters) must include enabled "Allow to manage sets" for the user profile and set to read only.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may also work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version             | Supported | Notes |
| ------------------- | --------- | ----- |
| Version 11.0 and up | Yes       |       |