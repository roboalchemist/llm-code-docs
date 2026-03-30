# Source: https://docs.axonius.com/docs/github.md

# GitHub

GitHub provides hosting for software development version control using Git, including distributed version control and source code management (SCM) functionality.

### Asset Types Fetched

<Table>
  <thead>
    <tr>
      <th>
        Asset Type
      </th>

      <th>
        Requirements and Authentication
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Devices, Users, Aggregated Security Findings, Software, Roles, Groups, Secrets, Tickets, Groups
      </td>

      <td>
        * No specific requirements
        * Authenticate either with an Authorization Token or with the GitHub App
      </td>
    </tr>

    <tr>
      <td>
        Alerts/Incidents, Permissions, SaaS Applications, All Application Extensions, All Application Extension Instances, Admin Managed Extensions, Application Addons, User Initiated Extensions, Admin Managed Extension Instances, Application Addon Instances, Application Keys, User Initiated Extension Instances
      </td>

      <td>
        * Axonius SaaS Applications (product)
        * Authenticate either with an Authorization Token or with the GitHub App
      </td>
    </tr>

    <tr>
      <td>
        Application Resources
      </td>

      <td>
        * To fetch GitHub projects as Application Resources assets, you must have the **Axonius SaaS Applications** product.
        * Authenticate either with an Authorization Token or with the GitHub App
      </td>
    </tr>

    <tr>
      <td>
        Application Settings
      </td>

      <td>
        Authenticate with User Name and Password
      </td>
    </tr>

    <tr>
      <td>
        Licenses
      </td>

      <td>
        * Authenticate either with an Authorization Token **OR** with the GitHub App

        * **AND** Authenticate with User Name and Password
      </td>
    </tr>
  </tbody>
</Table>

## Before You Begin

### Authentication Methods

You can connect the adapter using either of the following authentication methods:

