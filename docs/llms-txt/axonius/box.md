# Source: https://docs.axonius.com/docs/box.md

# Box Platform

Box Platform provides data security, file sharing, collaborating, and content management tools. Box Platform provides access to Box APIs.

### Asset Types Fetched

* Users, Roles, Groups, Application Settings, Permissions

## Resources Required by Asset Type

The following connection parameters, advanced settings, permissions, and configurations are required to fetch each asset type.

Search by Asset Type to find the resources required for your specific needs.

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Asset Type
      </th>

      <th>
        [Connection Parameters](/docs/box#connecting-the-adapter-in-axonius)
      </th>

      <th>
        [Advanced Settings](/docs/box#advanced-settings)
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
        Users
      </td>

      <td>
        * Box Platform enterprise ID
        * Client ID
        * Box Platform private key configuration file
      </td>

      <td>
        No specific setting required
      </td>

      <td>
        * Read and write all files and folders stored in Box
        * Manage users
        * Manage groups
        * Manage enterprise properties
      </td>

      <td>
        [Creating an Application](/docs/box#creating-an-application)
      </td>
    </tr>

    <tr>
      <td>
        Roles
      </td>

      <td>
        * Box Platform enterprise ID
        * Client ID
        * Box Platform private key configuration file
      </td>

      <td>
        No specific setting required
      </td>

      <td>
        No specific permission required
      </td>

      <td>
        [Creating an Application](/docs/box#creating-an-application)
      </td>
    </tr>

    <tr>
      <td>
        Groups
      </td>

      <td>
        * Box Platform enterprise ID
        * Client ID
        * Box Platform private key configuration file
      </td>

      <td>
        Fetch Groups
      </td>

      <td>
        No specific permission required
      </td>

      <td>
        [Creating an Application](/docs/box#creating-an-application)
      </td>
    </tr>

    <tr>
      <td>
        Application Settings
      </td>

      <td>
        * Box Platform enterprise ID
        * Client ID
        * Box Platform private key configuration file
        * Additional parameters - see note below
      </td>

      <td>
        Fetch Application Settings
      </td>

      <td>
        * Co-admin permissions with access to Reports and Settings
        * Read-only access to your organization’s settings and application
        * Manage users
        * Manage groups
        * Manage enterprise properties
      </td>

      <td>
        [Creating an Application](/docs/box#creating-an-application)
        [Creating a User Account](/docs/box#creating-a-user-account)
      </td>
    </tr>

    <tr>
      <td>
        Permissions
      </td>

      <td>
        * Box Platform enterprise ID
        * Client ID
        * Box Platform private key configuration file
      </td>

      <td>
        No specific setting required
      </td>

      <td>
        No specific permission required
      </td>

      <td>
        [Creating an Application](/docs/box#creating-an-application)
      </td>
    </tr>
  </tbody>
</Table>

<Callout icon="📘" theme="info">
  **Fetching Application Settings**

  1. Some high-privilege settings cannot be fetched with client credentials (Box Platform enterprise ID, Client ID and private key configuration file) alone. These settings require additional parameters: Box Login URL, Username, Password, 2FA Secret Key (if required by your organization), and Use SSO (if required by your organization). See [Connecting the Adapter in Axonius](/docs/box#connecting-the-adapter-in-axonius) for more information on these parameters.
</Callout>

### APIs

Axonius uses the [Box REST API - List enterprise users](https://developer.box.com/reference/get-users/).

## Setting Up Box Platform to Work with Axonius

### Creating an Application

<Callout icon="📘" theme="info">
  Note

  Only users with a Developer account can create an application.
</Callout>

The values supplied in [Client ID and Box Platform private key configuration file](/docs/box#connecting-the-adapter-in-axonius) refer to the generated Client ID and private key configuration file of your Custom App.

1. For details on setting up a Custom App using JWT authentication, see [Box Guides - Setup with JWT](https://developer.box.com/guides/authorization/custom-app-approval/). The following App Scopes (permissions) are required for creating a Custom App:

* Read and write all files and folders stored in Box
* Manage groups
* Manage enterprise properties
* Manage users

2. Select **Configuration** from the left sidebar in your application, scroll down to **App Access Level**, and select **App + Enterprise Access**. This enables your application to access all users and manage enterprise settings, content, and users.

<Image align="center" width="auto" alt="AppAccessLevel" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-SX9WBXI1.png" height="auto" />

3. Create a configuration file from the Developer Console. This file will include the keypair as well as a number of other application details that are used during authentication.

   1. Select **Configuration** from the left sidebar in your application and scroll down to **Add and Manage Public Keys**. ![AddAndManagePublicKeys](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-OADHY47B.png)
   2. Click **Generate a Public/Private Keypair** to have Box generate a keypair. This triggers the download of a JSON configuration file that you can move to your application code.
   3. Upload this file as the **Box Platform private key configuration file**.

4. To get the **Client ID**, log into your Box developer console and select **Edit Application** for the application you're working with.

5. In the OAuth 2.0 Parameters section of the configuration page, find the item labelled `client_id`. The text of that item is your application's Client ID.

### Creating a User Account

<Callout icon="💡" theme="warn">
  Notes

  * This is required only to fetch some Application Settings. While to access Application Settings data you need to grant roles and/or permissions that include write capabilities, the adapter only actually reads data from the application.

  * It is recommended for the username and password to be derived from a newly created user account dedicated for the usage of Axonius SaaS Applications. Retrieve the username and password from that user account.

  * When single-sign-on is enabled, and direct login flow is disabled, then it is recommended to derive the username and password from a user account maintained by the single-sign-on solution.
</Callout>

1. Log into Box as an administrator and navigate to **Admin Console`>` Users & Group.**

2. Click the **+ User** button.

3. Clear *Allow this user to sync files between Box and the user's desktop*.

4. Click **Add User**.

5. Look up for the newly created user, click on its options button, and select **Change User Settings**.

6. Check *Exempt this user from maximum allowed devices*.

7. Check  *Exempt this user from 2-step login verification*.

8. Check *User is granted the following administrative privileges*.

9. Clear the following:

   1. *Manage users*
   2. *Manage groups*
   3. *View users' content*
   4. *Edit users' content*
   5. *Log in to users' accounts*
   6. *Create, edit and delete automations for your company*
   7. *Create and edit metadata templates for your company*

10. Check the following:
    1. *View settings and apps for your company*
    2. *Edit settings and apps for your company*
    3. *Run new reports and access existing reports*
    4. *View automations set up for your company*

11. Click **Save**.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters. Refer to [Resources Required by Asset Type](/docs/box#resources-required-by-asset-type) for the parameters required for specific asset types.

* **Box Platform enterprise ID** - Specify your Box enterprise account ID. The Box Platform enterprise ID is located in the Enterprise settings view. Click the **Admin Console** link from the top of your Box account. Then choose the Gear icon / Enterprise settings. Your Enterprise ID may also be located in the Account and Billing tab of the Admin Console.
* **Client ID** and **Box Platform private key configuration file** - The Client ID and private key configuration file that provides the [Required Permissions](/docs/box#resources-required-by-asset-type) to fetch assets. Refer to [Creating an Application](/docs/box#creating-an-application) for instructions on how to obtain these parameters.
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

**Parameters required to fetch SaaS Application Settings:**

* **Box Login URL** - The URL as it appears in the browser's address bar after signing-in.
* **Username and Password** - The username and the password of the dedicated account created for Axonius SaaS Applications.
* **2FA Secret Key** - The secret generated in the adapter for setting up 2-factor authentication (if your organization uses it) for the adapter user created to collect SaaS Applications Settings.
* **Use SSO** - Select this option if your organization uses SSO to log in to Box Platform. When you check Use SSO enter the SSO username, password, and the 2FA from the SSO provider, in these configuration fields, instead of BOX credentials.

<Image align="center" width="auto" alt="BoxPlatformAddConnection" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-GDTOFUVL.png" height="auto" />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  **Note**

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Groups** - Select this option to fetch Box groups.
2. **Fetch User Last Login Time** - Select this option to fetch the last time the user logged in.
3. **Fetch Application Settings** - Select this option to fetch Application Settings.

<Callout icon="📘" theme="info">
  **Note**

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [Box - Send CSV](/docs/send-csv-to-box)
* [Box - Create/Update User](https://docs.axonius.com/axonius-help-docs/docs/box-platform-create-update-user)
* [Box - Create/Update User](https://docs.axonius.com/axonius-help-docs/docs/box-platform-create-update-user)

<br />