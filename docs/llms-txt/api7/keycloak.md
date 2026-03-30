# Source: https://docs.api7.ai/enterprise/best-practices/dashboard-sso/oidc/keycloak.md

# Source: https://docs.api7.ai/enterprise/3.8.x/best-practices/dashboard-sso/oidc/keycloak.md

# Configure Dashboard SSO with Keycloak

Single Sign-On (SSO) allows users to access multiple applications using a single set of credentials, streamlining the authentication process. In API7 Enterprise, SSO supports multiple protocols and provides the capability to manage users by importing them from existing identity providers.

This guide walks you through configuring Single Sign-On (SSO) for the API7 Enterprise Dashboard using Keycloak as the identity provider via the OpenID Connect (OIDC) protocol, and setting up role and permission boundary mappings for imported users.

Explore our interactive demo to learn how to seamlessly integrate Keycloak SSO with API7 Enterprise.

## Set Up SSO Integration[â](#set-up-sso-integration "Direct link to Set Up SSO Integration")

This section guides you through configuring Single Sign-On (SSO) for the API7 Enterprise Dashboard using Keycloak as the identity provider.

### Configure Keycloak[â](#configure-keycloak "Direct link to Configure Keycloak")

This section describes example configuration in Keycloak 26.3.3. If you are using a different version, adjust the configuration accordingly.

1. Create a **realm**, for example `quickstart-realm`.

2. Create a **client**, for example `apisix-quickstart-client`. In the client:

   <!-- -->

   1. Enable **client authentication**, which sets the access type to be confidential.
   2. Enable **standard flow** (authorization code grant).
   3. Configure the **redirect URL**, for example `*`.
   4. After creating the client, navigate to the **Credentials** tab and obtain the **client secret**. Record this value for later use.

3. Create a **user**. In the user:

   <!-- -->

   1. Create a user password.
   2. Configure the user email, first name, and last name as needed.

4. In the **realm settings**, find the link to the discovery document. In the discovery document, record these values for later use:

   <!-- -->

   1. The `issuer` URL, for example, `http://192.168.10.101:8080/realms/quickstart-realm`.
   2. The `end_session_endpoint` URL, for example, `http://192.168.10.101:8080/realms/quickstart-realm/protocol/openid-connect/logout`.

### Create a Dashboard Login Option[â](#create-a-dashboard-login-option "Direct link to Create a Dashboard Login Option")

API7 Enterprise supports Single Sign-On (SSO) using multiple protocols. By integrating with existing user systems, it allows users to access API7 Enterprise without creating a new account.

1. Select **Organization** from the top navigation bar, then choose **Settings**.
2. Click **Add Login Option**.
3. Fill in the configuration:

* **Name**: The unique login name. The name should be identifiable for users. For example, if you configure the name to be `Employee Account`, you will see `Login with Employee Account` option in the Dashboard login page.

* **Provider**: Choose `OIDC`.

* **Issuer**: The issuer URL of the OpenID Connect provider, for example, `http://192.168.10.101:8080/realms/quickstart-realm`.

* **Client ID**: The unique identifier of your application assigned by the OIDC provider, for example `apisix-quickstart-client`.

* **Client Secret**: Secret key used for authentication assigned by the OIDC provider.

* **Request Scope**: Scope values requested from the OIDC provider, which define the level of access and the claims included in the tokens. The `openid` scope is mandatory for all OIDC requests. Additional scopes can be included as needed, separated by spaces. For example, `openid profile email`.

* **Root URL**: The root address through which users access the API7 Dashboard, for example, `https://dashboard.your-company.com`. This URL must exactly match what users enter in their browsers, including the protocol (HTTP or HTTPS) and the port number if it differs from the standard ports (80 or 443).
  <!-- -->
  * The callback URL will be automatically generated as `<Root_URL>/api/oidc/<LOGIN_OPTION_ID>/callback`.

* **SSL verify**: Whether the OIDC providerâs SSL/TLS certificate should be validated.

* **Logout URL**: The URL that ends the user session and redirects them to the sign-in page. This should be the `end_session_endpoint` URL with the `post_logout_redirect_uri` query parameter set to the API7 Dashboard URL, for example `http://192.168.10.101:8080/realms/quickstart-realm/protocol/openid-connect/logout?post_logout_redirect_uri=https://dashboard.your-company.com`.

