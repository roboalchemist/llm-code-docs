# Source: https://docs.axonius.com/docs/asana.md

# Asana

Asana is a web and mobile work management platform designed to help teams organize, track, and manage their work.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* SaaS data

## Parameters

1. **Asana API URL** *(required, default: `https://app.asana.com`)* - The hostname or IP address of the Asana server.

2. **Access Token** *(required)* - An API Key associated with a user account that has permissions to fetch assets.
   To generate an access token, see [asana Personal access token](https://developers.asana.com/docs/personal-access-token).

3. **Capture User from Workspaces** - Enter a comma separated list of either Workspace names or Workspace GIDs to fetch.

4. **Verify SSL**  - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. **User Name and Password** *(only used to fetch SaaS data)* - The username and the password of an Axonius SaaS Applications dedicated user credentials.

9. **2FA Secret Key** *(only used to fetch SaaS data)* - The secret generated in the adapter for setting up 2-factor authentication for the adapter  user created to collect SaaS data.

10. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![AsanaSM](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AsanaSM.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch users  last login**   - Select whether to fetch information about the last login of the user.
* **Fetch groups**  - Select whether to fetch groups.
* **Fetch User Status** - Select this option to fetch the logs for each user, and determine the user status (for example: Member, Admin, Guest, and Accepted Invite) based on the last log.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Asana Developers API](https://developers.asana.com/docs/how-users-are-organized).

## Adapter Integration Setup

### Create a User Account (Axonius SaaS Applications)

<Callout icon="📘" theme="info">
  Note

  This is only required for Axonius SaaS Applications.
</Callout>

<Callout icon="💡" theme="warn">
  While to access SaaS data you need to grant roles and/or permissions that include write capabilities, the adapter only actually reads data from the application.
</Callout>

1. Log in as administrator to Asana.
2. Click the red '+' button next to your profile picture at the top right. Then click invite.
3. Select a team and specify a designated email address for Axonius SaaS Applications.
4. Open the received email and complete the signup.

<Callout icon="📘" theme="info">
  NOTE

  Copy the **Email address and password**, that is required for the as the username and password to fetch SaaS data in the adapter configuration parameter.
</Callout>

5. Click your profile picture at the top right. Click **Admin Console** and then click **Members** on the left.
6. Edit the user you have just invited and change its role to Admin.

### Create a Personal Access Token (PAT)

1. Log in with the newly created user account.
2. From within Asana, click your profile photo from the top bar and select **My Profile Settings**.
3. Click the **Apps** tab.
4. Click **Manage Developer Apps**.
5. Click **+ Create New Token**
6. Type a description of what you’ll use the Personal Access Token for.
7. Click **Create**.

<Callout icon="📘" theme="info">
  Note

  Copy the **token**, that is required for the [Access token](#connection-parameters) adapter configuration parameter.
</Callout>

## Supported From Version

Supported from Axonius version 4.5