* [Authenticating with an Authorization Token](/docs/github#authenticating-with-an-authorization-token)
* [Authenticating with the GitHub app](/docs/github#authenticating-with-a-github-app)
* **(Only for fetching Application Settings and Licenses)** Prove the following parameters: [Custom Login URL, User Name, Password, Multi-factor Authentication](/docs/github#fetching-application-settings)

### APIs

Axonius uses the [GitHub API](https://developer.github.com/v3/).

### Permissions

Refer to [GitHub Permissions](/docs/github-permissions) for full details.

### Authenticating with an Authorization Token

1. From within a GitHub app, navigate to **Personal access tokens** `>` **Fine-grained token**.
2. Enter a token name.
3. Set the expiration date for one year after the current date.

<Callout icon="📘" theme="info">
  Note

  You must regenerate the token and replace it in the adapter connection before the expiration date (at most, one year from creation).
</Callout>

![GitHub\_TokenExpiration](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GitHub_TokenExpiration.png)

4. In the **Repository Access** section, select **All repositories**.

5. Set Repository and Account permissions according to the list in [Permissions for Authenticating with an Authorization Token](/docs/github-permissions#permissions-for-authenticating-with-an-authorization-token). Note that some asset types require specific permissions.

6. Set the Resource owner to **Organization**.

7. Click **Generate Token**.

8. Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Github_CopyButton.png) to copy the token.

   ![copy token](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Github_CopyToken.png)

9. Back in Axonius, paste the copied token into the **Authorization Token** connection parameter.

10. To use a personal access token with an organization that uses SAML single sign-on (SSO), you must first authorize the token to access the organization's SSO. For details,[see GitHub Docs - Authorizing a personal access token for use with SAML single sign-on](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on).

### Authenticating with a GitHub App

Follow these steps:

#### Creating and Configuring the App

1. In your GitHub account, navigate to **Settings `>` Developer settings**.
2. Select **GitHub Apps** and click **New GitHub App**.
3. Enter a name for your app.
4. Set the Homepage URL (this can be a GitHub repository or documentation URL).
5. *(Optional)* Set the Callback URL if the app will authenticate with OAuth.
6. Set permissions for the app based on what actions it needs to perform. For API usage, you might need to set specific permissions for repositories, organizations, etc.
7. Subscribe to events that your app needs to be notified about.
8. Click **Generate a private key**. This downloads a .pem file.
9. Store the .pem file for later use for authenticating your app.
10. Locate the App ID on the app's page, copy and paste it into the **GitHub App ID** connection parameter.

#### Assigning Permissions to the App

1. Set Repository, Account and Organization permissions according to the list in [Permissions for Authenticating with a GitHub App](/docs/github-permissions#permissions-for-authenticating-with-a-github-app). Note that some asset types require specific permissions.
2. Under **Account Permissions**, select the following options:
   1. **Access: Read-only** for **Email addresses** and **Followers**
   2. **Access: Read and write** for **Gists** and **Profile**

#### Installing the App on Your Organizations

1. On your app's settings page, under the **General** section, locate the **Installation URL**. This URL is used to install the app on any organization where you have sufficient permissions.
2. Log into GitHub as an organization admin.
3. Navigate to the installation URL.
4. Select the organizations from the drop-down menu and follow the prompts to install the app.
5. If your permissions are set to request access on a per-repository basis, specify which repositories the app can access.

#### Using the App as an API

To use the GitHub App as an API, you`ll need to authenticate using the App ID and the private key (.pem file) you downloaded. You`ll typically generate a JWT (JSON Web Token) and use it to authenticate API requests.

The GitHub documentation provides extensive guides on [authenticating with GitHub Apps](https://docs.github.com/en/developers/apps/authenticating-with-github-apps), including code examples for generating JWTs and making authenticated API requests.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### General - All Assets

#### Required Parameters

1. **GitHub Domain** - The hostname or IP address of the GitHub server.

<Callout icon="📘" theme="info">
  Note

  The **GitHub Domain** parameter is always required, for all authentication methods and asset types.
</Callout>

#### Optional Parameters

1. **Organization** - The organization of the GitHub account. To connect this adapter, you must either configure this parameter, or enable the **Fetch all organizations for logged user** Advanced Setting. You can also [fetch data without specifying the Organization](/docs/github#fetching-data-without-specifying-the-organization).
2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the GitHub domain.

### Authenticating with an Authorization Token (All Assets except for Application Settings)

1. **Authorization Token** - Specify the personal access token that has read access. If you authenticate using GitHub App leave this field blank.

### Authenticating with the GitHub App (All Assets except for Application Settings)

1. **Authenticate using GitHub App**- Check to enable authenticating using the GitHub App. Make sure you add the 'org' scope in GitHub.
2. **GitHub App ID** - The GitHub app ID can be found under the GitHub app's page.
3. **App Key File (pem)** - Click **Upload File** to upload the GitHub app's .pem key file. You can download this file from the GitHub app's page. When an App Key is set up, Axonius also fetches external collaborator data for GitHub apps.

### Fetching Application Settings and Licenses

<Callout icon="📘" theme="info">
  **Note**

  If you have the required permissions to fetch Licenses, the adapter will also automatically fetch Copilot license and metrics Info.
</Callout>

1. **Custom Login URL** - If you have GitHub Enterprise, enter your Custom Login URL here.
2. **User Name** and **Password** - Credentials used for the account that fetches Application Settings.
3. **Multi-factor Authentication** - The secret generated in the adapter for setting up 2-factor authentication for the adapter user created to fetch Application Settings data. This is only needed if the you enable it in the account assigned to the adapter.

![GitHub parameters drawer](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-XSAX4XID.png)

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

### Fetching data without Specifying the Organization

It is possible to fetch data without specifying the organization. This configuration is meant for GitHub accounts that have multiple organizations.

If an account has multiple organizations and wants to fetch data from many of them, you need to create the GithHub app, get the App ID and PEM file, install it on all the organizations you want to fetch from, and use the app as an API.

Before beginning this procedure, ensure that you have the necessary permissions in each organization to install apps. Also, note that the installation process needs to be done for each organization individually unless you are automating it through an API, which requires an initial installation to get started.

This section provides a general approach to creating, configuring, and using a GitHub App across multiple organizations. For detailed instructions and advanced configurations, refer to the [GitHub Developer documentation](https://docs.github.com/en/apps).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch public organizations for users** - Select whether to fetch the public organizations where each user is a member.

  * If disabled, this adapter will not fetch the public organizations each user is a  member of.

* **Fetch public gists for users** - Select whether to fetch data about public gists for users.

* **For each user, show in the user all the repositories they  have access in the organization** - For each user, show all the repositories in the organization to which they have access.

* **Fetch Teams to insert on the Users** - Select this option to fetch data for teams that the users belong to.

* **Fetch repository software bill of materials (SBOM)** - Select this option to enrich Repositories with Software Bill of Materials (SBOM).

* **Fetch repository runners** - Select to enrich repositories with runners data.

* **Enable fetching of default branches** - Select this option to fetch default branches from repositories.

* **Fetch branch rules** - Select this option to enrich default branches with protection rules.

* **Number of organizations to fetch concurrently** -  Enter the number of organizations to concurrently fetch by the adapter.

* **Fetch issues** - Select this to fetch GitHub Repository Issues.

* **Fetch Projects V2** - Select this to fetch Projects V2 as Application Resources.

* **Fetch public organizations for users** - Select this option to fetch the names of organizations that the users belong to.

* **Fetch all organizations for logged user** - Select whether to fetch all organizations for the logged user. To connect this adapter, you must either enable this setting or provide the **Organization** parameter for each connection's basic configuration.

* **Fetch user role and organization data** - Select to fetch each user role in the organization and additional information about the organization.

* **Fetch Repositories as devices (if Application Resources are not available)** - Select this option to fetch repositories as devices when application resources are not available.

* **Fetch code and secret scanning alerts** - Select this option to fetch code scanning and secret scanning alerts from GitHub as Alerts and Incidents assets.

* **Fetch repository vulnerabilities** - Select this option to fetch dependency vulnerabilities via GitHub Dependabot alerts, which provide information about vulnerabilities in the repository's dependencies. These vulnerabilities appear as a **GitHub Repositories** resource type under the **Application Resources** assets.

* **Fetch repository commits** - Select this option to fetch for each repository its commit history, if available.

<Callout icon="📘" theme="info">
  Note

  To access the REST API endpoints for code/secret scanning alerts and repository vulnerabilities, the authenticated user must be an owner or security manager for the organization. OAuth app tokens and personal access tokens (classic) must have the `security_events` or `repos` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.
</Callout>

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [GitHub - Remove User Extensions](https://docs.axonius.com/docs/github-delete-extension)
* [GitHub - Create Issue](/docs/github-create-issue)

<br />