# Source: https://docs.axonius.com/docs/onelogin.md

# OneLogin

OneLogin's unified access management platform centralizes access across on-prem and cloud environments to give full control, management, and security for data, devices, and users.

### Asset Types Fetched

* Users
* All Application Extensions
* Roles
* Groups
* All Application Extension Instances
* SaaS Applications
* Admin Managed Extensions
* Application Addons
* User Initiated Extensions
* Admin Managed Extension Instances
* Application Addon Instances
* Application Keys
* User Initiated Extension Instances

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Client ID/Client Secret

### APIs

Axonius uses the [OneLogin API version 1](https://developers.onelogin.com/api-docs/1/getting-started/dev-overview).

### Permissions

The value supplied in [Client ID](#required-parameters) must have **Read All** or **Manage All** permission.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the OneLogin server.
2. **Client ID** and **Client Secret** - The API credentials that have the Required Permissions to fetch assets.

<Image alt="OneLogin" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OneLogin.png" />

### Optional Parameters

1. **SSO Provider** - If your organization uses OneLogin for SSO, you can set this select this check box (selected by default). For more information, see [Connecting your SSO Solution Provider](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider).

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Enrolled Factors** *(required, default: true)* - Select whether to fetch users who are enrolled in a multi-factor authentication policy.
2. **Comma-separated custom attributes** - Enter a case-sensitive comma-separated string of custom attribute fields to display in Axonius.
3. **Enable rate limit override settings** - Toggle on to enable rate limit override settings.
   1. **# of requests per seconds (below)** - Specify the number of requests allowed within the number of seconds specified (default: 2500).
   2. **Timeframe (seconds) for # of requests (above)** - Specify the number of seconds within which the number of requests are allowed (default: 60).
4. **Enable ingestion of SM-related entities** *(only for accounts with Axonius SaaS Applications)* - By default Axonius fetches entities from Axonius SaaS Applications. Clear this option to not fetch entities from Axonius SaaS Applications.
5. **Enable fetch of additional user details** *(required, default: true)* - By default Axonius fetches both user applications and user events. Disable this option to not fetch user applications and user events. You also have the capability to disable one of these options:
   * **Fetch user applications**
   * **Fetch user events**
6. **Enrich Roles with Privileges** - Select this option to enrich roles with privileges.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [Append to Comment - OneLogin](/docs/append-to-comment-onelogin)
* [Modify User State - OneLogin](/docs/modify-user-state-onelogin)
* [Modify User Custom Fields - OneLogin](/docs/modify-user-custom-fields-onelogin)
* [Modify User Status - OneLogin](/docs/modify-user-status-onelogin)
* [Logout User - OneLogin](/docs/logout-user-onelogin)
* [Set a New Password for User - OneLogin](/docs/set-new-password-onelogin)