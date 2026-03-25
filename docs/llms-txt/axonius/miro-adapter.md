# Source: https://docs.axonius.com/docs/miro-adapter.md

# Miro

Miro is a digital collaboration platform designed to facilitate remote and distributed team communication and project management.

<Callout icon="📘" theme="info">
  NOTE

  This adapter is only for the Miro Enterprise plan.
</Callout>

## Asset Types Fetched

This adapter fetches the following types of assets:

* Users, Roles, Groups, Licenses, Application Settings, SaaS Applications

## Before You Begin

### Authentication Methods

* For **all asset types except for Application Settings**: Client ID and Secret, One Time OAuth Access Code
* For **Application Settings only**: User Name, Password, and 2FA Secret Key (if required by your Miro environment)

### APIs

Axonius uses the [Miro REST API](https://developers.miro.com/reference/api-reference#enterprise-plan) In Miro's Enterprise plan.

### Required Permissions

The following permissions are required:

* identity:read
* team:read
* organizations:read
* organizations:teams:read
* **To fetch Account Settings:** boards:read
* **To fetch Entity Settings** boards:read
* **To fetch SaaS data:** When authentication with **Client ID** and **Client Secret**, the provided credentials must be associated with the appropriate [Miro scopes](https://developers.miro.com/reference/scopes).

## Adapter Integration Setup

<Callout icon="📘" theme="info">
  NOTE

  These instructions are relevant for users with either or both Axonius Cyber Assets and Axonius SaaS Applications.
</Callout>

#### Create an App in Miro

1. Ensure that your Miro user [has a Developer team](https://developers.miro.com/docs/create-a-developer-team).

2. From within a Miro account, click the account avatar to open the profile menu.

3. Select **Settings**.

4. Click the **Your apps** tab.

5. Click **+ Create new app**.<br />
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateNewApp.jpg)

6. Enter an app name (for example: Axonius SaaS Applications).

7. Click **Create App**.<br />
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateApp.jpg)

#### Add Redirect URI for OAuth2.0

1. On the App Settings page, locate the Redirect URI for OAuth2.0 section
2. Enter the following redirect URI: `https://localhost/adapters/miro_adapter`
3. Click **Add**.<br />
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RedirectURI.png)

#### Set App Permissions

1. On the App Settings page, locate the App URL section.
2. In the Permissions area, select the following permissions:
   * identity:read
   * team:read
   * organizations:read
   * organizations:teams:read
   * boards:read (to fetch Account Settings)
3. Click **Install app and get OAuth token**.

#### Generate the One Time OAuth Access Code

1. Navigate to the following URL (make sure you add in your client ID to the URL):
   `https://miro.com/oauth/authorize?response_type=code&client_id=**Your_Client_ID**&redirect_uri=https://localhost/adapters/miro_adapter`

2. On the dialog that opens, from the team drop-down list, select the relevant team.

3. Click **Add**.The browser redirects to Axonius.

4. Copy the `code` parameter from the browser's address bar.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AUthenticationParameter.png)

5. Paste the copied parameter into the One Time OAuth Access Code field in the Axonius configuration.

## Connecting the Adapter in Axonius

### Required Parameters - all asset types

1. **Host Name or IP Address** - The hostname or IP address of the Miro server. If Miro is not self-hosted, the Host Name must be `https://api.miro.com`.

### Required Parameters - all asset types except for Application Settings

1. **Client ID** and **Client Secret** - Miro Authentication credentials. Refer to [Get started with OAuth2.0 and Miro](https://developers.miro.com/docs/getting-started-with-oauth).

2. **One Time OAuth Access Code** - The one-time authentication code to get the refresh token. Refer to [Generate the One Time OAuth Access Code](/docs/miro-adapter#generate-the-one-time-oauth-access-code) below.

### Required Parameters - Application Settings

1. **User Name** and **Password** - The credentials for a user account that has the permissions to fetch assets.
2. **2FA Secret Key**- If you access Miro through an SSO solution that requires multi-factor authentication, you need to generate a secret key in that solution and paste it here. See [Set Up Google Authenticator](/docs/okta#step-5-set-up-google-authenticator) in the Okta adapter, for an example.

<Image border={false} src="https://files.readme.io/69b0e11db3070ec29ba880ad5cfb63cc5ac98704c0edc1d5bc6da1b8838b178a-image.png" />

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

1. **Fetch Account-Level Settings** - Select to fetch account settings. For this to work, you must have the boards:read permission.
2. **Fetch Entity-Level Settings** - Select to fetch entry-level settings. For this to work, you must have the boards:read permission.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

### Supported From Version

Supported from Axonius version 5.0