* **Attributes Mapping**: API7 user fields mapping to OIDC claims. For example:

  <!-- -->

  * **username**: `preferred_username`
  * **email**: `email`
  * **name**: `name`

4. Click **Add**.

A new login option should now appear on the API7 Dashboard login page, allowing you to authenticate using the user created in your IdP. After the user signs in, log in as the admin user, navigate to **Organization** in the top navigation bar, then select **Users** to view the user.

Note that this user has no roles assigned yet, and therefore lacks permissions to manage resources in the Dashboard.

important

Deleting a user in the Dashboard removes all [roles and permission boundaries assigned in the API7 Dashboard](#enable-permission-boundary-mappings), but the user can still log in as a new user. To fully revoke access to the API7 Dashboard, the user must be removed from the IdP.

## Manage User Roles and Permissions[â](#manage-user-roles-and-permissions "Direct link to Manage User Roles and Permissions")

When automatic mappings are enabled, imported users can be automatically assigned roles and permission boundaries based on attributes from their identity provider, such as title, position, or department. These roles and permission boundaries are synchronized each time the user logs in, ensuring consistent access. A login optionâs mapping can include multiple rules that collectively determine a userâs access privileges.

info

If you prefer to manually update roles and permission boundaries for users (best suited for ad-hoc adjustments), see [Update a User Role](https://docs.api7.ai/enterprise/3.8.x/getting-started/rbac.md#update-a-user-role) and [Set Permission Boundary](https://docs.api7.ai/enterprise/3.8.x/getting-started/rbac.md#set-user-permission-boundary).

Automatic mappings take precedence over manually modified roles and permission boundaries. When mappings are active, manual changes in the Dashboard will be overwritten the next time the user logs in.

### Configure Keycloak[â](#configure-keycloak-1 "Direct link to Configure Keycloak")

Role and permission boundary mappings rely on values configured in the IdP and passed to API7 Enterprise. The same IdP configuration applies when setting up mappings for roles and permission boundaries.

For instance, to assign the `position` attribute with the value `admin` to a user in Keycloak, you can configure it either user attribute or via group membership. This section describes example configuration in Keycloak 26.3.3. If you are using a different version, adjust the configuration accordingly.

tip

In a production environment, it is recommended to implement fine-grained permission controls. For example, you can create detailed permissions in API7 and bind them to a role, then use the API7 Login Options settings to explicitly map each Keycloak atribute to the corresponding API7 role. Finally, assign the appropriate attribute to each user in Keycloak to ensure proper access control.

#### Configure User Attribute[â](#configure-user-attribute "Direct link to Configure User Attribute")

1. Enable **Unmanaged Attributes** from the **Realm Settings**.

2. Navigate to the user in Keycloak.

3. Go to the **Attributes** tab.

4. Add a new attribute, for example, with `Key` set to `position` and `Value` set to `admin`.

5. Navigate to **Client Scopes** and select a scope to which you want to add a mapper, for example, `profile`. Note that the selected scope should be configured in the API7 Dashboard **Request Scope**.

6. Add a mapper **by configuration**. Select **User Attribute** from the list, and fill in the configuration:

   * **Name**: Name of the mapper, for example, `position`.
   * **User Attribute**: Name of the user attribute, for example, `position`.
   * **Token Claim Name**: Name of the claim to insert into the token, for example, `position`.
   * By default, this attribute will be included in the UserInfo, which API7 Enterprise uses to obtain user attributes. For example:

   ```
   {
     "email":"johndoe@api7.ai",
     "email_verified":false,
     "name":"John Doe",
     "preferred_username":"johndoe",
     "sub":"b724c7ed-ad74-4330-9365-e599fdfbffcc",
     ...
     "position":"admin"
   }
   ```

In API7 Dashboard, you can use `$.position`, `Exact Match`, `admin` mapping rule. See [Configure Mappings in Dashboard](#configure-mappings-in-dashboard) for configuration steps.

#### Configure via Group Membership[â](#configure-via-group-membership "Direct link to Configure via Group Membership")

1. Navigate to **Groups** in Keycloak.

2. Create a new group, for example, `admin`.

3. Add the user to this group.

4. Navigate to **Client Scopes** and select a scope to which you want to add a mapper, for example, `profile`. Note that the selected scope should be configured in the API7 Dashboard **Request Scope**.

5. Add a mapper **by configuration**. Select **Group Membership** from the list, and fill in the configuration:

   * **Name**: Name of the mapper, for example, `groups`.
   * **Token Claim Name**: Name of the claim to insert into the token, for example, `groups`.
   * By default, this attribute will be included in the UserInfo, which API7 Enterprise uses to obtain user attributes. For example:

   ```
   {
     "email":"johndoe@api7.ai",
     "email_verified":false,
     "name":"John Doe",
     "preferred_username":"johndoe",
     "sub":"b724c7ed-ad74-4330-9365-e599fdfbffcc",
     ...
     "groups": ["/admin"]
   }
   ```

In API7 Dashboard, you can use `$.groups[*]`, `Contains String`, `admin` as the mapping rule. See [Configure Mappings in Dashboard](#configure-mappings-in-dashboard) for configuration steps.

### Configure Mappings in Dashboard[â](#configure-mappings-in-dashboard "Direct link to Configure Mappings in Dashboard")

This section describes how to configure role and permission boundary mappings in the API7 Enterprise Dashboard to define how user attributes from the identity provider are translated into access controls.

#### Enable Role Mappings[â](#enable-role-mappings "Direct link to Enable Role Mappings")

1. Select **Organization** from the top navigation bar, then choose **Settings**.
2. Select the login option.
3. Enable **Role Mapping**.
4. Fill in the configuration:

* **Internal Role**: The role in API7 Enterprise to assign. For example, `Super Admin`.
* **Role Attribute**: The [JSONPath](https://goessner.net/articles/JsonPath) to the corresponding attribute in the IdP. The attribute should correspond to a claim in the UserInfo, for example, `$.position`.
* **Operation**: The comparison method used to match the attribute value. For example, `Exact Match`.
* **Role Value**: The value of the IdP attribute, for example, `admin`.

5. Click **Enable**.

Now all users with the `position` attribute set to `admin` in the IdP will automatically be assigned the `Super Admin` role upon their next login.

Note that role mapping is dynamic. If a user's attribute changes in the IdP, their role will be automatically updated based on the role mapping rules the next time they log in to API7 Enterprise.

#### Enable Permission Boundary Mappings[â](#enable-permission-boundary-mappings "Direct link to Enable Permission Boundary Mappings")

1. Select **Organization** from the top navigation bar, then choose **Settings**.
2. Select the previously created login option.
3. Enable **Permission Boundary Mapping**.
4. Fill in the configuration:

* **Permission Policy**: The permission policy to assign in API7 Enterprise. For example, you can create a policy such as [`Admin License Restricted`](https://docs.api7.ai/enterprise/3.8.x/reference/permission-policy-examples.md#full-resource-access-with-license-update-restriction), which grants full resource access while restricting license updates; and apply the policy to this field.
* **Permission Boundary Attribute**: The [JSONPath](https://goessner.net/articles/JsonPath) to the corresponding attribute in the IdP. The attribute should correspond to a claim in the UserInfo, for example, `$.position`.
* **Operation**: The comparison method used to match the attribute value. For example, `Exact Match`.
* **Permission Boundary Value**: The value of the IdP attribute. For example, `admin`.

5. Click **Enable**.

Now all users with the `position` attribute set to `admin` in the IdP will be automatically assigned the `Admin License Restricted` permission boundary upon their next login.

Note that permission boundary mapping is dynamic. If a user's attribute changes in the IdP, their permission boundary will be automatically updated based on the mapping rules the next time they log in to API7 Enterprise.

## Synchronize User Data from IdP (SCIM)[â](#synchronize-user-data-from-idp-scim "Direct link to Synchronize User Data from IdP (SCIM)")

SCIM (System for Cross-domain Identity Management) is a protocol that can be used to synchronize user and group information from an Identity Provider (IdP) to API7 Enterprise. This eliminates the need to manually manage users and groups across multiple systems, saving time and reducing the risk of errors.

With SCIM Provisioning, API7 Enterprise automatically synchronizes user data whenever a new user is registered or deleted in your IdP.

1. Select **Organization** from the top navigation bar, then choose **Settings**.
2. Enable **SCIM Provisioning**.
3. Copy the `API7 SCIM Endpoint URL` and `SCIM Token`.
4. Configure SCIM in your IdP, if supported.

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
