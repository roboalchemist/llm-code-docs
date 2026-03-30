# Source: https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-okta.md

# Set up SAML SSO with Okta

This guide walks through configuring Okta as your GraphOS organization's identity provider (IdP) for SAML-based SSO.
Once you've set up your integration, you need to [assign users to it in Okta](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-okta.md#assign-users-in-okta) so they can access GraphOS Studio via SSO.

Before assigning users, Apollo recommends setting a [default GraphOS role](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-okta.md#set-default-graphos-role) for users logging in via SSO.
You can also configure Okta to [assign GraphOS roles](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-okta.md#assign-graphos-roles-in-okta) to your users based on their Okta groups.

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

3. In the dialog that appears, select **SAML 2.0** as your sign-in method. Click **Next**.

4. The **Create SAML Integration** dialog appears. In the **General Settings** step, provide the following values:

   * **App integration name**: `Apollo GraphOS`
   * **Logo**: [Apollo logo](https://www.apollographql.com/docs/img/apollo-sk-logo.png) (optional)

   Then click **Next**.

5. In the **Configure SAML** step, provide the following values:

   * **Single sign on URL**: Single sign-on URL provided by the setup wizard
     * Also check **Use this for Recipient URL and Destination URL**.
   * **Audience URI (SP Entity ID)**: Entity ID provided by the setup wizard
   * Leave the default values for other settings, including leaving the **RelayState** blank.

6. Still in the **Configure SAML** step, scroll down to **Attribute Statements**. Set values for the following attributes:

   * `sub`: `user.email`
   * `email`: `user.email`
   * `given_name`: `user.firstName`
   * `family_name`: `user.lastName`

   Leave the **Name format** as `Unspecified`.

   Then click **Next**.

7. For the app type, select that it's an internal app. Click **Finish**.

8. In the setup wizard in GraphOS Studio, select whether your Okta implementation requires signing an AuthnRequest.

9. In the setup wizard in GraphOS Studio, click **Continue**.

### Step 3. Share SSO metadata with Apollo

1. In your Okta Administrator Dashboard, go to the **Sign On > Settings > SAML 2.0 > Metadata details** section in the app integration you just created.

2. Copy and paste the contents of the **Metadata URL** text box into the setup wizard in GraphOS Studio. Once the wizard shows the green success banner that says **Successfully parsed SAML metadata**, click **Continue**.

### Step 4. Verify details

The GraphOS Studio setup wizard populates your SSO metadata based on the URL you entered in the last step. Verify the values are correct.

You can find your **EntityID** and **SSO URL** in your Okta Administrator Dashboard in the app integration you created for GraphOS.

* Your app integration's **Entity ID** is in the **Sign On** tab. Scroll down to the **SAML 2.0** section and look for a field labeled **Issuer**. (You may need to click **More details** to see it.) This field contains the Entity ID. It uses a URL format: `http://www.okta.com/<unique-id>`.
* The **SSO URL** is also in the **SAML 2.0** section in a field labeled **Sign on URL**.

Once you've verified the values or corrected them, click **Continue**.

### Step 5. Verify SSO Configuration

To verify that your SSO configuration works, click **Login with new SSO** in the GraphOS Studio wizard.
This button launches a new login session in a new browser tab. You may need to assign yourself to the application in your IdP first.

Once you successfully login using your new configuration, click **Continue**.

### Step 6. Enable SSO

Once you've verified your new SSO configuration works, you'll be prompted to finalize your configuration.

Once your SSO connection is finalized, all non-SSO user accounts are removed from your GraphOS organization. This means:

* If team members could previously login before you implemented SSO, they must re-login to GraphOS Studio via SSO.
* Signing in via SSO creates new user profiles separate from previous non-SSO user profiles.
* Any [personal API keys](https://www.apollographql.com/docs/graphos/platform/access-management/account#personal-api-keys) associated with non-SSO user profiles will be lost.
  * [Graph API keys](https://www.apollographql.com/docs/graphos/platform/access-management/api-keys#graph-api-keys) are unaffected and remain functional.
* You must reassign any [GraphOS roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles) associated with previous user profiles.

You can set a [default role](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-okta.md#set-default-graphos-role) for any users signing in with SSO. Apollo recommends setting the default role before [assigning users](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-okta.md#assign-users-in-okta).

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

#### Step 2: Configure GraphOS application

1. In your Okta Administrator Dashboard left navigation, go to **Applications** > **Applications**.
   Select the GraphOS Studio application created during SSO configuration.

2. In the **General** tab, scroll to the **SAML Settings** section and click **Edit**.

3. Once in the **General Settings** section, click the **Next** button to move to the SAML configuration section.

4. Scroll to the **Attribute Statements (optional)** section and add these new attribute statement(s).
   * For organization-wide roles, the **Name** should be `graphos_org_role`, and the **Value** should be `appuser.graphos_org_role`.
   * For graph-specific roles, the **Name** should be `graphos_graph_roles`, and the **Value** should be `appuser.graphos_graph_roles`.

5. To save this change, click **Next** at the bottom of the screen, then **Finish** on the next screen.

#### (Optional) Step 3: Assign organization-wide GraphOS roles to Okta groups

Follow these steps to use the `graphos_org_role` attribute to set [organization-wide roles](https://www.apollographql.com/docs/graphos/platform/access-management/member-roles#organization-wide-member-roles) based on Okta groups.

1. In your Okta GraphOS Studio application, open the **Assignments** > **Groups** tab.

2. If the desired groups are already assigned to the application, click the pencil icon next to a group to edit it. Otherwise, assign the group by clicking the **Assign** > **Assign to Groups** dropdown.

3. Whether editing or assigning a group for the first time, select the appropriate **GraphOS Organization Role** for each.

4. Ensure the groups are prioritized correctly. The groups with more privileged access should have a higher priority.

   * In the example above, the **Apollo Admins** group has the highest priority (1). Suppose this group has the most privileges as **Org admins**.
   * Next, suppose the **Feature Team 1** has the **Graph Admin** role.
   * The rest of the **Engineering** organization has the **Contributor** role.
   * This priority order ensures a user belonging to the Apollo Admin group has **Org admin** privileges, even if they also belong to Feature Team 1 and the Engineering groups. If a user only belongs to the Engineering group, they receive the **Contributor** role.

#### (Optional) Step 4: Assign graph-specific GraphOS roles

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

### Role assignment behavior

Once you've completed the previous steps, whenever a user signs into GraphOS, they receive the role based on their IdP groups and/or individual graph-specific roles. If they don't belong to an IdP group that was assigned a role, they receive the [SSO default role](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-okta.md#set-default-graphos-role).

If a user's assigned role changes in IdP while logged into GraphOS Studio, they must log out of Studio and back in to receive their new role and permissions.

#### Sending multiple roles

Each GraphOS team member can only have one organization-wide role. If your IdP sends multiple roles for a single user, GraphOS treats it as [invalid](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-okta.md#invalid-role). This should only be a concern if you incorrectly configured the [`graphos_org_role` user attribute](https://www.apollographql.com/docs/graphos/platform/access-management/sso/saml-okta.md#step-1-add-user-attributes). If a user is part of multiple groups, IdPs generally only send the role corresponding to the highest priority group or last claim.

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
