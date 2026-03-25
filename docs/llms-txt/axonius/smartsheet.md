# Source: https://docs.axonius.com/docs/smartsheet.md

# Smartsheet

Smartsheet is a cloud-based work management platform that empowers collaboration, drives better decision making, and accelerates innovation.

## Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Groups.svg) Groups | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Licenses.svg) Licenses |  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_settings.svg) Application Settings |  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Permissions.svg) Permissions

## Before You Begin

### Authentication Methods

* API Token
* OAuth2

### APIs

Axonius uses the following APIs:

* [Smartsheet OpenAPI Reference](https://developers.smartsheet.com/api/smartsheet/openapi)
* [Smartsheet SDKs and Samples](https://developers.smartsheet.com/api/smartsheet/guides/additional-resources)
* [Smartsheet SDK for Python](https://github.com/smartsheet-platform/smartsheet-python-sdk/blob/master/ADVANCED.md#working-with-smartsheetgovcom-accounts)

### Required Permissions

* When authenticating with OAuth2, the required scope for Request an Authorization Code is `READ_USERS`.
* *(Relevant only to accounts with Axonius SaaS Applications)* When adding a **Username** and **Password** to the connection parameters, the user must have `administrator` permissions and the `System Admin` role.

  <Callout icon="📘" theme="info">
    **Note**

    While to access SaaS data, Application Settings and Licenses you need to grant roles and/or permissions that include write capabilities, the adapter only actually reads data from the application.
  </Callout>

### Setting Up the Integration

To fetch Application Settings and Licenses, you must create a user account on Smartsheet.

**Guidelines for creating a user account:**

* It is recommended to retrieve the **Username** and **Password** parameters from the user account created specifically to work with Axonius.
* The password length should be at least 32 characters.
* Configuring user roles:
  * Enable: `System Admin`
  * Disable: `System Licensed User`
* If Single-Sign-on is enabled and the 'Email + Password option' is disabled, it is recommended to retrieve the Username and Password from a user account maintained by the SSO solution.

#### Creating an Application Access Token

<Callout icon="🚧" theme="warn">
  Note

  This process is required only if you authenticate with an **API Token**.
</Callout>

To retrieve the **Token** parameter, follow these steps:

1. Login to Smartsheet as the user dedicated to working with Axonius.
2. Click the user's avatar and select **Personal Settings**.
3. Navigate to **API Access** and generate a new access token.
4. Copy the token and paste it into the Axonius **Token** field.

## Deploying the Adapter in Axonius

### Required Parameters

1. **Authentication Method** - Select **API Token** or **OAuth2**. Select the relevant tab below to view the required fields for each method.

   <Tabs>
     <Tab title="API Token authentication">
       1. **Token** - The application access token created for the Axonius application.

          ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/smartsheet_api%20token.png)
     </Tab>

     <Tab title="OAuth Authentication">
       1. **Application Client ID** and **Application Client Secret** - The OAuth credentials required for OAuth access to Smartsheet. For more information, see [Request an Authorization Code](https://smartsheet.redoc.ly/#section/OAuth-Walkthrough/Request-an-Authorization-Code).

       2. **Refresh Token** - Enter the value of the Refresh Token issued by your Smartsheet instance. For more information, see [Get or Refresh an Access Token](https://smartsheet.redoc.ly/#section/OAuth-Walkthrough/Get-or-Refresh-an-Access-Token).

          ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/smartsheet_oauth2.png)
     </Tab>

     <Tab title="Username and Password">
       **This is relevant only to accounts with Axonius SaaS Applications, and only for fetching Application Settings and Licenses.**
       To fetch these assets, **in addition to** API Token/OAuth authentication, you must also provide these parameters:

       1. **Username** and **Password** - The user credentials of the user account you created when setting up the adapter integration.
       2. **Username** and **Password** - The user credentials of the user account you created when setting up the adapter integration.
       3. **2FA Secret Key** - If you access Smartsheet through an SSO solution that requires multi-factor authentication, you must generate a secret key in that solution and paste it here. See instructions for performing this action in [Okta](/docs/okta#step-5-enable-multifactor-authentication-saas-management) (applies to all adapters with this capability).
     </Tab>
   </Tabs>

### Optional Parameters

1. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

* **Fetch Group Data** - Select this option to fetch group data for Smartsheet users.
* **Parse Last Logon As Last Seen** - Select this option to populate the "Last Seen" field with the value of "Last Logon".
* **Fetch Application settings and Licenses** *(default: enabled)* - Disable this option if you **don't** want to fetch Application Settings and Licenses.

<br />