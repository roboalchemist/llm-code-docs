# Source: https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-microsoft-entra-id.md

# Set up OIDC SSO with Microsoft Entra ID (formerly Azure AD)

This guide walks through configuring Microsoft Entra ID (formerly known as Azure Active Directory) as your GraphOS organization's identity provider (IdP) for OIDC-based SSO.
Once you've set up your integration, you need to assign users to it in Entra ID so they can access GraphOS Studio via SSO.

Before assigning users, Apollo recommends setting a [default GraphOS role](https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-microsoft-entra-id.md#set-default-graphos-role) for users logging in via SSO.
You can also configure Entra ID to [assign GraphOS roles](https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-microsoft-entra-id.md#assign-graphos-roles-in-entra-id) to your users based on their Entra ID groups.

## SSO impact on user accounts and access

For organizations using SSO, access to GraphOS is exclusively managed through your IdP.
Any [invitation links](https://www.apollographql.com/docs/graphos/org/members/#inviting-members) created before SSO setup will be automatically revoked and you won't be able to create new invitation links once SSO is enabled.
To give team members access, you must assign them to the GraphOS application in your IdP.

Once your SSO connection is finalized, all non-SSO user accounts are removed from your GraphOS organization. This means:

* If team members could previously login before you implemented SSO, they must re-login to GraphOS Studio via SSO.
* Signing in via SSO creates new user profiles separate from previous non-SSO user profiles.
* Any [personal API keys](https://www.apollographql.com/docs/graphos/platform/access-management/account#personal-api-keys) associated with non-SSO user profiles will be lost.
  * [Graph API keys](https://www.apollographql.com/docs/graphos/platform/access-management/api-keys#graph-api-keys) are unaffected and remain functional.
* You must reassign any [GraphOS roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles) associated with previous user profiles.

## Prerequisites

Setup requires:

* A GraphOS user account with the [**Org Admin** role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles/#organization-wide-member-roles)
  * Check the **Members** tab in [GraphOS Studio](https://studio.apollographql.com/) to see your role and which team members are org admins
* Administrative access to your IdP

## Setup

### Step 1. Enter your SSO details

### Step 2. Create an Entra ID app registration

1. Once you reach **Step 2: Configure Your IdP** in the wizard, go to your [Microsoft Entra admin center](https://entra.microsoft.com/). Alternatively, you can sign in to the [Azure Portal](http://portal.azure.com/) and then go to **Microsoft Entra ID**.

2. In Entra, go to **Identity > Applications > App registrations**. If accessing Entra from the Azure Portal, go to **Manage > App registrations**. Select **+New registration** in the top menu.

3. On the **Register an application** page, provide the following information:

   * Enter a descriptive name for your application, such as `Apollo GraphOS`.
   * Under **Supported account types**, select which Microsoft account types should have access to GraphOS.
   * For **Redirect URI**, select **Web** and enter the redirect URI provided by the setup wizard.

4. Click **Register**.

5. From the **Overview** section of your newly created app registration, copy and paste your **Application (client) ID** into the **Client ID** field in the setup wizard.

6. Next to **Client credentials**, click **Add a certificate or secret** and create a new secret.

7. Copy and paste the secret's **Value** into the **Client Secret** field in the setup wizard.

8. Back in the **Overview** section, select **Endpoints** from the top menu.

9. Copy and open the **OpenID Connect metadata document** URL in a new browser tab. Find the **`issuer`** value. It should be formatted like `https://login.microsoftonline.com/unique-value/vx.x`. Copy and paste this URL into the **Issuer** field in the setup wizard.

10. Click **Continue**.

### Step 3. Configure OIDC

1. Confirm your sign-in redirect URL by comparing what appears in the GraphOS wizard with what appears in your Entra app registration. Go to your app registration's **Authentication** tab and check the **Web** > **Redirect URI**.

2. Next, from the **API permissions** section of your app registration, check whether `User.Read` is listed by default. If it isn't, add it manually:

   1. Select **+ Add a permission > Microsoft Graph > Application permissions**.
   2. Search for `User`, expand, and select `User.Read.All`. Click **Add permissions**.
   3. **Save** your changes.

3. Also from the **API Permissions** section, select **Grant admin consent for Default Directory** next to the **+ Add a permission** button. Doing this ensures that your users don't need to grant consent during SSO.

4. From the **Manifest** section of your app registration, find the `groupMembershipClaims` property. Change its value from `null` to either `"All"` or `"SecurityGroup"`. These values ensure that the access token includes the group membership claim during SSO.

5. **Save** your changes.

### Step 4. Verify SSO Configuration

To verify that your SSO configuration works, click **Login with new SSO** in the GraphOS Studio wizard.
This button launches a new login session in a new browser tab. You may need to assign yourself to the application in your IdP first.

Once you successfully login using your new configuration, click **Continue**.

### Step 5. Enable SSO

Once you've verified your new SSO configuration works, you'll be prompted to finalize your configuration.

Once your SSO connection is finalized, all non-SSO user accounts are removed from your GraphOS organization. This means:

* If team members could previously login before you implemented SSO, they must re-login to GraphOS Studio via SSO.
* Signing in via SSO creates new user profiles separate from previous non-SSO user profiles.
* Any [personal API keys](https://www.apollographql.com/docs/graphos/platform/access-management/account#personal-api-keys) associated with non-SSO user profiles will be lost.
  * [Graph API keys](https://www.apollographql.com/docs/graphos/platform/access-management/api-keys#graph-api-keys) are unaffected and remain functional.
* You must reassign any [GraphOS roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles) associated with previous user profiles.

You can set a [default role](https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-microsoft-entra-id.md#set-default-graphos-role) for any users signing in with SSO. Apollo recommends setting the default role before [assigning users](https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-microsoft-entra-id.md#assign-users-in-entra-id).

## Set default GraphOS role

Once you've enabled SSO, you can optionally set the default [GraphOS role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles) for new users logging in via SSO.
If you don't set a default, the default role is **Consumer**.
To update the default role for new SSO users, go to **Settings** > **Security** > **Single sign-on** and click **Update new user role**.

## Assign users in Entra ID

Once you've set up your Apollo GraphOS application in Entra ID, you need to assign users to it so they can access GraphOS.
You can assign individual users or groups from the **User and groups** page of your Apollo GraphOS application in Entra ID.

You may want to begin by adding yourself individually and then testing SSO by clicking **Test** at the bottom of the **Single sign-on** page.

Once you've successfully tested your own user's ability to use SSO, add any applicable users or groups.
Once you've confirmed the new configuration works for your users, remove any legacy Apollo GraphOS applications in Entra ID or app registrations in Azure AD if you have them.

## Assign GraphOS roles in Entra ID

Apollo recommends using *either* SSO or SCIM for role assignment.
If you use both, role assignments will overwrite one another.

### Setup

Follow steps 1 and 2 to set organization-wide roles and step 3 for graph-specific roles.

#### Step 1: Add `graphos_org_role` claim

1. In your [Microsoft Entra admin center](https://entra.microsoft.com/), go to **Identity** > **Applications** > **Enterprise applications** and select the GraphOS application you previously created.

2. Go to the **Single sign-on** section and click **Edit** next to **Attributes & Claims**.

3. Click **+Add new claim** and give your new claim the name `graphos_org_role`. Leave the **Namespace** blank.

4. Expand the **Claim conditions** section. This is where you'll map groups to GraphOS roles.

   One claim condition row represents one GraphOS role and all the groups you want to assign to it. For each GraphOS role you want to map groups to, select the following:

   * **User type**: `Members`
   * **Scoped Groups**: Select all Entra ID groups that should have the same GraphOS role.
   * **Source**: `Attribute`
   * **Value**: Enter the GraphOS role name in all caps without quotes. [EntraID inserts quotes for constant values](https://learn.microsoft.com/en-us/entra/identity-platform/jwt-claims-customization#view-or-edit-claims).

     The following `string` values are valid GraphOS [organization-wide roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles):
     * `ORG_ADMIN`
     * `GRAPH_ADMIN`
     * `CONTRIBUTOR`
     * `DOCUMENTER`
     * `OBSERVER`
     * `CONSUMER`
     * `BILLING_MANAGER`

   The order of the rows matters. Since Entra ID assigns values [based on the last condition met](https://learn.microsoft.com/en-us/entra/identity-platform/saml-claims-customization?WT.mc_id=Portal-Microsoft_AAD_IAM), you should assign groups to GraphOS roles in increasing order of permissions. This ensures that users who belongs to multiple groups get the highest level of permissions.

   * In the example above, imagine the general **Engineering** group is the **Scoped Group** for the `CONTRIBUTOR` role in the first claim condition.
   * Next, suppose a **Feature Team 1** group has the `GRAPH_ADMIN` role.
   * Finally, an **Apollo Admins** group has the most privileges as `ORG_ADMIN`s.
   * This order ensures a member of the Apollo Admin group has `ORG_ADMIN` privileges, even if they also belong to Feature Team 1 and the Engineering groups. If a user only belongs to the Engineering group, they receive the `CONTRIBUTOR` role.

5. Save your changes.

#### Step 2: Include claim in manifest

1. Still in your [Microsoft Entra admin center](https://entra.microsoft.com/), go to **Applications** > **App registrations** > **All applications** and select the GraphOS application you added claims to.

2. In the App registration left nav, open **Manage > Manifest**. Set both `isFallbackPublicClient` and `api.acceptMappedClaims` to `true`

3. Click **Save**.

#### (Optional) Step 3: Set graph-specific roles

Use the following steps to set `graphos_graph_roles` attributes on individual users.

In addition to administrative access to Entra ID, these steps require:

* Access to [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer) or the ability to use the [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/use-the-api)
* The [listed permissions](https://learn.microsoft.com/en-us/graph/api/application-post-extensionproperty?view=graph-rest-1.0\&tabs=http#permissions) for the extension property API

1. Find your Entra GraphOS application's ID for use in API calls. Note it down for use in the following steps. You can find your application ID either:

   * In the application's **Manifest** in the **App Registrations** view under `id`

   * Using a `GET` request to:
     ```url
     https://graph.microsoft.com/v1.0/applications?$select=id,displayName&$filter=displayName eq 'Apollo GraphOS'
     ```
     This assumes that your application's name is "Apollo GraphOS." If it isn't, change the portion after `displayName eq` to your application's name.

   The ID you use in API calls is different from the Application ID on the application's **Overview** page. Ensure you use one of the methods above to get the correct ID.

2. Define the `graphos_graph_roles` extension and attach it to your Entra Apollo GraphOS application using a `POST` request to:

   ```url
   https://graph.microsoft.com/v1.0/applications/{application-id}/extensionProperties'
   ```

   With the following request body:

   ```json
   {
     "name": "graphos_graph_roles",
     "dataType": "String",
     "isMultiValued": true,
     "targetObjects": [
         "User"
     ]
   }
   ```

   See the example in the Graph Explorer below:

   `POST` `https://graph.microsoft.com/v1.0/applications/8ec36bea-9fca-4aab-bacc-fb28d1bbb25d/extensionProperties`

3. Confirm the extension was created using the following `GET` request:

   ```url
   https://graph.microsoft.com/v1.0/applications/{application-id}/extensionProperties
   ```

   * For example, `GET` `https://graph.microsoft.com/v1.0/applications/8ec36bea-9fca-4aab-bacc-fb28d1bbb25d/extensionProperties`
   * Take note of the `value.name` in the response. It should have a format like `extension_{extension-id}_graphos_graph_roles`

4. Retrieve user ID of the user whose graph-specific roles you want to set. You can view a user's ID from **Users** > (Select User) > **Overview** > **Object ID**.

5. Define as many graph-specific roles as you like on the user with the following `PATCH` request:

   ```url
   https://graph.microsoft.com/v1.0/users/{user-id}
   ```

   * With a request body with the following format:

     ```json
     {
       "{extension-name}":
           [
               "{graph-id}:{graph-specific-role}",
               "{graph-id}:{graph-specific-role}"
           ]
     }
     ```

     * The extension name is what you saved after making the `GET` request in step 2.

     * A graph's ID is the portion of the graph ref before the `@`.

     * Valid values for graph roles are `GRAPH_ADMIN`, `CONTRIBUTOR`, `DOCUMENTER`, `OBSERVER`, and `CONSUMER`.

     * Ensure the delimiter between the graph ID and role is a colon (`:`).

     * For example, `PATCH` `https://graph.microsoft.com/v1.0/user/s456fc1be-7809-461a-8e0f-2884f5791af0` with the following request body:
       ```json
       {
         "extension_d7ebe566a2e2402c88e09e105336a3bf_graphos_graph_roles":
             [
                 "graph-1:GRAPH_ADMIN",
                 "graph-2:DOCUMENTER"
             ]
       }
       ```

     You should receive a successful response, but the response preview won't show any information.

     You confirm that roles were set in the next step.

6. Confirm the extension is set on the user with the following `GET` request:
   ```url
   https://graph.microsoft.com/v1.0/users/{user-id}?$select=<extension-name>
   ```
   * For example, `GET` `https://graph.microsoft.com/v1.0/user/s456fc1be-7809-461a-8e0f-2884f5791af0?$select=extension_d7ebe566a2e2402c88e09e105336a3bf_graphos_graph_roles
     `
   * You should see the array of graph IDs and roles in the response.

7. Add the `graphos_graph_roles` claim to the Entra application:

   * In your [Microsoft Entra admin center](https://entra.microsoft.com/), go to **Identity** > **Applications** > **Enterprise applications** and select the GraphOS application you previously created. Open the **Single sign-on** section and click **Edit** next to **Attributes & Claims**.
   * Click **+Add new claim** and give your new claim the name `graphos_graph_roles`. Leave the **Namespace** blank.
   * Expand the **Claim conditions** section and select the following:

     * **User type**: `Members`
     * **Scoped Groups**: Select all Entra ID groups that should have this claim.
     * **Source**: `Directory schema extension`
     * **Value**: In the modal that appears, select the Entra application, then in the **Add Extension Attributes** modal, select the `user.graphos_graph_roles`custom  extension you previously created.
     * Click **Add**.

     - Save the new claim.

### Role assignment behavior

Once you've completed the previous steps, whenever a user signs into GraphOS, they receive the role based on their IdP groups and/or individual graph-specific roles. If they don't belong to an IdP group that was assigned a role, they receive the [SSO default role](https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-microsoft-entra-id.md#set-default-graphos-role).

If a user's assigned role changes in IdP while logged into GraphOS Studio, they must log out of Studio and back in to receive their new role and permissions.

#### Sending multiple roles

Each GraphOS team member can only have one organization-wide role. If your IdP sends multiple roles for a single user, GraphOS treats it as [invalid](https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-microsoft-entra-id.md#invalid-role). This should only be a concern if you incorrectly configured the [`graphos_org_role` user attribute](https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-microsoft-entra-id.md#step-1-add-user-attributes). If a user is part of multiple groups, IdPs generally only send the role corresponding to the highest priority group or last claim.

Team members can have as many graph-specific roles as graphs. Their graph-specific role must have higher permissions than their organization-wide role to be applied.

#### Sending invalid roles

Only the `graphos_org_role` values specified in setup Step 1 are valid.
If your IdP sends an invalid `graphos_org_role`:

* Existing users keep their current roles.
* New users receive your organization's default role.
* Either way, the user will still be authenticated and allowed to log in.

#### Accidental removal of org admins

If your role assignment removes all org admins from your GraphOS organization, you can fix it by:

* Updating your assignments so that at least one group maps to the Org Admin role.
* Reaching out to [support@apollographql.com](mailto:support@apollographql.com) to update roles manually.
