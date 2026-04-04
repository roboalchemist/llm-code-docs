# Source: https://redocly.com/docs/realm/reunite/organization/sso/configure-okta.md

# Configure SSO with Okta and SAML2

In this video, we integrate Okta with Redocly to set up Single Sign-On (SSO) using SAML2.

This step-by-step tutorial shows you how to create an identity provider in Redocly, configure an Okta application, assign user groups, and test the connection.

It also covers using group attributes for customized access controls, giving you complete flexibility in managing team permissions.
Follow along and simplify your Redocly access with Okta!

iframe
## Preserve the Owner organization role

**Critical step:** Complete this step before clicking **Save** in Reunite to prevent getting locked out of your organization.

To prevent Okta from changing users' roles to the default organization role specified in the SSO settings:

1. In Okta, navigate to **Directory** > **Groups**.
2. Create a group named `redocly.owners`.
3. Navigate to **Directory** > **People** and assign users with an Owner role in your organization to the `redocly.owners` group.
4. Return to Reunite and click **Save** to complete the identity provider setup.


## Configure SSO in Redocly Reunite

1. Log into your Redocly Reunite account.
2. Navigate to **Organization settings** > **SSO**.
3. Click **Create identity provider**.
4. Select **SAML 2.0** as the SSO method.
5. Choose **Corporate SSO account** to enable SSO for both Reunite and internal projects.
6. Keep this page open - you'll need to copy values from here to Okta and then return to complete the setup.


## Create SAML application in Okta

1. In your Okta dashboard, navigate to **Applications**.
2. Click **Create App Integration**.
3. Select **SAML 2.0** as the sign-in method.
4. Click **Next**.
5. Fill out the general settings:
  - **App name**: Enter a descriptive name like "Redocly Reunite"
  - **App logo**: Upload your company logo (optional)
6. Copy the **Single sign-on URL** and **Audience URI** from your Reunite SSO page and paste them into the corresponding fields in Okta.


## Configure group attribute statements

Group attributes enable role-based access control (RBAC) by passing Okta group memberships to Redocly.

1. In the **Group Attribute Statements** section of your Okta SAML app:
  - **Name**: Enter `https://redocly.com/sso/teams`
  - **Name format**: Select **URI Reference**
  - **Filter**: Enter `redocly.`
2. This filter passes all groups that start with "redocly." to Redocly.
3. Click **Next**.
4. Select **This is an internal app that we have created**.
5. Click **Finish**.


## Get SAML setup information

1. In your newly created Okta app, click **View SAML setup instructions**.
2. Copy the following information - you'll need it to complete the Reunite setup:
  - **Identity Provider Single Sign-On URL**
  - **Identity Provider Issuer**
  - **X.509 Certificate**


## Complete SSO setup in Reunite

1. Return to your Reunite SSO configuration page.
2. Fill out the remaining fields with information from Okta:
  - **Single sign-on URL**: Paste the URL from Okta
  - **Issuer ID**: Paste the issuer URL from Okta
  - **X.509 Certificate**: Paste the certificate from Okta
3. Set the **Default organization role** to **Owner** initially to ensure you don't lose administrative access.
4. Click **Save** to create the identity provider.


## Create and assign Okta groups

1. In Okta, navigate to **Directory** > **Groups**.
2. Create groups using the naming pattern that starts with "redocly.":
  - `redocly.owners` (for organization owners)
  - `redocly.members` (for organization members)
  - Add any project-specific groups as needed
3. Navigate to **Directory** > **People**.
4. Assign users to the appropriate groups.
5. Return to your SAML application in Okta.
6. Go to the **Assignments** tab.
7. Click **Assign** > **Assign to Groups**.
8. Assign your newly created groups to the application.


## Test SSO login

1. Log out of Reunite.
2. Navigate to your organization's SSO login URL: `https://app.redocly.com/org/YOUR_ORG_SLUG`
3. Click **Login with SSO**.
4. Complete the Okta authentication flow.
5. If you're using the same email address as your existing Redocly account, you'll be prompted to link accounts.
6. Verify you can access all expected features and that your organization role is preserved.


## Update default organization role

After confirming SSO works correctly, you can adjust the default role for new users:

1. In Reunite, navigate to **Organization settings** > **SSO**.
2. Edit your identity provider.
3. Change the **Default organization role** to **Member** or **Viewer** based on your security requirements.
4. Save the changes.
5. Test by logging out and back in to ensure you retain access.


## Test project SSO and RBAC

To test project-level access control using Okta groups:

1. In your project's `redocly.yaml` file, configure SSO and RBAC:

```yaml
sso:
  type: corporate
rbac:
  content:
    "**": read
  tutorials:
    redocly.developers: read
```
This example allows everyone to read all content, but restricts tutorials to the `redocly.developers` group.
2. Create the `redocly.developers` group in Okta.
3. Assign users to the group.
4. Assign the group to your SAML application in Okta.
5. Test access by logging into your project - users should only see content they have permissions for.


## Resources

- **[Single sign-on (SSO) concepts](/docs/realm/reunite/organization/sso/sso)** - Understand different identity provider types and how they apply to project authentication and access control
- **[Add an identity provider](/docs/realm/reunite/organization/sso/add-idp)** - Add identity providers in Reunite for centralized authentication management across your projects
- **[Configure SSO](/docs/realm/reunite/organization/sso/configure-sso)** - Enable multiple identity provider types for flexible project authentication options
- **[Role-based access control (RBAC)](/docs/realm/access/rbac)** - Grant specific users access to specific content using role-based permissions and access controls