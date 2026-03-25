# Source: https://docs.axonius.com/docs/jamf-pro.md

# Jamf Pro

Jamf Pro is an enterprise mobility management (EMM) tool that provides unified endpoint management for Apple devices.

**Use cases the adapter solves**

Jamf Pro is a powerful endpoint management solution that provides a robust inventory of our managed Apple devices in Axonius. More importantly, by combining Jamf Pro with network/infrastructure data coming from additional adapters, Axonius can identify unmanaged or even rogue devices on the network.

**Data retrieved by Jamf Pro**

Axonius collects common device information such as hostname, IPs, MAC address, and serial number. It also collects information unique to Jamf such as device policies, profiles, and groups. The adapter can be configured to collect additional information, such as user data and mobile devices.

<Callout icon="📘" theme="info">
  Note:

  Official Jamf recommendation is to limit the number of fetches for the Jamf Pro adapter to one fetch per day, in order to preserve the stability of the Jamf cloud.
</Callout>

### Asset Types Fetched

* Devices, Users, Software, Accounts/Tenants, Application Settings

## Resources Required by Asset Type

The following connection parameters, advanced settings, permissions, and configurations are required to fetch each asset type.

Search by Asset Type to find the resources required for your specific needs.

<Callout icon="📘" theme="info">
  Note

  When fetching Users, different permissions are required for the Jamf Classic API and the Jamf Pro API because each API fetches different data about users.
