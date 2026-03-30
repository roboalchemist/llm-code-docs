# Source: https://docs.axonius.com/docs/sailpoint-iq.md

# SailPoint IdentityIQ

SailPoint IdentityIQ is an identity and access management (IAM) solution that delivers automated access certifications, policy management, access request and provisioning, password management, and identity intelligence.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Roles
* Accounts/Tenants

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SailPoint IdentityIQ server. You must include https\:// or http\:// at the beginning of the Host Name or IP Address

2. **Port** *(optional)* - The port for the SailPoint IdentityIQ instance.

3. **Auth Method** - Select Authentication method either **Basic Authentication** (default) or **OAuth 2.0**.
   * **Basic Authentication**:
     * **Username** and **Password** - The credentials for a user account that has the permissions to fetch assets.
   * **OAuth 2.0**:
     * **Client ID** and  **Client Secret** - Parameters for SailPoint IdentityIQ OAuth2 authentication.

4. **Filter** - A filter to use. Note that the filter only works for the Users asset type.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

9. **API Gateway Connection** *(optional)* - Enable this to use API gateway parameters for authentication. After enabling this option, under API Gateway Type, choose Layer7 and fill in the parameters that are displayed (in addition to the SailPoint IdentityIQ host name or IP address). Read more about [Layer7 API Gateway Parameters](/docs/adding-a-new-adapter-connection#layer7-api-gateway-parameters).

<Callout icon="📘" theme="info">
  Note

  When you use an API gateway connection, the other authentication parameters are not required. However, to add the connection successfully, you need to enter placeholder values in these fields.
</Callout>

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![IdentityIQ](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-806O4SEM.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch user entitlements** - Select this option to fetch user entitlements.
2. **Fetch user roles** - Select this option to fetch user roles.
3. **Fields to exclude from fetch** - Enter a comma-separated list of fields to exclude from the fetch.
4. **Fields to include exclusively from the fetch** - Enter a comma-separated list of fields to include from the fetch.
5. **Custom attributes to fetch** -  Enter a comma-separated list of extra fields to fetch.
6. **Users per request** *(default: 1000)* - Enter a number of users to receive in each request from the server, in order to reduce strain on the server.
7. **Exclude disabled users** - Select this option to not fetch users whose “active“ status is false or non-existent.
8. **Async batch chunk size** *(default: 50)* - Specify the size of the chunk size per async request batch. This can be helpful when the SailPoint IdentityIQ server crashes due to loads.
9. **Fetch users seen in the last X days** - Fetch only users that have been seen within the given number of days.
10. **Save entitlements raw data** - Select this option to save the raw data for the entitlements field in JSON format.
11. **Fetch Sailpoint Applications as Accounts** - Select this option to fetch SailPoint Applications as Accounts.
12. **Fetch Sailpoint Accounts as Users** - Select this option to fetch SailPoint Accounts as Users.
13. **Fetch Roles as Assets** - Select this option to fetch SailPoint Roles as Roles.
14. **Fetch Entitlements as Roles** - Select this option to fetch SailPoint Entitlements as Roles.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [IdentityIQ SCIM REST API (8.3)](https://developer.sailpoint.com/iiq/api/).

## Supported From Version

Supported from Axonius version 4.5