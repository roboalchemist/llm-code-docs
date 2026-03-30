# Source: https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-okta.md

# Set up OIDC SSO with Okta

This guide walks through configuring Okta as your GraphOS organization's identity provider (IdP) for OIDC-based SSO. Once you've set up your integration, you need to assign users to it in Okta so they can access GraphOS Studio via SSO.

Before assigning users, Apollo recommends setting a [default GraphOS role](https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-okta.md#set-default-graphos-role) for users logging in via SSO.
You can also configure Okta to [assign GraphOS roles](https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-okta.md#assign-graphos-roles-in-okta) to your users based on their Okta groups.

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

### Step 2. Create a custom Okta app integration

1. Once you reach **Step 2: Configure Your IdP** in the wizard, open your Okta Administrator Dashboard in a separate browser tab.

2. In your Okta Administrator Dashboard, go to the **Applications** view and click **Create App Integration**.

   To use the latest version of Apollo's SSO, ensure you *create a custom app integration* in Okta rather than use the GraphOS app in the Okta Application Network.

3. In the dialog that appears, select **OIDC - OpenID Connect** as your sign-in method. For the **Application type**, select **Web Application**. Click **Next**.

4. In the **General Settings** section, provide the following values:

   * **App integration name**: `Apollo GraphOS`
   * **Logo**: [Apollo logo](https://www.apollographql.com/docs/img/apollo-sk-logo.png) (optional)

   Leave the other fields (for example, Proof of possession, Grant type) as the default values.

5. Add the following URIs:

* In the **Sign-in redirect URIs** section, add the Sign-in URL provided in the GraphOS wizard.
* In the **Sign-out redirect URIs** section, add `https://studio.apollographql.com`.
* Leave the **Base URIs** section empty.

6. For **Assignments**, you can select **Skip group assignment for now** or [assign the users](https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-okta.md#assign-users-in-okta) you want to have access to GraphOS. Click **Save**. This creates your custom app integration and brings you to its **General** tab.

7. In the **Client Credentials** section of the **General** tab, copy the **Client ID** and paste it into the Client ID input in the GraphOS wizard. Copy and paste the secret in the **Client Secrets** section into the wizard.

8. In Okta, while still on the app's **General tab** scroll to **General Settings** and click **Edit**. and scroll to the **Login** section. Add `https://studio.apollographql.com/sso/login` as the **Initiate login URI**. Click **Save**.

9. In Okta, open the **Sign On** tab. Scroll to the **OpenID Connect ID Token** section and click **Edit**. Change the **Issuer** to be **Okta URL** and click **Save**. Copy the URL into the **Issuer** input in the GraphOS Wizard.

10. In the setup wizard in GraphOS Studio, optionally enter a **Discovery URL**. Click **Next**.

### Step 3. Configure OIDC

1. In Okta, go back to the **General** tab of your custom app integration and confirm that the **Sign-in redirect URIs** contains the URL provided in the wizard.
2. You don't need to make any claims configurations, since by default, custom OIDC apps in Okta include all user attributes on the app profile.
3. Click **Next**.

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

You can set a [default role](https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-okta.md#set-default-graphos-role) for any users signing in with SSO. Apollo recommends setting the default role before [assigning users](https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-okta.md#assign-users-in-okta).

## Set default GraphOS role

Once you've enabled SSO, you can optionally set the default [GraphOS role](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles) for new users logging in via SSO.
If you don't set a default, the default role is **Consumer**.
To update the default role for new SSO users, go to **Settings** > **Security** > **Single sign-on** and click **Update new user role**.

## Assign users in Okta

Once your SSO is set up, you need to assign users to it so they can access GraphOS. You can assign individual users or groups by following these steps:

1. From your Okta Administrator Dashboard, open the **Applications** view from the left menu and open the Apollo GraphOS integration. Then, click the **Assignments** tab.

2. Click the **Assign** drop-down and then **Assign to People** or **Assign to Groups**.

3. Click **Assign** on the right of the people or group(s) you want to have access to your GraphOS Studio Org. Click **Done**.

Repeat these steps whenever you want to grant GraphOS Studio access to a new user or group.
Okta displays every user and group you've assigned to the integration in the **Assignments** tab.

## Assign GraphOS roles in Okta

Apollo recommends using *either* SSO or SCIM for role assignment.
If you use both, role assignments will overwrite one another.

### Setup

#### Step 1: Add user attributes

1. In your Okta Administrator Dashboard left navigation, go to **Directory** > **Profile Editor**. The profile editor displays native Okta user profiles and user profiles associated with applications. Select the GraphOS Studio User for the application created during SSO configuration.

2. Once in the GraphOS Studio User profile, click **+ Add Attribute**.

3. Enter the following values in the modal that appears:

   * To set organization-wide roles based on Okta groups:

     **Data type**
     `string`

     **Display name**
     `GraphOS Organization Role`

     **Variable name**
     `graphos_org_role`

     **Description**
     `GraphOS Studio organization-wide role`

     **Enum**
     Check `Define enumerated list of values`

     **Attribute members**

     **Display name**
     **Value**

     `Org Admin`
     `ORG_ADMIN`

     `Graph Admin`
     `GRAPH_ADMIN`

     `Contributor`
     `CONTRIBUTOR`

     `Documenter`
     `DOCUMENTER`

     `Observer`
     `OBSERVER`

     `Consumer`
     `CONSUMER`

     `Billing Manager`
     `BILLING_MANAGER`

     **Attribute type**
     `Group`

     Leave **Attribute length** and **Attribute required** as their default empty/unchecked values.

   * To set graph-specific roles:

     To create both `graphos_org_role` and `graphos_graph_roles` attributes, click **Save and Add Another** after you've created `graphos_org_role`.

     **Data type**
     `string array`

     **Display name**
     `GraphOS Graph Roles`

     **Variable name**
     `graphos_graph_roles`

     **Description**
     `GraphOS Studio graph-specific roles`

     **Enum**
     Do **NOT** check `Define enumerated list of values`

     **Attribute type**

     `Personal` or `Group`

     Use `Personal` if you plan to set graph-specific roles on a per-user basis
     Use `Group` if you plan to set graph-specific roles for entire Okta groups

     Leave **Attribute required** unchecked.

4. Click **Save**.

#### (Optional) Step 2: Assign Okta groups to GraphOS roles

Follow these steps to use the `graphos_org_role` attribute to set [organization-wide roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles) based on Okta groups.

1. In your Okta GraphOS Studio application, open the **Assignments** > **Groups** tab.

2. If the desired groups are already assigned to the application, click the pencil icon next to a group to edit it. Otherwise, assign the group by clicking the **Assign** > **Assign to Groups** dropdown.

3. Whether editing or assigning a group for the first time, select the appropriate **GraphOS Organization Role** for each.

4. Ensure the groups are prioritized correctly. The groups with more privileged access should have a higher priority.

   * In the example above, the **Apollo Admins** group has the highest priority (1). Suppose this group has the most privileges as **Org admins**.
   * Next, suppose the **Feature Team 1** has the **Graph Admin** role.
   * The rest of the **Engineering** organization has the **Contributor** role.
   * This priority order ensures a user belonging to the Apollo Admin group has **Org admin** privileges, even if they also belong to Feature Team 1 and the Engineering groups. If a user only belongs to the Engineering group, they receive the **Contributor** role.

#### (Optional) Step 3: Assign graph-specific GraphOS roles

Follow these steps to use the `graphos_graph_roles` attribute to set [graph-specific roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#graph-specific-member-roles) on groups or individuals.

1. In your Okta GraphOS Studio application, open the **Assignments** tab.

2. If the individual or group is already assigned to the app, click the pencil icon next to it. Otherwise, assign them by clicking the **Assign** dropdown.

3. Groups and individuals can have as many graph-specific roles as necessary. Use the `<graph-id>:<graph-role>` format for each graph-specific role.

   * A graph's ID is the portion of the graph ref before the `@`.
   * Valid values for graph-specific roles are `GRAPH_ADMIN`, `CONTRIBUTOR`, `DOCUMENTER`, `OBSERVER`, and `CONSUMER`.
   * Ensure the delimiter between the graph ID and role is a colon (`:`).

   When assigning individuals: if the user also has an organization-wide role assigned based on their Okta group, keep the **Assignment master** set to **Group** to ensure this role stays set for other graphs.

   For example, the user in the screenshot above receives the following roles:

   * A `DOCUMENTER` role for `doc-sandbox` graph
   * A `GRAPH_ADMIN` role for `another-graph`
   * `OBSERVER` for all other graphs in their organization, based on their group assignment.

A user's graph-specific role must have higher permissions than their organization-wide role to be applied.

#### Step 4: Configure GraphOS application

1. In your Okta Administrator Dashboard left navigation, go to **Security** > **API**.
   The **Authorization Servers** tab shows a list of your authorization servers. Click the pencil icon on the **Default** server.

2. Go to the **Claims** tab and click **Add Claim**.

3. In the modal that appears, enter the following values:

   For organization-wide roles:

   * Set **Name** to `graphos_org_role`
   * Keep **Include in token type** to **Access token**
   * Keep **Value type** as **Expression**
   * Set **Value** to `appuser.graphos_org_role`
   * You can keep **Include in** to **Any scope**. If you want to restrict it to certain scopes, keep at least the `openid` and `profile`s scopes.

     Click **Create**.

4. If setting graph-specific roles, repeat steps 2 - 3, setting the claim name and values to `graphos_graph_roles` and `appuser.graphos_graph_roles` respectively.

5. To test that your claims are being sent properly, go to the **Token Preview** tab. Enter the following **Request Properties**:

   * **OAuth/OIDC client**: The name of your application
   * **Grant type**: **Authorization Code**
   * **User**: Select a user from a group you've mapped GraphOS roles to.
   * **Scopes**: `openid` and `profile`

   Click **Preview Token**. In the **token** tab of the **Preview**, you should be able to see the expected `graphos_org_role` and/or `graphos_graph_roles` value(s) for the user.

### Role assignment behavior

Once you've completed the previous steps, whenever a user signs into GraphOS, they receive the role based on their IdP groups and/or individual graph-specific roles. If they don't belong to an IdP group that was assigned a role, they receive the [SSO default role](https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-okta.md#set-default-graphos-role).

If a user's assigned role changes in IdP while logged into GraphOS Studio, they must log out of Studio and back in to receive their new role and permissions.

#### Sending multiple roles

Each GraphOS team member can only have one organization-wide role. If your IdP sends multiple roles for a single user, GraphOS treats it as [invalid](https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-okta.md#invalid-role). This should only be a concern if you incorrectly configured the [`graphos_org_role` user attribute](https://www.apollographql.com/docs/graphos/platform/access-management/sso/oidc-okta.md#step-1-add-user-attributes). If a user is part of multiple groups, IdPs generally only send the role corresponding to the highest priority group or last claim.

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

#### Overriding a group role

You can override an individual user's group role by going to the **Assignments** tab in Okta, selecting the **People** filter, and clicking the pencil icon next to an individual. In the modal that appears, select  **Administrator** for the **Assignment master** and then select the appropriate GraphOS Organization role.

Once you've overridden an individual's role, group role updates won't affect them. You can revert an individual's settings to pull from group attributes by selecting **Convert assignments** from the **Assignments** > **People** tab.

Org Admins can also manually change user roles in GraphOS Studio. However, if you've configured SSO and role assignment through Okta, Apollo recommends using Okta as the single source of truth for identity and access management.
