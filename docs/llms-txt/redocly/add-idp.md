# Source: https://redocly.com/docs/realm/reunite/organization/sso/add-idp.md

# Add an identity provider (IdP)

Add SSO identity providers in Reunite, so users can use them for logging into Reunite as well as individual projects.
After you have added an IdP in Reunite, the identity provider can then be configured in the `redocly.yaml` configuration file for individual projects.

## Before you begin

Make sure you have the following:

- a SAML 2 or OpenID Connect-based identity provider
- the following information about your identity provider:
  - SAML 2
    - Single sign on URL
    - Issuer ID
    - x509 public certificate
    - NameID format set to email address
    - the following standard SAML attributes (claims) are supported:
      - `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname`
      - `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname`
      - `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name`
  - OpenID Connect
    - either a configuration JSON or URL
    - Client ID
    - Client Secret
- `owner` role in your organization


## Add a Corporate identity provider (IdP)

A Corporate identity provider is used to authenticate internal users into Reunite and projects.
You can only add one Corporate identity provider for your organization.

1. Log in to your Redocly instance.
2. Select **SSO and login** in the navigation menu on the left side of the page.
3. In the **Corporate** row under **Identity Provider**, click **+ Add** and select the type of identity provider you want to add - either SAML 2 or OpenID Connect.
4. Complete the form based on the information you have gathered about your SSO identity provider.
5. Click **Save**.


## Add a Guest identity provider (IdP)

A Guest identity provider is used to authenticate external users into projects.
You can only add one Guest identity provider for your organization.

1. Log in to your Redocly instance.
2. Select **SSO and login** in the navigation menu on the left side of the page.
3. In the **Guest** row under **Identity Provider**, click **+ Add** and select the type of identity provider you want to add - either SAML 2 or OpenID Connect.
4. Complete the form based on the information you have gathered about your SSO identity provider.
5. Click **Save**.


## Team mapping

Team mapping is an option when you add a Corporate or Guest IdP.
The option name differs depending on the protocol you are using to connect:

- For OpenID Connect, the option is referred to as *team claim mapping*.
- For SAML 2, the option is referred to as *team attribute mapping*.


In both instances, team mapping is a way to specify what you want your IdP groups to be labeled as in Reunite.

You can also use team mapping to assign users in your IdP groups different [project RBAC teams](/docs/realm/access#assign-roles-to-specified-teams) or [organization roles](/docs/realm/reunite/organization/teams#team-mapping) than the default team and role.

When users log in with an IdP, the groups assigned in the IdP override the RBAC teams assigned in Reunite.

To map IdP groups to Redocly default teams or project RBAC teams:

1. Select the **Configure team attribute mapping** or **Configure team claim mapping** checkbox.
2. Enter the IdP group name in the Value text box on the left side.
3. Enter the [Redocly default team tied to an organization role](/docs/realm/reunite/organization/teams#team-mapping) or [project RBAC team name](/docs/realm/access#assign-roles-to-specified-teams) into the **Team** text box on the right side.
4. Click the **Add mapping** button to add additional mappings as needed.
5. Click **Save**.


When users assigned to those groups in your IdP log in to Reunite, they have the project or organization role access assigned to those teams.

## Verified domains

Verified domains are a way for you to connect users with a given organization.
They only apply to corporate identity providers when logging into Reunite, not logging in to projects.
You can add a Verified domain on the **SSO and login** page in Reunite.

When you add a Verified domain to your organization, users logging in to Reunite with the verified domain email are automatically directed to the corporate identity provider, with the option to use Redocly credentials or social logins.
If you also select to require SSO authentication, users logging in to Reunite with the verified domain email domain can only log in using the corporate identity provider.

## Require SSO authentication

You can require SSO authentication for all members of your organization by selecting the **Require SSO authentication for all members of the Redocly organization** checkbox on the **SSO and Login** page.
Selecting this checkbox means that if you have `rbac` configured, users must log in with SSO credentials and if they do not have SSO credentials, they will lose access to the organization.

attention
Requiring SSO authentication does not require users to log in to your project.
To require login to your project, you must configure `rbac` or `requiresLogin`.
See [Configure RBAC](/docs/realm/access) or [requiresLogin](/docs/realm/config/access/requires-login) for more information.

## Resources

- **[Configure SSO](/docs/realm/reunite/organization/sso/configure-sso)** - Specify which identity providers users can access or disable SSO entirely for your project authentication settings
- **[Configure RBAC](/docs/realm/access)** - Limit user access to specific pages and features in your project and Reunite using role-based access control
- **[SSO configuration reference](/docs/realm/config/access/sso)** - Complete technical reference for all available SSO configuration options and implementation details
- **[Single sign-on (SSO) concepts](/docs/realm/reunite/organization/sso/sso)** - Understand different identity provider types and their configuration options for both Reunite and redocly.yaml file setup
- **[Role-based access control (RBAC) concepts](/docs/realm/access/rbac)** - Understand the components and architecture of Redocly's role-based access control system
- **[RBAC configuration reference](/docs/realm/config/access/rbac)** - Examples and configuration options for implementing RBAC in your redocly.yaml file with detailed setup instructions