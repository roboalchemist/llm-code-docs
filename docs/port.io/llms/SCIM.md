# Source: https://docs.port.io/sso-rbac/SCIM.md

# SCIM

**SCIM (System for Cross-domain Identity Management)** enables automated user provisioning and de-provisioning from Identity Providers (IdP) like Okta, Azure AD, and Google Workspace directly into Port.

## What is SCIM?[â](#what-is-scim "Direct link to What is SCIM?")

SCIM automates the process of creating, updating, and deleting users in Port based on changes in your identity provider. This eliminates the need for manual user management and ensures your Port user directory stays synchronized with your IdP.

**Before SCIM:**

* Users had to log in first before being created in Port.
* IT admins had to manually add or remove users.
* User profile updates required manual intervention.

**With SCIM:**

* Users are automatically created, updated, or deleted in Port when changes happen in the identity provider.
* Changes occur before users log in.
* Reduced manual user management overhead.
* Automatic synchronization of user attributes from your IdP.

## Setup[â](#setup "Direct link to Setup")

To set up SCIM for your organization:

1. **Contact [Port support](http://support.port.io/)** to request SCIM enablement.

2. **Port will provide:**

   * SCIM endpoint URL.
   * SCIM authentication token.

3. **Configure your identity provider** using the endpoint and token provided by Port.

### Prerequisites[â](#prerequisites "Direct link to Prerequisites")

Before setting up SCIM, ensure you have:

* Migrated to [multiple organizations](/sso-rbac/multi-organization.md).
* An active SSO connection configured in Port.
* Admin access to your identity provider (Okta, Azure AD, or Google Workspace).

### Provider-specific setup[â](#provider-specific-setup "Direct link to Provider-specific setup")

* Okta
* Azure AD
* Google Workspace

- SAML
- OIDC

For Okta SAML applications, SCIM can be configured directly on the same application:

1. In your Okta Admin Console, navigate to your Port SAML application.
2. Go to the **Provisioning** tab.
3. Click **Configure API Integration**.
4. Enable **Enable API integration**.
5. Enter the SCIM endpoint URL and token provided by Port.
6. Set the **Unique identifier field** to `userName`.
7. For authentication, choose **HTTP Header** and use the SCIM token provided by Port.
8. Save your configuration.

To use [SCIM](https://auth0.com/docs/authenticate/protocols/scim) with your Okta OIDC SSO setup, you will need to create an additional Okta application according to the following instructions:

1. Create a new SSO application, of type SWA, and fill the form as below:

   ![](/img/sso/okta/OktaSWA.png)

   <br />

   <br />

   ![](/img/sso/okta/Okta_OIDC_SCIM.png)

   * `App's login page URL`

     * Organizations hosted in the EU: `https://app.getport.io`
     * Organizations hosted in the US: `https://app.us.getport.io`

   * `Who sets the credentials` - Administrator sets username, password is the same as user's Okta password

   * `Application username` - Okta username

   * `Update application username on` - Create and update

2. Edit the App Settings, and enable `Enable SCIM provisioning`

   ![](/img/sso/okta/OktaSCIMSecond.png)

After completing these steps, reach out to Port's team. You will be provided with:

* A SCIM `endpoint`
* A SCIM `token`

The `endpoint` and `token` will be used to complete the setup of the new SWA application.

3. Open the Provisioning tab in your application, and under `Integration` fill the following:

   * SCIM connector base URL: The `endpoint` you received from Port.

   * Unique identifier field for users: `userName`.

   * Supported provisioning actions: `Push New Users`, `Push Profile Updates`.

     **Note:** Only user events (`user.created`, `user.updated`, `user.deleted`) are supported. Using group events will cause a 403 error as they are not included in the Auth0 token's scope.

   * Authentication Mode: `HTTP Header`.

   * Authorization: The `token` you received from Port.

     ![](/img/sso/okta/OktaSCIMConfiguration.png)

   After configuration, press the `Test Connector Configuration` and confirm the integration was configured correctly.

4. Go to the newly created `To App` settings, and enable the following:

   * Create Users
   * Update User Attributes
   * Deactivate Users

   <br />

   ![](/img/sso/okta/OktaSCIMapp.png)

* SAML
* OIDC

For Azure AD SAML applications:

1. In the Azure portal, navigate to **Enterprise applications**.
2. Select your Port application.
3. Go to **Provisioning** in the left menu.
4. Click **Get started**.
5. Set **Provisioning Mode** to **Automatic**.
6. Enter the SCIM endpoint URL and token provided by Port in the **Tenant URL** and **Secret Token** fields.
7. Click **Test Connection** to verify the connection.
8. Click **Save** to enable provisioning.

Entra ID (AzureAD) OIDC applications support [SCIM](https://auth0.com/docs/authenticate/protocols/scim). Since Entra ID does not allow provisioning configuration directly on OIDC app registrations, you must create a separate provisioning application.

### Prerequisites

Before setting up SCIM, you must have a working OIDC SSO connection. Follow the [Entra ID OIDC setup guide](/sso-rbac/sso-providers/oidc/azure-ad.md#register-a-new-application), from **Register a new application** through **Provide application information to Port**.

### Create a provisioning application

To set up SCIM for Entra ID OIDC based applications, contact [Port support](http://support.port.io/).

You will be provided with:

* A SCIM `endpoint`.
* A SCIM `token`.

The `endpoint` and `token` will be used to set up the SCIM integration in your identity provider.

After receiving the SCIM `endpoint` and `token`, follow this [step-by-step guide](https://auth0.com/docs/authenticate/protocols/scim/inbound-scim-for-new-azure-ad-connections#configure-scim-in-azure-ad-for-oidc-apps) to enable SCIM.

Assign users to both applications

The OIDC application is used for **login**, while the provisioning application handles **user lifecycle management** (creating, updating, and deleting users). Users must be assigned to **both** applications to ensure full functionality.

**Functionality enabled by SCIM**

By enabling SCIM the following functionality will be enabled:

* Automatic deprovisioning of users (for example, when a user is unassigned from the SSO application, that user will automatically lose access to Port).

**Limitations**

* **Does not support group provisioning** - Group membership changes in your identity provider are not synchronized via SCIM.

For full user and group synchronization, rely on the SSO login process rather than SCIM.

For Google Workspace:

1. In the Google Admin Console, go to **Apps** > **Web and mobile apps**.
2. Select your Port application or create a new one.
3. Go to **User provisioning**.
4. Enable **SCIM provisioning**.
5. Enter the SCIM endpoint URL and token provided by Port.
6. Save your configuration.

## Field management[â](#field-management "Direct link to Field management")

When SCIM is enabled for a user, certain fields are managed exclusively by your identity provider and cannot be updated via the Port UI or API.

SCIM uses two metadata fields to track management:

* `managedByScim` - Set to `true` on first SCIM event, immutable thereafter.
* `scimUpdatedAt` - Timestamp of last SCIM update, used for ordering and staleness checks.

The following tabs describe which fields are synced from your identity provider and which remain editable in Port:

* SCIM-managed fields
* Non-SCIM fields

These fields are exclusively managed by SCIM and cannot be updated when `managedByScim = true`:

* `email` - User's email address.
* `firstName` - User's first name.
* `lastName` - User's last name.
* `phoneNumber` - User's phone number.
* `picture` - User's profile picture.
* `companyId` - User's company association.

SCIM field protection

Attempting to update SCIM-managed fields via the API will result in a `409 Conflict` error with code `SCIM_CONFLICT`.

These fields can be updated via the Port UI or API even when SCIM is enabled:

* `termsAccepted` - Terms of service acceptance status.
* `isInvisible` - User visibility setting.
* `supportLevel` - Support level assignment.
* `type` - User type (Standard or Service Account).
* `providers` - Authentication providers.
* `companyRole` - Role within the company.
* `roles` - Port platform roles (Admin, Moderator, Member).
* `teams` - Team memberships.

## Event processing[â](#event-processing "Direct link to Event processing")

SCIM processes three types of events from your identity provider:

* User created
* User updated
* User deleted

When a new user is assigned to the SSO application in your IdP:

* User is automatically created in Port with `managedByScim = true`.
* User is assigned to the appropriate organizations.
* SSO teams are synchronized.
* User can log in immediately without manual setup.

When user attributes change in your IdP:

* User profile fields are automatically updated in Port.
* Changes are applied before the user's next login.
* Only SCIM-managed fields are updated (email, name, phone, picture, company).

When a user is unassigned from the SSO application in your IdP:

* User is automatically deleted from Port (hard delete with cascade).
* All user data and associations are removed.
* User immediately loses access to Port.

User deletion

User deletion via SCIM is permanent and cannot be undone. All user data, including entity ownership and team memberships, will be removed.

## Post-login behavior[â](#post-login-behavior "Direct link to Post-login behavior")

When a SCIM-managed user logs in to Port:

* **Profile updates are skipped** - SCIM manages `email`, `firstName`, `lastName`, `phoneNumber`, and `picture`.
* **Existing user is returned** - No upsert occurs. The user record remains as managed by SCIM.
* **Teams are still synced** - SSO team membership is refreshed on login to ensure current team associations.

## API protection[â](#api-protection "Direct link to API protection")

Port's API includes protection logic to prevent conflicts between SCIM and manual updates:

* **SCIM-managed users** - Attempts to update SCIM-managed fields via API are blocked with a `409 Conflict` error.
* **Non-SCIM fields** - Can be updated normally via API even for SCIM-managed users.
* **Mixed updates** - If a request includes both SCIM and non-SCIM fields, only non-SCIM fields are updated.

## Limitations[â](#limitations "Direct link to Limitations")

* **OIDC requires separate application** - OIDC integrations require a separate SCIM application. Users must be assigned to both.
* **Not real-time** - SCIM operations may have delays and are not instantaneous.
* **Standard fields only** - Only standard user fields are synchronized, custom attributes are not supported.
* **Team sync on login** - While user data syncs automatically, team membership is refreshed primarily on user login.

## Troubleshooting[â](#troubleshooting "Direct link to Troubleshooting")

**User not created after assignment**

If a user is assigned in your IdP but not appearing in Port:

1. Verify SCIM is enabled for your SSO connection.
2. Ensure the SCIM endpoint is correctly configured in your IdP.
3. Contact [Port support](http://support.port.io/) if the issue persists.

**User updates not syncing**

If user profile changes in your IdP are not reflected in Port:

1. Verify the user has `managedByScim = true` in Port.
2. Check that the fields being updated are SCIM-managed fields.
3. Allow time for the SCIM event to process (may take a few minutes).
4. Contact Port support if updates are consistently not syncing.

**API update conflicts**

If you receive a `409 Conflict` error when updating a user:

* The user is SCIM-managed and you're attempting to update a SCIM-managed field.
* Update only non-SCIM fields, or make the change in your identity provider instead.

## Best practices[â](#best-practices "Direct link to Best practices")

* **Use SCIM for user lifecycle management** - Let SCIM handle user creation, updates, and deletion to maintain consistency.
* **Manage roles and teams in Port** - Use Port's UI or API to manage user roles and team memberships, as these are not SCIM-managed.
* **Monitor SCIM events** - Keep an eye on user provisioning to ensure expected behavior.
* **Coordinate with IdP changes** - Communicate with your IdP administrators about user changes that will affect Port access.

## Related documentation[â](#related-documentation "Direct link to Related documentation")

* [Manage users and teams](https://www.notion.so/sso-rbac/users-and-teams/manage-users-teams)
* [SSO providers](https://www.notion.so/sso-rbac/sso-providers/)
* [RBAC overview](https://www.notion.so/sso-rbac/rbac-overview/rbac-overview)
