# Source: https://redocly.com/docs/realm/reunite/organization/sso/configure-google-sso.md

# Configure Google Workspace as a SAML SSO

Follow the steps to configure Google Workspace SAML SSO integration with Reunite.

## Create an app in Google Workspace

1. In the Google Workspace Admin panel, navigate to **Apps** > **Web and mobile apps**.
2. Select **Add app** and choose **Custom SAML app**.
3. Fill in the form:
  - **App name**: `Redocly Reunite`
  - (Optional) **Description**: provide a description for your app.
  - (Optional) **Icon**: upload an image as your app's icon.
4. Click **Continue**.


## Add a SAML 2 identity provider in Reunite

1. In Reunite, navigate to your organization's **Overview** page.
2. Select **SSO and login** in the navigation menu on the left side of the page.
3. Click **Add** in the Guest or Corporate Identity Provider section.
4. Select **SAML2**.
5. Enter a name for your identity provider.
6. Select the default **Organization Role** for users who log in with the identity provider.
7. (Optional) Enter the name of the **Default Team**.
8. In **Single sign on URL**, enter: `https://auth.cloud.redocly.com/org/`*{your-organization-slug}*`/`.
9. In **Issuer ID**, enter the unique identifier of the identity provider.
10. In **x509 public certificate**, paste the certificate from the identity provider.
11. Click **Save**.


## Configure attributes in Google Workspace to send to Reunite

1. In the Google Workspace, in your app's configuration, in **App attribute**, enter: `https://redocly.com/sso/teams`.
2. (Optional) Select groups to transmit to Reunite.
3. (Optional) To preserve the Owner organization role for assigned users, create a group named `redocly.owners` and add users that have this organization role.


## Resources

- **[Single sign-on (SSO) concepts](/docs/realm/reunite/organization/sso/sso)** - Understand different identity provider types in Reunite and their implementation for project authentication
- **[Add an identity provider](/docs/realm/reunite/organization/sso/add-idp)** - Complete guide for adding identity providers in Reunite for streamlined authentication management
- **[Configure SSO](/docs/realm/reunite/organization/sso/configure-sso)** - Set up multiple identity provider types to provide users with flexible authentication options for your projects
- **[Role-based access control (RBAC)](/docs/realm/access/rbac)** - Implement advanced access control scenarios to grant specific users access to specific content and features