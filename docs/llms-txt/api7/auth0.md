# Source: https://docs.api7.ai/enterprise/best-practices/dashboard-sso/oidc/auth0.md

# Source: https://docs.api7.ai/enterprise/3.8.x/best-practices/dashboard-sso/oidc/auth0.md

# Configure Dashboard SSO with Auth0

Single Sign-On (SSO) allows users to access multiple applications using a single set of credentials, streamlining the authentication process. In API7 Enterprise, SSO supports multiple protocols and provides the capability to manage users by importing them from existing identity providers.

This guide walks you through configuring Single Sign-On (SSO) for the API7 Enterprise Dashboard using Auth0 as the identity provider via the OpenID Connect (OIDC) protocol, and setting up role and permission boundary mappings for imported users.

## Set Up SSO Integration[â](#set-up-sso-integration "Direct link to Set Up SSO Integration")

This section guides you through configuring Single Sign-On (SSO) for the API7 Enterprise Dashboard using Auth0 as the identity provider.

### Configure Auth0[â](#configure-auth0 "Direct link to Configure Auth0")

1. Under **Applications**, create a new **application**, specify a custom name (for example, `API7 Dashboard`), and choose **Regular Web Applications** as the application type.

   <!-- -->

   1. Under the **Settings** tab, record **Client ID**, **Client Secret**, and **Domain** (Issuer) for later use.
   2. Under the **Connections** tab, make sure the **Username-Password-Authentication** built-in database connection is enabled.

2. Under **User Management > Users**, create a **user** and configure their password. Update the username as needed.

3. Review the application's discovery document at `https://<DOMAIN>/.well-known/openid-configuration`:

   <!-- -->

   1. Find the `end_session_endpoint` URL, for example, `https://<DOMAIN>.us.auth0.com/oidc/logout`. Record this value for later use.
   2. Review the `claims_supported` for configuring attributes mapping in API7 later.

