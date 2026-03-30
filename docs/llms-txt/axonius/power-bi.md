# Source: https://docs.axonius.com/docs/power-bi.md

# Microsoft Power BI

Microsoft Power BI is a business analytics tool for visualizing and sharing data insights across an organization.

**Related Enforcement Actions:**

* [Microsoft Azure - Send Assets to Microsoft Power BI](/docs/send-data-to-power-bi)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Groups
* Compute Services

## Parameters

1. **Azure Tenant ID**, **Azure Client ID**, **Azure Client Secret**, **Cloud Environment** *(required)* - See details under [Microsoft Entra ID](/docs/microsoft-azure-active-directory-ad#parameters).

2. **Azure Oauth - Authorization Code** (*required*) - The authorization code to connect to Microsoft Power BI. Learn how to [generate the OAuth Authorization Code](#generate-the-oauth-authorization-code).

3. **Azure OAuth - Redirect URI / Reply URL** (as required) - The location where the authorization server sends the user once the Azure has been successfully authorized and granted an authorization code or an access token. For more information, see [Redirect URI (reply URL) restrictions and limitations](https://learn.microsoft.com/en-us/entra/identity-platform/reply-url).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **API Type** *(default: Commercial)* - Select the API type. When a government entity is selected, the data is sent to *app.powerbigov.us* for government use instead of *app.powerbi.com*.

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![PowerBI\_Adapter(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PowerBI_Adapter\(1\).png)

## Generate the OAuth Authorization Code

To authenticate with OAuth, you must generate an OAuth Authorization Code for this adapter setup.

**Generate the OAuth Authorization Code**

1. Copy and paste the following URL into a browser window. Make sure to add the Tenant ID, Client ID, and Redirect URI that you used earlier in this setup and save the URL for later use:
   `https://login.microsoftonline.com/TENANT/oauth2/v2.0/authorize?client_id=CLIENT_ID&scope=https://graph.microsoft.com/.default&redirect_uri=REDIRECT_URI&response_mode=query&response_type=code`

2. Authorize, if required.

3. Copy the value for the code parameter in the changed URL. This is the entire string in the URL between `code=` and `&session_state` and it can be quite long.
   ![AuthorizationCodeParameter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AuthorizationCodeParameter.png)

4. Back in Axonius, paste the copied code into the **Azure OAuth - Authorization Code** field.
   Get the redirect URL:
   1. In Microsoft Azure, navigate to App Registrations and select your application for this integration.
   2. On the left panel, navigate to **Manage `>` Authentication**.
   3. In the Web area, copy one of the redirect URIs.
   4. Back in Axonius, paste the copied Redirect URI into the **Azure OAuth - Redirect URI/Reply URL** field.
      ![RedirectURI(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RedirectURI\(1\).png)

## APIs

Axonius uses the following APIs:

* [Get Groups](https://learn.microsoft.com/en-us/rest/api/power-bi/groups/get-groups)
* [Get Group Users](https://learn.microsoft.com/en-us/rest/api/power-bi/groups/get-group-users)
* [Get Dataflows](https://learn.microsoft.com/en-us/rest/api/power-bi/dataflows/get-dataflows)

## Required Permissions

* To connect with delegated permissions, you must register an Entra ID application with Power BI.
* The application requires the following delegated permissions: Power BI Service: Dataflow\.Read.All and Workspace.Read.All.

![PowerBI\_Permissions](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PowerBI_Permissions.png)

## Supported From Version

Supported from Axonius version 6.1