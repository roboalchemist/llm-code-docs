# Source: https://docs.axonius.com/docs/lucidchart.md

# Lucidchart

Lucidchart allows users to collaborate on drawing, revising, and sharing charts and diagrams.

### Asset Types Fetched

* Users, Roles, Licenses, Application Settings, SaaS Applications

## Resources Required by Asset Type

The following connection parameters, advanced settings, permissions, and configurations are required to fetch each asset type.

Search by Asset Type to find the resources required for your specific needs.

<Callout icon="💡" theme="warn">
  Note

  All configurations must be performed by a user with Admin privileges who can access the Lucid admin console.
</Callout>

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Asset Type
      </th>

      <th>
        [Connection Parameters](/docs/lucidchart#connecting-the-adapter-in-axonius)
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
        * Host Name or IP Address
        * Client ID
        * Client Secret
        * One Time OAuth Access Code
      </td>

      <td>
        Developer privileges
      </td>

      <td>
        [Generating a Client ID and Client Secret](/docs/lucidchart#generating-a-client-id-and-client-secret)
        [Getting an Access Code](/docs/lucidchart#getting-the-access-code)
      </td>
    </tr>

    <tr>
      <td>
        Roles
      </td>

      <td>
        * Host Name or IP Address
        * One Time OAuth Access Code
        * Client ID
        * Client Secret
      </td>

      <td>
        Developer privileges
      </td>

      <td>
        [Generating a Client ID and Client Secret](/docs/lucidchart#generating-a-client-id-and-client-secret)
        [Getting an Access Code](/docs/lucidchart#getting-the-access-code)
      </td>
    </tr>

    <tr>
      <td>
        Licenses
      </td>

      <td>
        * Host Name or IP Address
        * Client ID
        * Client Secret
        * Login URL
        * Redirect URL
        * Account ID
        * User name
        * Password
        * 2FA Secret
      </td>

      <td>
        Developer privileges
      </td>

      <td>
        [Generating a Client ID and Client Secret](/docs/lucidchart#generating-a-client-id-and-client-secret)
        [Generating a Redirect URL](/docs/lucidchart#generating-a-redirect-url)
        [Getting the Username and Password](/docs/lucidchart#getting-the-username-and-password-creating-a-new-user-account)
      </td>
    </tr>

    <tr>
      <td>
        Application Settings
      </td>

      <td>
        * Host Name or IP Address
        * Client ID
        * Client Secret
        * Login URL
        * Redirect URL
        * Account ID
        * User name
        * Password
        * 2FA Secret
      </td>

      <td>
        * Developer privileges
        * Team Admin privileges
        * Developer privileges
        * Billing privileges
      </td>

      <td>
        [Generating a Client ID and Client Secret](/docs/lucidchart#generating-a-client-id-and-client-secret)
        [Generating a Redirect URL](/docs/lucidchart#generating-a-redirect-url)
        [Getting the Username and Password](/docs/lucidchart#getting-the-username-and-password-creating-a-new-user-account)
      </td>
    </tr>

    <tr>
      <td>
        SaaS Applications
      </td>

      <td>
        * Host Name or IP Address
        * Client ID
        * Client Secret
        * Login URL
        * Redirect URL
        * Account ID
        * User name
        * Password
        * 2FA Secret
      </td>

      <td>
        Developer privileges
      </td>

      <td>
        [Generating a Client ID and Client Secret](/docs/lucidchart#generating-a-client-id-and-client-secret)
        [Generating a Redirect URL](/docs/lucidchart#generating-a-redirect-url)
        [Getting the Username and Password](/docs/lucidchart#getting-the-username-and-password-creating-a-new-user-account)
      </td>
    </tr>
  </tbody>
</Table>

To set up Developer privileges, on your Lucid admin console, Go to **User Settings**> **Developer Settings**and check **Enable Developer tools**.

<Image align="center" border={false} width="1075px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-32YSC5XP.png" height="auto" />

### Required Ports

* 80
* 443

### APIs

Axonius uses the [Lucid API Version 1](https://lucid.readme.io/reference/client-creation).

#### Supported From Version

Supported from Axonius version 5.0

## Setting Up Lucidchart to Work with Axonius

### Generating a Client ID and Client Secret

<Callout icon="📘" theme="info">
  Note

  Client ID and Client Secret are required to fetch **all**asset types.
</Callout>

The Lucidchart adapter uses Oauth2 verification, which requires a Client ID and Client Secret.

1. Login as an Account Admin user to your Lucid admin console.
2. Ensure that the account has Developer tools Enabled (see above image).
3. From the left navigation menu, go to **App Integration** `>` **General** `>` **Custom OAuth app**.
4. Under **Create Custom OAuth 2.0 Client**, provide a name for your app and click on **Create OAuth 2.0 Client**. A new app is added.
5. Grant the *View users on your account* permission for the app.
6. Open the new app and select the **OAuth 2.0** tab.
7. Copy the generated **Client ID** and **Client Secret** and paste them into their corresponding parameters in Axonius. ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-AGTUMZLM.png)

#### Getting the Access Code

<Callout icon="📘" theme="info">
  Note

  Access code is required only for fetching Users and Roles.
</Callout>

This process creates an Account Token. For more information, see [Access Token Types](https://developer.lucid.co/rest-api/v1/#access-token-types).

1. Navigate to: `https://lucid.app/oauth2/authorizeAccount?client_id={CLIENT_ID}&redirect_uri=https://lucid.app/oauth2/clients/{CLIENT_ID}/redirect&scope=account.user:readonly+offline_access`
2. Select **Grant Access**.
3. You will be redirected to `lucid.app/oauth2/clients/{CLIENT_ID}/redirect`.
4. Underneath the verification code, click **Copy to Clipboard**.
5. In Axonius, paste the verification code into the **One Time OAuth Access Code** [parameter](/docs/lucidchart#connecting-the-adapter-in-axonius).

### Fetching Licenses, Application Settings, and SaaS Applications

#### Generating a Redirect URL

Paste the following URL into the **Redirect URL** [parameter](/docs/lucidchart#connecting-the-adapter-in-axonius) (make sure to add your specific [Client ID](/docs/lucidchart#generating-a-client-id-and-client-secret) into the URL):

`https://lucid.app/oauth2/clients{CLIENT_ID}/redirect`

#### Getting the Username and Password (Creating a New User Account)

1. Login as an admin user to your Lucid admin console.
2. From the left navigation menu, go to **Users**.
3. Click **Add Users** `>` **Add a single user**.
4. Provide an email address you can access.
5. Edit the users' roles and set it as **Team Admin Privileges**, **Developer Privileges**, and **Billing Admin Privileges**.
6. You will receive an activation email. Open the email and use it to set the password.
7. Copy the generated **Username** and **Password**.
8. Paste the copied values into their corresponding [parameters](/docs/lucidchart#connecting-the-adapter-in-axonius) in Axonius.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters. Refer to [Resources Required by Asset Type](/docs/lucidchart#resources-required-by-asset-type) for the parameters required for specific asset types.

1. **Host Name or IP Address** - The hostname or IP address of the Lucidchart server that Axonius can communicate with via the Required Ports.
2. **Client ID** and **Client Secret** - The Client ID and Client Secret for an account that has read access to the API. For more information, see [Generating a Client ID and Client Secret.](/docs/lucidchart#generating-a-client-id-and-client-secret)
3. **One Time OAuth Access Code** - The access coded generated in Lucidchart for getting the refresh token and access token, for accounts that authorize with OAuth. For more information, see [Getting the Access Code](/docs/lucidchart#getting-the-access-code).
4. **Verify SSL** *(default: false)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy***(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
6. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in Host Name or IP Address via the value supplied in HTTPS Proxy.
7. **HTTPS Proxy Password***(optional, default: empty)* - The password to use when connecting to the server using the HTTPS Proxy.

<Image align="center" border={false} width="auto" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-J2209GNK.png" height="auto" />

**Parameters required to fetch Licenses, Application Settings and SaaS Applications:**

1. **Login URL** - Your Login URL. The format for this URl is: `https://lucid.app/users/login#/login`
2. **Redirect URL** - The Lucidchart OAuth app URI. The format for this URL is `https://lucid.app/oauth2/clients{CLIENT_ID}/redirect`.
3. **Account ID** - Your Lucidchart account ID. This is the number in your admin console URL. For example, if your URL is `https://admin.lucid.app/teams/123456789#/`, then the Account ID is 123456789.
4. **Username** and **Password** - The username and the password of an Axonius user account.
5. **2FA Secret** - Required only if the user created to collect Application Settings accesses Lucidchart through an SSO solution that requires 2-factor authentication. In this case, you need to generate a secret key in that solution and paste it here. See [Set Up Google Authenticator in for the Okta adapter](/docs/okta#step-5-set-up-google-authenticator), for example.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| API v1  | Yes       | --    |