</Callout>

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Asset Type
      </th>

      <th>
        [Connection Parameters](/docs/jamf-pro#connecting-the-adapter-in-axonius)
      </th>

      <th>
        [Advanced Settings](/pl/docs/jamf-pro#advanced-settings)
      </th>

      <th>
        Permissions
      </th>

      <th>
        Additional Configuration
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Devices
      </td>

      <td>
        * Jamf Domain
        * User Name and Password **or** User Client Credentials
      </td>

      <td>
        Fetch mobile devices (to fetch mobile devices in addition to standard devices)
      </td>

      <td>
        **API: Pro/Classic**
        Read Computers

        *When fetching mobile devices:*
        **API: Pro/Classic**
        Read Mobile Devices
      </td>

      <td>
        * [Creating a User by Connecting to the Jamf Admin Panel](/pl/docs/jamf-pro#creating-a-user-by-connecting-to-the-jamf-admin-panel)
        * [Obtaining a Client ID and Client Secret](https://learn.jamf.com/bundle/jamf-pro-documentation-current/page/API_Roles_and_Clients.html)
      </td>
    </tr>

    <tr>
      <td>
        Users
      </td>

      <td>
        * Jamf Domain
        * User Name and Password **or** User Client Credentials
      </td>

      <td>
        Fetch Users
      </td>

      <td>
        **API: Pro**

        * Read Accounts
        * Read Jamf Pro User Accounts & Groups
        * Read Users

        **API: Classic**
        Read Users

        *When fetching department and building information:*
        **API: Pro**

        * Read Buildings
        * Read Departments
      </td>

      <td>
        * [Creating a User by Connecting to the Jamf Admin Panel](/pl/docs/jamf-pro#creating-a-user-by-connecting-to-the-jamf-admin-panel)
        * [Obtaining a Client ID and Client Secret](https://learn.jamf.com/bundle/jamf-pro-documentation-current/page/API_Roles_and_Clients.html)
      </td>
    </tr>

    <tr>
      <td>
        Software
      </td>

      <td>
        * Jamf Domain
        * User Name and Password **or** User Client Credentials
      </td>

      <td>
        No specific setting is required
      </td>

      <td>
        No specific permission is required
      </td>

      <td>
        * [Creating a User by Connecting to the Jamf Admin Panel](/pl/docs/jamf-pro#creating-a-user-by-connecting-to-the-jamf-admin-panel)
        * [Obtaining a Client ID and Client Secret](https://learn.jamf.com/bundle/jamf-pro-documentation-current/page/API_Roles_and_Clients.html)
      </td>
    </tr>

    <tr>
      <td>
        Accounts/Tenants
      </td>

      <td>
        * Jamf Domain
        * User Name and Password **or** User Client Credentials
      </td>

      <td>
        No specific setting is required
      </td>

      <td>
        No specific permission is required
      </td>

      <td>
        * [Creating a User by Connecting to the Jamf Admin Panel](/pl/docs/jamf-pro#creating-a-user-by-connecting-to-the-jamf-admin-panel)
        * [Obtaining a Client ID and Client Secret](https://learn.jamf.com/bundle/jamf-pro-documentation-current/page/API_Roles_and_Clients.html)
      </td>
    </tr>

    <tr>
      <td>
        Application Settings
      </td>

      <td>
        * Jamf Domain
        * User Name and Password **or** User Client Credentials
        * 2FA Secret Key
        * Bypass SSO
      </td>

      <td>
        No specific setting is required
      </td>

      <td>
        * The Jamf Pro user must have Read permissions to all items under Jamf Pro Server Settings and access to the Admin Portal (granted by default)
        * If you are using Bypass SSO, you must have Update permission over ‘SSO setting’ configured in Jamf.
        * Specific permissions for Client Credentials - see below
      </td>

      <td>
        * [Creating a User by Connecting to the Jamf Admin Panel](/pl/docs/jamf-pro#creating-a-user-by-connecting-to-the-jamf-admin-panel)
        * [Obtaining a Client ID and Client Secret](https://learn.jamf.com/bundle/jamf-pro-documentation-current/page/API_Roles_and_Clients.html)

        <br />
      </td>
    </tr>
  </tbody>
</Table>

### Additional Requirements for Fetching Application Settings

When using Client Credentials to fetch Application Settings, the following configurations are required:

* Access to the following API endpoints:
  * /api/v3/sso
  * /api/v2/sso/cert
  * /api/v1/device-communication-settings
  * /api/v4/enrollment
  * /api/v2/smtp-server
  * /api/v1/log-flushing
* An API role with specific Read permissions for your Jamf Pro instance, depending on the API you're using.
  * When using the Jamf Pro API, the following Read permissions are required:
    * SSO Settings: Read
    * Enrollment Settings: Read
    * SMTP Server Settings: Read
  * When using Jamf Classic API, the following Read permissions are required:
    * Device Communication Settings: Read
    * Log Flushing: Read

### Permissions for Enforcement Actions

To successfully run [Enforcement Actions](/docs/jamf-pro#related-enforcement-actions) with this adapter, the following permission is required (for both API types):

* Update - Smart Computer Groups

### APIs

Axonius supports the [Jamf Classic API](https://developer.jamf.com/jamf-pro/docs) and [Jamf Pro API](https://developer.jamf.com/jamf-pro/docs/jamf-pro-api-overview).

<Callout icon="📘" theme="info">
  Note

  This adapter supports token-based authentication for Jamf Pro API access.
</Callout>

## Creating a User by Connecting to the Jamf Admin Panel

Before connecting the adapter, you need to create a new user on Jamf Pro and assign it the relevant permissions.

1. Log in to the **Jamf Pro admin** panel and navigate to the **Settings** panel.
2. Select **Jamf Pro User Accounts & Groups**.
3. Click **New** to create a new user and then select **Create Standard Account `>` Next**. ![CreateStandardAccount](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-1KMS6NOX.png)
4. Fill in the details for this account. Make sure to select **Custom** from the **Privilege Set** dropdown, and select **Full Access** from the **Access Level** dropdown. ![AccountDetailsPrivilegeSet](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-WUBPSD0J.png)
5. Navigate to the **Privileges** tab. Under **Jamf Pro Server Objects**, select the **Read** option for each object displayed. ![ServerObjectsReadPermissions](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-QMUJQOQ6.png)
6. Click **Save**.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Jamf Domain** - The hostname of the Jamf Pro server. This field format is 'https\://\[instance].jamfcloud.com'.
2. Either of the following credential pairs:

   1. **User Name** and **Password** - The credentials for a user account that has the required permissions to fetch assets via the API.
   2. **Use Client Credentials** - Enable this option to authenticate with a **Client ID** and **Client Secret**. For more information about obtaining a Client ID and Client Secret, see [API Roles and Clients](https://learn.jamf.com/bundle/jamf-pro-documentation-current/page/API_Roles_and_Clients.html).
3. **If you access Jamf Pro through an SSO solution that requires 2-factor authentication**, the following parameters are required to fetch Application Settings (only):
   1. **2FA Secret Key** - Generate a secret key within the SSO solution you're using and paste it here. For example, see [Set Up Google Authenticator for the Okta adapter](/docs/okta#step-5-set-up-google-authenticator).
   2. **Bypass SSO (default: switched off)** - Select it if the newly created user account is allowed to bypass SSO according to the Jamf instance settings. Note that Bypass SSO follows the Failover URL.

<Image alt="JamfProAddConnection" border={false} src="https://files.readme.io/bfaa7a476acc9a6af5247c59929c3655a374e1cd2a287b7d0423e91d6b27d103-image.png" />

### Optional Parameters

The following parameters are optional:

1. **Tenant Tag** - Specify a tag name to tag all devices fetched from this adapter connection.
2. **HTTP Proxy** and **HTTPS Proxy** - A proxy to use when connecting to the value supplied in Jamf Domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Devices** - This adapter fetches devices by default. Clear this option to **not** fetch devices.
2. **Fetch device from Advanced Computer Search with the following name** (optional) - Enter the name of an Advanced Computer Search endpoint to fetch devices from. If you don’t provide an endpoint, all devices will be fetched from the standard API.
3. **Parse device hostnames from Extension Attributes** - Select this option to override each device's host name with the value found in Extension Attributes, if provided.
4. **Fetch Users (default: true)** - Select this option to fetch users - for both Classic and Pro API connections. If this setting is disabled, the adapter will not fetch users at all.
5. **Fetch department of users** - Select whether to fetch the names of buildings and departments of users for this adapter connection.
6. **Fetch history of applied policies for devices** - Select whether to fetch the history of policies that were applied to devices.
7. **Fetch mobile devices (required, default: true)** - Select whether to fetch mobile devices in addition to standard devices for this adapter connection.
8. **Fetch Enrollment Devices** - Select this option to fetch enrollment devices.
9. **Use pro API** - Select this option to use JAMF Pro API. Clear this option to use the JAMF Classic API. Note that On-prem Jamf servers require the Pro API.
10. **Async chunks in parallel** - The number of chunks to fetch in parallel when working with the Classic API. Note that for Jamf Pro **cloud** instances (not on-prem), the maximum number of async requests is 5. Even if a higher value is entered, the value of 5 is used. This is per Jamf official recommendation. Higher values are possible only for Jamf Pro on-prem.
11. **Items to not fetch** - Select one or more fields to exclude from the Devices fetch. This option only applies to devices fetched from the Pro API.
12. **Enrich software with version info** - Select this option to enrich software with the following fields: 'Current version release date', 'Next version release date', 'Newer version count'.
13. **List of Device IDs to filter** - Enter a comma-separated list of device IDs for specific devices that you want to fetch.
14. **Fetch application usage** - Enable this option to applications' usage history.
    * **Number of days to look back** - Set the number of days to look back when fetching usage history.

<Callout icon="📘" theme="info">
  Note:

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [Jamf Pro - Add or Remove Assets to/from Group](/docs/add-devices-to-jamfpro)
* [Jamf Pro - Lock Device](/docs/lock-device)
* [Jamf Pro - Delete Device](https://docs.axonius.com/axonius-help-docs/docs/jamf-delete-device)
* [Jamf Pro - Update Device](https://docs.axonius.com/axonius-help-docs/docs/update-jamf-device)

<br />