4. Complete the [Create a Dashboard Login Option](#create-a-dashboard-login-option) instructions below, as the subsequent configurations require information from API7.

5. In the application, under the **Connections** tab:

   <!-- -->

   1. Configure the callback URL in the **Allowed Callback URLs**.
   2. Configure the value of `post_logout_redirect_uri` in the **Allowed Logout URLs**, for example, `https://dashboard.your-company.com`.
   3. Configure the dashboard address in the **Allowed Web Origins**.

The configuration is now complete. You should now be able to log in to API7 Dashboard with the new login option.

tip

If you enable the **google-oauth2** built-in social connection under the application's **Connections** tab and allow users to sign in to API7 using their social accounts, these users will not appear in Auth0âs **User Management** until they have logged in to API7 at least once. After their first login, the users will be visible in Auth0, and you can then assign roles to them.

### Create a Dashboard Login Option[â](#create-a-dashboard-login-option "Direct link to Create a Dashboard Login Option")

API7 Enterprise supports Single Sign-On (SSO) using multiple protocols. By integrating with existing user systems, it allows users to access API7 Enterprise without creating a new account.

1. Select **Organization** from the top navigation bar, then choose **Settings**.
2. Click **Add Login Option**.
3. Fill in the configuration:

* **Name**: The unique login name. The name should be identifiable for users. For example, if you configure the name to be `Employee Account`, you will see `Login with Employee Account` option in the Dashboard login page.

* **Provider**: Choose `OIDC`.

* **Issuer**: The issuer URL of the OpenID Connect provider, for example, `https://<DOMAIN>/`. Make sure to include the trailing slash at the end of the URL.

* **Client ID**: The unique identifier of your application assigned by the OIDC provider, for example `opqOFcwhzoRMRAekG1rfp7VdpU63tKsv`.

* **Client Secret**: Secret key used for authentication assigned by the OIDC provider.

* **Request Scope**: Scope values requested from the OIDC provider, which define the level of access and the claims included in the tokens. The `openid` scope is mandatory for all OIDC requests. Additional scopes can be included as needed, separated by spaces. For example, `openid profile email`.

* **Root URL**: The root address through which users access the API7 Dashboard, for example, `https://dashboard.your-company.com`. This URL must exactly match what users enter in their browsers, including the protocol (HTTP or HTTPS) and the port number if it differs from the standard ports (80 or 443).
  <!-- -->
  * The callback URL will be automatically generated as `<Root_URL>/api/oidc/<LOGIN_OPTION_ID>/callback`.

* **SSL verify**: Whether the OIDC providerâs SSL/TLS certificate should be validated.

* **Logout URL**: The URL that ends the user session and redirects them to the sign-in page. This should be the `end_session_endpoint` URL with the `post_logout_redirect_uri` query parameter set to the API7 Dashboard URL, for example `https://<DOMAIN>.us.auth0.com/oidc/logout?post_logout_redirect_uri=https://dashboard.your-company.com`.

* **Attributes Mapping**: API7 user fields mapping to OIDC claims. For example:

  <!-- -->

  * **username**: `name`
  * **email**: `email`
  * **name**: `name`

4. Click **Add**.
5. In the new OIDC login option, find the **Callback URL**, for example, `https://dashboard.your-company.com/api/oidc/<LOGIN_OPTION_ID>/callback`.
6. Return to the [Configure Auth0](#configure-auth0) above, step 5.

If all the above steps are completed, a new login option should now appear on the API7 Dashboard login page, allowing you to authenticate using the user created in your IdP. After the user signs in, log in as the admin user, navigate to **Organization** in the top navigation bar, then select **Users** to view the user.

Note that this user has no roles assigned yet, and therefore lacks permissions to manage resources in the Dashboard.

important

Deleting a user in the Dashboard removes all [roles and permission boundaries assigned in the API7 Dashboard](#enable-permission-boundary-mappings), but the user can still log in as a new user. To fully revoke access to the API7 Dashboard, the user must be removed from the IdP.

## Manage User Roles and Permissions[â](#manage-user-roles-and-permissions "Direct link to Manage User Roles and Permissions")

When automatic mappings are enabled, imported users can be automatically assigned roles and permission boundaries based on attributes from their identity provider, such as title, position, or department. These roles and permission boundaries are synchronized each time the user logs in, ensuring consistent access. A login optionâs mapping can include multiple rules that collectively determine a userâs access privileges.

info

If you prefer to manually update roles and permission boundaries for users (best suited for ad-hoc adjustments), see [Update a User Role](https://docs.api7.ai/enterprise/3.8.x/getting-started/rbac.md#update-a-user-role) and [Set Permission Boundary](https://docs.api7.ai/enterprise/3.8.x/getting-started/rbac.md#set-user-permission-boundary).

Automatic mappings take precedence over manually modified roles and permission boundaries. When mappings are active, manual changes in the Dashboard will be overwritten the next time the user logs in.

### Configure Auth0[â](#configure-auth0-1 "Direct link to Configure Auth0")

Role and permission boundary mappings rely on values configured in the IdP and passed to API7 Enterprise. The same IdP configuration applies when setting up mappings for roles and permission boundaries.

tip

In a production environment, it is recommended to implement fine-grained permission controls. For example, you can create detailed permissions in API7 and bind them to a role, then use the API7 Login Options settings to explicitly map each Auth0 role to the corresponding API7 role. Finally, assign the appropriate role to each user in Auth0, either manually or via an Action, to ensure proper access control.

1. Under **User Management > Roles**, create a new role, for example, `admin`.

2. Assign this role to the users who require admin rights in API7.

3. To make roles available to your application, create a `post-login` trigger under **Actions > Triggers**. Create an action `Inject Roles Claim` and deploy the following action:

   ```
   exports.onExecutePostLogin = async (event, api) => {
   // List of roles assigned to users in Auth0
   const roles = (event.authorization && event.authorization.roles) || [];

   // Use a namespace in the form of a URL for custom claims to avoid conflicts.
   const claimName = "https://dashboard.your-company.com/roles";

   // Write roles to ID Token and Access Token (array)
   api.idToken.setCustomClaim(claimName, roles);
   api.accessToken.setCustomClaim(claimName, roles);
   };
   ```

4. Drag the created action to Post Login trigger and apply the change.

### Configure Mappings in Dashboard[â](#configure-mappings-in-dashboard "Direct link to Configure Mappings in Dashboard")

This section describes how to configure role and permission boundary mappings in the API7 Enterprise Dashboard to define how user attributes from the identity provider are translated into access controls.

#### Enable Role Mappings[â](#enable-role-mappings "Direct link to Enable Role Mappings")

1. Select **Organization** from the top navigation bar, then choose **Settings**.
2. Select the login option.
3. Enable **Role Mapping**.
4. Fill in the configuration:

* **Internal Role**: The role in API7 Enterprise to assign. For example, `Super Admin`.
* **Role Attribute**: The [JSONPath](https://goessner.net/articles/JsonPath) to the corresponding attribute in the IdP. The attribute should correspond to a claim in the UserInfo, for example, `$['https://dashboard.your-company.com/roles']`.
* **Operation**: The comparison method used to match the attribute value. For example, `Exact Match in Array`.
* **Role Value**: The value of the attribute, for example, `admin`.

5. Click **Enable**.

Now all users with the `roles` attribute set to `admin` in the IdP will automatically be assigned the `Super Admin` role upon their next login.

Note that role mapping is dynamic. If a user's attribute changes in the IdP, their role will be automatically updated based on the role mapping rules the next time they log in to API7 Enterprise.

#### Enable Permission Boundary Mappings[â](#enable-permission-boundary-mappings "Direct link to Enable Permission Boundary Mappings")

1. Select **Organization** from the top navigation bar, then choose **Settings**.
2. Select the previously created login option.
3. Enable **Permission Boundary Mapping**.
4. Fill in the configuration:

* **Permission Policy**: The permission policy to assign in API7 Enterprise. For example, you can create a policy such as [`Admin License Restricted`](https://docs.api7.ai/enterprise/3.8.x/reference/permission-policy-examples.md#full-resource-access-with-license-update-restriction), which grants full resource access while restricting license updates; and apply the policy to this field.
* **Permission Boundary Attribute**: The [JSONPath](https://goessner.net/articles/JsonPath) to the corresponding attribute in the IdP. The attribute should correspond to a claim in the UserInfo, for example, `$['https://dashboard.your-company.com/roles']`.
* **Operation**: The comparison method used to match the attribute value. For example, `Exact Match in Array`.
* **Permission Boundary Value**: The value of the IdP attribute. For example, `admin`.

5. Click **Enable**.

Now all users with the `roles` attribute set to `admin` in the IdP will be automatically assigned the `Admin License Restricted` permission boundary upon their next login.

Note that permission boundary mapping is dynamic. If a user's attribute changes in the IdP, their permission boundary will be automatically updated based on the mapping rules the next time they log in to API7 Enterprise.

## Delete a Login Option[â](#delete-a-login-option "Direct link to Delete a Login Option")

warning

Deleting a login option will remove all users associated with that option in API7 Dashboard.

1. Select **Organization** from the top navigation bar, then choose **Users**.
2. Check if any users are still using this login option. If so, notify them before making any changes.
3. Select **Organization** from the top navigation bar, then choose **Settings**.
4. Click **Delete** of the target login option.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts
  <!-- -->
  * [Roles and Permission Policies](https://docs.api7.ai/enterprise/3.8.x/key-concepts/roles-and-permission-policies.md)

* Getting Started
  <!-- -->
  * [Create Custom Role](https://docs.api7.ai/enterprise/3.8.x/getting-started/create-custom-role.md)

* Reference

  <!-- -->

  * [Permission Policy Actions and Resources](https://docs.api7.ai/enterprise/3.8.x/reference/permission-policy-action-and-resource.md)
  * [Permission Policy Examples](https://docs.api7.ai/enterprise/3.8.x/reference/permission-policy-examples.md)
