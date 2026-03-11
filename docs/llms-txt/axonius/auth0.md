# Source: https://docs.axonius.com/docs/auth0.md

# Auth0

Auth0 provides authentication and authorization solutions for web, mobile, and legacy applications.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Client ID/Client Secret

### APIs

Axonius uses the [Get Users API](https://auth0.com/docs/api/management/v2#!/Users/get_users).

To get API Access tokens, see [Get Management API Access Tokens for Production](https://auth0.com/docs/secure/tokens/access-tokens/get-management-api-access-tokens-for-production).

<Callout icon="📘" theme="info">
  Note

  Before getting the API Access tokens, you need to register your machine-to-machine app with Auth0 according to the instructions in [Permissions](/docs/auth0#permissions).
</Callout>

### Permissions

The value supplied in [Client ID](/docs/auth0#required-parameters) must have read:users permissions to fetch assets.

For additional required permissions, see [Advanced Settings](/docs/auth0#advanced-settings).

You must do the following before configuring the Auth0 adapter connection screen:

1. Register a new machine-to-machine application with Auth0 and authorize it:[Follow steps 1 to 3](https://auth0.com/docs/get-started/auth0-overview/create-applications/machine-to-machine-apps). In step 3, select the **Auth0 Management API**, and click **Authorize**.
2. [Create credentials using the Post method](https://auth0.com/docs/get-started/applications/confidential-and-public-applications/view-application-type): Select the **Client Secret (Post)** method.
3. [Get a Management API token](https://auth0.com/docs/secure/tokens/access-tokens/management-api-access-tokens.)
4. Authorize the Management API to use the credentials, by enabling the settings in the screen below. (Access this page through this path: **Applications → API → Management API → Machine to Machine Applications**.)

<Image alt="Auth0ManagementAPI" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Auth0ManagementAPI.png" />

5. Once enabled, enter the updated credentials into the Adapter connection screen.

#### Supported From Version

Supported from Axonius version 4.7

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Auth0 server.
2. **Client ID** and **Client Secret** - The credentials for a user account that has the Required Permissions to fetch assets.
   To obtain the **Client ID** and **Client Secret**, follow the instructions in [Authentication API](https://auth0.com/docs/api/authentication#authentication-methods), using the  **Post** method.

<Image alt="Auth0" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Auth0.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch User Roles** - Select this option to fetch user roles. Read permissions for roles are required for this setting.
2. **Fetch Organization Members** - Select this option to fetch organization members as Axonius users. If **Fetch User Roles** is enabled, the adapter will also fetch the roles of the organization members.

<Callout icon="📘" theme="info">
  Note

  The following permissions are required for the **Fetch Organization Members** setting:

  * read:organization\_member\_roles

  * read:organizations **OR** read:organizations\_summary
</Callout>

3. **Exclude users that are not organization members** - Select this option to not fetch users that are not part of an organization.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>