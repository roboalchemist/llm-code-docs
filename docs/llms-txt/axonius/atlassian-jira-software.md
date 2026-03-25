# Source: https://docs.axonius.com/docs/atlassian-jira-software.md

# Atlassian (Formerly Atlassian Jira Software)

Atlassian (formerly Atlassian Jira Software) is a work management tool for various use cases, from requirements and test case management to agile software development.

This adapter lets you fetch data and get visibility and security across all Atlassian accounts and products at your company, including the users managed under the following cloud products:

* Jira Software
* Jira Work Management
* Jira Service Management
* Confluence
* Bitbucket
* Trello
* Opsgenie

### Asset Types Fetched

* Users, Roles, Groups, Application Settings, Accounts/Tenants, Application Resources, Permissions, Secrets

## Resources Required by Asset Type

The following connection parameters, advanced settings, permissions, and configurations are required to fetch each asset type.

Search by Asset Type to find the resources required for your specific needs.

<Callout icon="📘" theme="info">
  Note

  To fetch Roles, Groups, Application Settings, and Accounts/Tenants, you must have Axonius SaaS Applications configured in your environment.
</Callout>

<br />

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Asset Type
      </th>

      <th>
        [Connection Parameters](/docs/atlassian-jira-software#connecting-the-adapter-in-axonius)
      </th>

      <th>
        [Advanced Settings](/docs/atlassian-jira-software#advanced-settings)
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
        * Domain
        * User Name
        * API Token
        * Jira API Version
        * **Atlassian Admin API - Organization ID** and **Atlassian Admin API - API key** - required only to fetch organizational users
      </td>

      <td>
        No specific advanced setting required
      </td>

      <td>
        * ‘Jira Administrator’ or ‘Jira System Administrator’ global permission
        * ‘Browse Users and Groups’ global permission
        * ‘Administer Projects’ project permission (for all projects)

        **Permissions for non-admin accounts:** [see steps 7-8 in Creating a User Account](/docs/atlassian-jira-software#creating-a-user-account)
      </td>

      <td>
        * [Creating a user account](/docs/atlassian-jira-software#creating-a-user-account)
        * [Creating an API token](/docs/atlassian-jira-software#creating-an-api-token)
        * [Creating an Organization API Key](/docs/atlassian-jira-software#creating-an-organization-api-key) (required only to fetch organizational users)
      </td>
    </tr>

    <tr>
      <td>
        Roles
      </td>

      <td>
        * Domain
        * Jira API Version
        * User Name
        * API Token
      </td>

      <td>
        No specific advanced setting required
      </td>

      <td>
        * ‘Jira Administrator’ or ‘Jira System Administrator’ global permission
        * ‘Browse Users and Groups’ global permission
        * ‘Administer Projects’ project permission (for all projects)

        **Permissions for non-admin accounts:** [see steps 7-8 in Creating a User Account](/docs/atlassian-jira-software#creating-a-user-account)
      </td>

      <td>
        * [Creating a user account](/docs/atlassian-jira-software#creating-a-user-account)
        * [Creating an API token](/docs/atlassian-jira-software#creating-an-api-token)
      </td>
    </tr>

    <tr>
      <td>
        Groups
      </td>

      <td>
        * Domain
        * Jira API Version
        * User Name
        * API Token
      </td>

      <td>
        Fetch groups
      </td>

      <td>
        * ‘Jira Administrator’ or ‘Jira System Administrator’ global permission
        * ‘Browse Users and Groups’ global permission
        * ‘Administer Projects’ project permission (for all projects)

        **Permissions for non-admin accounts:** [see steps 7-8 in Creating a User Account](/docs/atlassian-jira-software#creating-a-user-account)
      </td>

      <td>
        * [Creating a user account](/docs/atlassian-jira-software#creating-a-user-account)
        * [Creating an API token](/docs/atlassian-jira-software#creating-an-api-token)
      </td>
    </tr>

    <tr>
      <td>
        Application Settings
      </td>

      <td>
        * Domain
        * Jira API Version
        * User Name

        [Additional parameters](/docs/atlassian-jira-software#required-parameters-application-settings):

        * Password
        * API Token
        * 2FA Secret Key (If your organization requires two-factor authentication to access Atlassian)
      </td>

      <td>
        Fetch settings
      </td>

      <td>
        * ‘Jira Administrator’ or ‘Jira System Administrator’ global permission
        * ‘Browse Users and Groups’ global permission
        * ‘Administer Projects’ project permission (for all projects)
      </td>

      <td>
        * [Creating a user account](/docs/atlassian-jira-software#creating-a-user-account)
        * [Creating an API token](/docs/atlassian-jira-software#creating-an-api-token)
      </td>
    </tr>

    <tr>
      <td>
        Accounts/Tenants
      </td>

      <td>
        * Domain
        * Jira API Version
        * User Name
        * API Token
      </td>

      <td>
        No specific advanced setting required
      </td>

      <td>
        * ‘Jira Administrator’ or ‘Jira System Administrator’ global permission
        * ‘Browse Users and Groups’ global permission
        * ‘Administer Projects’ project permission (for all projects)

        **Permissions for non-admin accounts:** [see steps 7-8 in Creating a User Account](/docs/atlassian-jira-software#creating-a-user-account)
      </td>

      <td>
        * [Creating a user account](/docs/atlassian-jira-software#creating-a-user-account)
        * [Creating an API token](/docs/atlassian-jira-software#creating-an-api-token)
      </td>
    </tr>

    <tr>
      <td>
        Application Resources
      </td>

      <td>
        * Domain
        * Jira API Version
        * User Name
        * API Token
      </td>

      <td>
        No specific advanced setting required
      </td>

      <td>
        * ‘Jira Administrator’ or ‘Jira System Administrator’ global permission
        * ‘Browse Users and Groups’ global permission
        * ‘Administer Projects’ project permission (for all projects)

        **Permissions for non-admin accounts:** [see steps 7-8 in Creating a User Account](/docs/atlassian-jira-software#creating-a-user-account)
      </td>

      <td>
        * [Creating a user account](/docs/atlassian-jira-software#creating-a-user-account)
        * [Creating an API token](/docs/atlassian-jira-software#creating-an-api-token)
      </td>
    </tr>

    <tr>
      <td>
        Permissions
      </td>

      <td>
        * Domain
        * Jira API Version
        * User Name
        * API Token
      </td>

      <td>
        Fetch permissions
      </td>

      <td>
        * ‘Jira Administrator’ or ‘Jira System Administrator’ global permission
        * ‘Browse Users and Groups’ global permission
        * ‘Administer Projects’ project permission (for all projects)

        **Permissions for non-admin accounts:** [see steps 7-8 in Creating a User Account](/docs/atlassian-jira-software#creating-a-user-account)
      </td>

      <td>
        * [Creating a user account](/docs/atlassian-jira-software#creating-a-user-account)
        * [Creating an API token](/docs/atlassian-jira-software#creating-an-api-token)
      </td>
    </tr>

    <tr>
      <td>
        Secrets
      </td>

      <td>
        * Domain

        * Jira API Version

        * User Name

        * API Token

        * **Atlassian Admin API - Organization ID** and **Atlassian Admin API - API key** with the read:tokens:admin permission
      </td>

      <td>
        Fetch API tokens
      </td>

      <td>
        * ‘Jira Administrator’ or ‘Jira System Administrator’ global permission

        * ‘Browse Users and Groups’ global permission

        * ‘Administer Projects’ project permission (for all projects)

        * read:tokens:admin permission
      </td>

      <td>
        * [Creating a user account](/docs/atlassian-jira-software#creating-a-user-account)

        * [Creating an API token](/docs/atlassian-jira-software#creating-an-api-token)
      </td>
    </tr>
  </tbody>
</Table>

### APIs

Axonius uses the [Jira Cloud platform REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-users-search-get).

## Setting Up Atlassian to Work with Axonius

To fetch all asset types, set up the following:

1. [Create a user account](/docs/atlassian-jira-software#creating-a-user-account)
2. [Create an API token](/docs/atlassian-jira-software#creating-an-api-token)

### Creating a User Account

<Callout icon="📘" theme="info">
  Notes

  1. While to access application data you need to grant roles and/or permissions that include write capabilities, the adapter only actually reads data from the application.
  2. (Relevant for Application Settings only) If single-sign-on is enabled, it is recommended to derive the username and password from a user account maintained by the single-sign-on solution.
</Callout>

You must have the Jira Administrator or Jira System Administrator global permission to be able to manage users in Jira applications.

To create a new user, from the Atlassian Administration:

1. Navigate to **Administration** `>` **User Management**.

2. In the User browser, select **Create User**.

3. Enter the Username, Password, Full Name, and Email address.

   1. The password length should be at least 32 characters.
   2. The user account needs to have MFA disabled.

4. Select all Jira applications.

5. Select **Create**.

6. Set admin permissions:

   1. Go to **Settings** `>` **Administrators**.
   2. Click **Add administrators**.
   3. Enter the created Atlassian account email address and click **Grant access**.

7. **To fetch data from Jira if the created account has not been set as an admin:** edit that user and add them to groups that provide the following permissions:

   * Administer Jira global permission
   * Browse users and groups global permission
   * Administer projects project permission (for all projects)

8. **To fetch data from Confluence if the created account has not been set as an admin:** edit that user and add them to groups that provide the following permissions:

   * Permission to access the Confluence site ('Can use' global permission)
   * 'View' permission for all spaces

### Creating an API Token

1. Login to *admin.atlassian.com* with the Atlassian user account you created, and generate an API token, using the following URL: `https://id.atlassian.com/manage/api-tokens#`
2. Select **Create API token**.
3. Select a label that is short and easy to remember, and click **Create**.
4. Copy the generated API token.
5. In Axonius, in the **Add Connection** drawer, paste the copied token in the **API Token** field.

### Creating an Organization API Key

<Callout icon="💡" theme="warn">
  Note

  This is only required to fetch Secrets and Users' organizational information.
</Callout>

1. Login to a\_dmin.atlassian.com\_ with the Atlassian user account you created.
2. Select your organization (if you have more than one).
3. Select **Settings** `>` **API keys**.
4. Select **Create API key** on the top right.
5. Enter a name that you can easily remember to identify the API key.
6. Set the latest date possible for the key expiration date. Usually, the maximum is one year.
7. Select **Create** to save the API key.
8. Copy the generated **Organization ID** and **API key**.
9. Select **Done**. The key will appear in your list of API keys.
10. In Axonius, paste the copied values in the **Atlassian Admin API - API Key** and **Atlassian Admin API - Organization ID** fields.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters - All Asset Types

1. **Domain** - The hostname or IP address of the Jira Software server.
2. **User Name** - The username for a user account that has the required permissions to fetch assets.
3. **API Token** - An API Token associated with a user account that has the required permissions to fetch assets. **Note:** The API Token is **not** the same as the Admin Key.
4. **Jira API Version** *(default: V3)* - Select your Jira API version.

### Required Parameters - Application Settings

1. **Password** - The password for the Atlassian user account.
2. **2FA Secret Key** - If your organization requires two-factor authentication to access Atlassian, and you want to fetch Application Settings from Atlassian, you will need to generate a secret key in a 2FA solution such as Google authenticator and paste it here. See for example [Set Up Google Authenticator](/docs/okta#step-5-set-up-google-authenticator) in the Okta adapter documentation.

### Required Parameters - Fetching Secrets and Users Organizational Data

[Atlassian Admin API - Organization ID and Atlassian Admin API - API key](/docs/atlassian-jira-software#creating-an-organization-api-key)

<Image align="center" border={false} width="953px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-OVG2D3I0.png" height="auto" />

### Optional Parameters

The following parameters are optional:

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

<br />

In **Advanced Settings**, at the top of the Advanced Configuration tab, you can choose asset types that are relevant to specific advanced configurations.

* From the dropdown, select one or more asset types.
* The relevant advanced configurations are displayed.
* Next to certain configurations, you can find a small info icon. Hover over the icon to see more information.
* The Advanced Configuration page is divided into sections, which can be collapsed to make it easier to navigate.

<br />

### Fetch Settings

1. **Do not fetch disabled users** - Select whether to exclude fetching disabled users or not.
2. **Fetch projects and project roles** - Select this option to fetch projects and project roles (available only for customers who have Axonius SaaS Applications enabled).
3. **Fetch groups** - Select to fetch users groups details (available only for customers who have Axonius SaaS Applications enabled).
4. **Fetch permissions** - Select to fetch permissions configured for the Atlassian accounts in your organization (available only for customers who have Axonius SaaS Applications enabled).
5. **Fetch settings** - Select to fetch settings configured for the Atlassian accounts in your organization (available only for customers who have Axonius SaaS Applications enabled).
6. **Fetch API tokens** - Select to fetch API tokens as Secrets.

### Parsing Settings

1. **Distinguish User ID From Different Domains** - When selected, the Atlassian domain is appended to the ID of each user, to allow Axonius to fetch the same users from multiple sites without overriding the data.
2. **Users per page (default: 50)** - Enter the number of users listed per a single request. Atlassian might limit the maximum number of users per page. If the number you enter is higher than the limit, the fetch will fail. Therefore make sure the value you enter is lower than that.
3. **Filter users without site access** - Select to exclude users who cannot access the Atlassian site.
4. **Number of parallel requests** - Specify the maximum parallel request this adapter will create when connecting the Atlassian server. This setting lets you control the performance of this adapter.

<br />

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

[Jira Software - Create User](/docs/jira-software-create-user)

[Jira Software - Delete User](/docs/jira-software-delete-user)

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| V3      | Yes       | --    |