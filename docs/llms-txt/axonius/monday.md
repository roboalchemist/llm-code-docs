# Source: https://docs.axonius.com/docs/monday.md

# Monday

[Monday.com](https://monday.com/) is a cloud-based workflow management platform that allows teams to build and manage projects.

Related Enforcement Actions:

* [Monday - Manage Users](/docs/monday-manage-users)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* All Application Extensions
* Roles
* Groups
* Licenses
* Application Settings
* All Application Extension Instances
* SaaS Applications
* Accounts/Tenants
* Application Resources
* Admin Managed Extensions
* Application Addons
* User Initiated Extensions
* Admin Managed Extension Instances
* Application Addon Instances
* Application Keys
* User Initiated Extension Instances

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.monday.com`)* - The hostname or IP address of the Monday.com server.

2. **API Token** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Account Name** - Your Monday account name.

4. **User Name** and **Password** - The credentials for a user account that has permission to fetch SaaS data.

5. **2FA Secret** - The secret generated in Monday for setting up multi-factor authentication for the Monday user created for collecting SaaS data.

6. **API Version** - Select which version of the Monday API you're using. You can select version **2023-07** (which is selected by default), **2024-01**, or **2024-10**.

7. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

8. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

9. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

10. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Monday\_Adapter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Monday_Adapter.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Monday Boards** - Select this option to fetch Monday boards from the account.
  * **Board Kind** - Select if you want to fetch Public, Private, or Shared board. Alternatively, you can select **No Filter** to fetch all Monday boards.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Monday.com platform API](https://developer.monday.com/api-reference/reference/about-the-api-reference).

## Required Permissions

**Note:** Additional permissions are only required in the Enterprise plan of Monday.com.

The value supplied in [Users](#parameters) must have permissions to read assets and requires writer permission to fetch SaaS data.

## Adapter Integration Setup

### Step 1: Create a User Account

* It is recommended for the username and password to be derived from a newly created user account dedicated for the usage of Axonius SaaS Applications. Retrieve the username and password from that user account.

<Callout icon="📘" theme="info">
  Note

  If single-sign-on is enabled and is not set to 'Using SSO authentication is optional', then it is recommended to derive the username and password from a user account maintained by the single-sign-on solution.
</Callout>

* The password length should be at least 32 characters.
* The user account needs to have MFA disabled.
* Set User Type to Admin.

### Step 2: Generate the API Token

The API Token needs to be derived from the newly create user account.

1. Log into Monday as the user.
2. From the profile menu, select **Admin**.
3. Go to API, scroll down to the API V2 Token section, and click **Generate**.
4. Copy and save the API Token.

## Supported From Version

Supported from Axonius version 4.5